#!/usr/bin/env python3
"""Validate state/async_tasks.yaml — async task ledger schema for multi-session work.

See docs/ASYNC_HITL_SCOPE.md for semantics.
"""
from __future__ import annotations

import re
import sys
from datetime import datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Install PyYAML: pip install PyYAML", file=sys.stderr)
    raise SystemExit(2) from None

ALLOWED_VERSIONS = frozenset({1})
ALLOWED_STATUSES = frozenset(
    {
        "backlog",
        "claimed",
        "in_progress",
        "blocked_hitl",
        "done",
        "superseded",
    }
)
# task-YYYYMMDD-slug (slug: lowercase alphanum + hyphens)
TASK_ID_RE = re.compile(r"^task-\d{8}-[a-z0-9]+(?:-[a-z0-9]+)*$")


def _parse_iso8601_utc(s: object) -> bool:
    if not isinstance(s, str) or not s.strip():
        return False
    raw = s.strip().replace("Z", "+00:00")
    try:
        datetime.fromisoformat(raw)
    except ValueError:
        return False
    return True


def _err(msg: str) -> None:
    print(msg, file=sys.stderr)


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    path = root / "state" / "async_tasks.yaml"
    if not path.is_file():
        _err(f"Missing {path.relative_to(root)}")
        return 1

    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        _err(f"YAML parse error: {e}")
        return 1

    if not isinstance(data, dict):
        _err("Root must be a mapping with version and tasks")
        return 1

    version = data.get("version")
    if version not in ALLOWED_VERSIONS:
        _err(f"version must be one of {sorted(ALLOWED_VERSIONS)}, got {version!r}")
        return 1

    tasks = data.get("tasks")
    if not isinstance(tasks, list):
        _err("tasks must be a list")
        return 1

    seen_ids: set[str] = set()
    for i, task in enumerate(tasks):
        prefix = f"tasks[{i}]"
        if not isinstance(task, dict):
            _err(f"{prefix}: each task must be a mapping")
            return 1

        tid = task.get("id")
        if not isinstance(tid, str) or not tid.strip():
            _err(f"{prefix}: id must be a non-empty string")
            return 1
        tid = tid.strip()
        if not TASK_ID_RE.match(tid):
            _err(
                f"{prefix}: id must match task-YYYYMMDD-<slug> "
                f"(lowercase slug), got {tid!r}"
            )
            return 1
        if tid in seen_ids:
            _err(f"Duplicate task id: {tid!r}")
            return 1
        seen_ids.add(tid)

        status = task.get("status")
        if status not in ALLOWED_STATUSES:
            _err(
                f"{prefix} ({tid}): status must be one of "
                f"{sorted(ALLOWED_STATUSES)}, got {status!r}"
            )
            return 1

        owner = task.get("owner")
        if not isinstance(owner, str) or not owner.strip():
            _err(f"{prefix} ({tid}): owner must be a non-empty string")
            return 1

        updated = task.get("updated_at")
        if not _parse_iso8601_utc(updated):
            _err(
                f"{prefix} ({tid}): updated_at must be ISO 8601 "
                f"(e.g. 2026-03-26T12:00:00Z), got {updated!r}"
            )
            return 1

        paths = task.get("paths")
        if not isinstance(paths, list) or not all(
            isinstance(p, str) for p in paths
        ):
            _err(f"{prefix} ({tid}): paths must be a list of strings")
            return 1

        if "notes" in task and task["notes"] is not None:
            if not isinstance(task["notes"], str):
                _err(f"{prefix} ({tid}): notes must be a string if present")
                return 1

        extra = set(task.keys()) - {
            "id",
            "status",
            "owner",
            "updated_at",
            "paths",
            "notes",
        }
        if extra:
            _err(f"{prefix} ({tid}): unknown keys: {sorted(extra)}")
            return 1

    print(f"OK: {path.relative_to(root)} ({len(tasks)} task(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
