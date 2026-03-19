#!/usr/bin/env python3
# PURPOSE: Extract co-access graph from state (daily, handoff, handoff_archive)
# DEPENDENCIES: Python 3.9+, pathlib, re, json
# MODIFICATION NOTES: Brain Map pattern; portable for Harness and projects using state schema

"""
Build brain-map-graph.json from Harness state sources.

Sources:
- state/daily/YYYY-MM-DD.md (or .cursor/state/daily/)
- state/handoff_latest.md
- state/handoff_archive/*.md
- state/decision-log.md

Extracts .md paths, notes_touched, Paths artifacts. Co-access = files in same session.
Output: brain-map-graph.json (Brain Map schema).

Env: CURSOR_STATE_DIR, BRAIN_MAP_OUTPUT
"""

from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


# Group mapping (Brain Map schema)
CORE_FILES = {"AGENTS.md", "SOUL.md", "MEMORY.md", "USER.md", "IDENTITY.md", "TOOLS.md"}
CORE_PATTERNS = ["org-intent", "org_intent"]


def _find_state_dir(root: Path) -> Path:
    """Find state directory: root/state or root/.cursor/state."""
    for candidate in [root / "state", root / ".cursor" / "state"]:
        cand = candidate.resolve()
        if cand.exists() and cand.is_dir():
            return cand
    return (root / "state").resolve()


def _classify_group(path: str) -> str:
    """Classify node into Brain Map group."""
    p = path.lower().replace("\\", "/")
    if any(c in p for c in CORE_FILES) or any(pat in p for pat in CORE_PATTERNS):
        return "core"
    if ".cursor/state" in p or "handoff" in p or "daily" in p or "decision-log" in p or "state/" in p:
        return "memory"
    if "skills" in p or ".cursor/skills" in p:
        return "skills"
    if "frontier-ops" in p or "scripts" in p or "tools" in p or "workflows" in p:
        return "tools"
    if "docs" in p or "plans" in p or "drafts" in p:
        return "publishing"
    return "general"


def _classify_session_type(text: str) -> str:
    """Classify session type from journal/handoff text for edge coloring."""
    t = text.lower()
    if any(k in t for k in ["strategy", "roadmap", "planning", "product", "business"]):
        return "strategy"
    if any(k in t for k in ["memory", "identity", "voice", "self"]):
        return "memory"
    if any(k in t for k in ["publish", "article", "draft", "content"]):
        return "publishing"
    if any(k in t for k in ["deploy", "build", "api", "route", "server", "cron"]):
        return "infrastructure"
    if any(k in t for k in ["research", "analysis", "audit", "skill"]):
        return "research"
    return "general"


def _extract_md_paths(text: str) -> set[str]:
    """Extract .md file paths from text (bullet lists, [[wikilinks]], paths)."""
    paths: set[str] = set()
    # Wikilinks [[Note]] or [[path/to/note]]
    for m in re.finditer(r"\[\[([^\]]+)\]\]", text):
        p = m.group(1).strip()
        if not p.endswith(".md"):
            p = f"{p}.md"
        paths.add(p)
    # Paths ending in .md (relative or with slashes)
    for m in re.finditer(r"[\w./\-\\]+\\.md\b", text, re.IGNORECASE):
        paths.add(m.group(0).replace("\\", "/"))
    for m in re.finditer(r"[\w./\-]+\\.md\b", text, re.IGNORECASE):
        paths.add(m.group(0))
    # Bullet paths: - path/to/file.md
    for m in re.finditer(r"^[\s\-*]+\s*([\w./\-\\]+\\.md)\b", text, re.MULTILINE | re.IGNORECASE):
        paths.add(m.group(1).replace("\\", "/"))
    # notes_touched: comma-separated
    if "notes_touched" in text.lower():
        for m in re.finditer(r"notes_touched[:\s]+([^\n]+)", text, re.IGNORECASE):
            for part in re.split(r"[,;]", m.group(1)):
                p = part.strip()
                if p.endswith(".md") or ".md" in p:
                    paths.add(p.strip())
    return paths


def _normalize_path(p: str, root: Path | None = None) -> str:
    """Normalize path for node id (relative, forward slashes). Strip workspace prefix if present."""
    p = p.replace("\\", "/").strip()
    if root:
        root_str = str(root).replace("\\", "/")
        for prefix in [root_str + "/", root_str + "\\", root_str]:
            if p.lower().startswith(prefix.lower()):
                p = p[len(prefix) :].lstrip("/\\")
                break
    # Fallback: strip common absolute prefixes
    for prefix in ["D:/", "C:/", "d:/", "c:/"]:
        if p.lower().startswith(prefix):
            parts = p.split("/")
            if len(parts) >= 2:
                p = "/".join(parts[2:])  # strip drive and first segment
            break
    return p or "unknown.md"


def build_graph(state_dir: Path, output_path: Path, root: Path | None = None) -> dict[str, Any]:
    """Build brain-map graph from state directory."""
    if root is None:
        root = state_dir.parent.parent if (state_dir.parent.name == ".cursor") else state_dir.parent

    nodes: dict[str, dict[str, Any]] = {}
    edges: dict[tuple[str, str], dict[str, Any]] = {}
    session_count = 0

    def add_session(session_id: str, paths: set[str], text: str) -> None:
        nonlocal session_count
        if not paths:
            return
        session_count += 1
        session_type = _classify_session_type(text)
        paths = {_normalize_path(p, root) for p in paths if p.strip()}
        for p in paths:
            nodes.setdefault(
                p,
                {
                    "id": p,
                    "group": _classify_group(p),
                    "accessCount": 0,
                    "path": p,
                },
            )
            nodes[p]["accessCount"] += 1
        pl = list(paths)
        for i, a in enumerate(pl):
            for b in pl[i + 1 :]:
                if a != b:
                    key = (min(a, b), max(a, b))
                    if key not in edges:
                        edges[key] = {
                            "source": key[0],
                            "target": key[1],
                            "weight": 0,
                            "sessionType": session_type,
                            "sessions": [],
                        }
                    edges[key]["weight"] += 1
                    if session_id not in edges[key]["sessions"]:
                        edges[key]["sessions"].append(session_id)

    # Daily logs
    daily_dir = state_dir / "daily"
    if daily_dir.exists():
        for f in daily_dir.glob("*.md"):
            try:
                text = f.read_text(encoding="utf-8", errors="replace")
                paths = _extract_md_paths(text)
                session_id = f.stem
                add_session(session_id, paths, text)
            except Exception:
                pass

    # Handoff latest
    handoff = state_dir / "handoff_latest.md"
    if handoff.exists():
        try:
            text = handoff.read_text(encoding="utf-8", errors="replace")
            paths = _extract_md_paths(text)
            for m in re.finditer(r"^##\s*Paths\s*/\s*artifacts\s*$([\s\S]*?)(?=^##\s|\Z)", text, re.MULTILINE | re.IGNORECASE):
                block = m.group(1)
                for line in block.splitlines():
                    line = line.strip()
                    if line.startswith("-") and ".md" in line:
                        for m2 in re.finditer(r"[\w./\-\\]+\\.md", line):
                            paths.add(m2.group(0))
            add_session("handoff_latest", paths, text)
        except Exception:
            pass

    # Handoff archive
    archive_dir = state_dir / "handoff_archive"
    if archive_dir.exists():
        for f in archive_dir.glob("*.md"):
            try:
                text = f.read_text(encoding="utf-8", errors="replace")
                paths = _extract_md_paths(text)
                for m in re.finditer(r"^##\s*Paths\s*/\s*artifacts\s*$([\s\S]*?)(?=^##\s|\Z)", text, re.MULTILINE | re.IGNORECASE):
                    block = m.group(1)
                    for line in block.splitlines():
                        if ".md" in line:
                            for m2 in re.finditer(r"[\w./\-\\]+\\.md", line):
                                paths.add(m2.group(0))
                session_id = f.stem
                add_session(session_id, paths, text)
            except Exception:
                pass

    # decision-log
    decision = state_dir / "decision-log.md"
    if decision.exists():
        try:
            text = decision.read_text(encoding="utf-8", errors="replace")
            paths = _extract_md_paths(text)
            add_session("decision-log", paths, text)
        except Exception:
            pass

    graph = {
        "nodes": list(nodes.values()),
        "edges": list(edges.values()),
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "sessionCount": session_count,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(graph, indent=2), encoding="utf-8")
    return graph


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    root = script_dir.parent  # Harness: scripts/ at repo root
    env_state = os.environ.get("CURSOR_STATE_DIR", "").strip()
    state_dir = Path(env_state) if env_state else _find_state_dir(root)
    out_env = os.environ.get("BRAIN_MAP_OUTPUT", "")
    output_path = Path(out_env) if out_env else (state_dir / "brain-map-graph.json")
    build_graph(state_dir, output_path, root)
    print(f"Wrote {output_path.resolve()}")


if __name__ == "__main__":
    main()
