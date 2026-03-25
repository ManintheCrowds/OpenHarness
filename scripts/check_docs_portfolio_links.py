# PURPOSE: Verify relative markdown links from openharness/docs to sibling portfolio-harness paths exist on disk.
# Also ensures resolved paths stay under the workspace parent (repo root parent) to limit ../ escape.
# DEPENDENCIES: stdlib only; run from repo root: python scripts/check_docs_portfolio_links.py

from __future__ import annotations

import re
import sys
from pathlib import Path


def _repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def _is_under(child: Path, parent: Path) -> bool:
    """True if child resolves under parent (Python 3.9+ compatible)."""
    try:
        child.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def _extract_md_links(text: str) -> list[str]:
    # [label](url) — capture url without parens in url
    return re.findall(r"\[[^\]]*\]\(([^)]+)\)", text)


def main() -> int:
    root = _repo_root()
    docs = root / "docs"
    if not docs.is_dir():
        print(f"ERROR: {docs} not found", file=sys.stderr)
        return 2

    md_files = sorted(docs.rglob("*.md"))
    failures: list[tuple[str, str, str]] = []
    checked = 0

    for md_path in md_files:
        text = md_path.read_text(encoding="utf-8")
        base = md_path.parent
        for raw in _extract_md_links(text):
            url = raw.strip()
            if url.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if "portfolio-harness" not in url:
                continue
            # strip fragment
            path_part = url.split("#", 1)[0]
            if not path_part:
                continue
            target = (base / path_part).resolve()
            checked += 1
            # Containment: resolved path must stay under the workspace parent (sibling repos),
            # not escape to arbitrary filesystem locations via ../ chains.
            workspace_parent = root.parent.resolve()
            if not _is_under(target, workspace_parent):
                failures.append(
                    (
                        str(md_path.relative_to(root)),
                        url,
                        f"{target} (resolves outside workspace {workspace_parent})",
                    )
                )
                continue
            if not target.is_file():
                failures.append((str(md_path.relative_to(root)), url, str(target)))

    print(f"Checked {checked} portfolio-harness relative file links under docs/")
    if failures:
        print("FAILURES:", file=sys.stderr)
        for src, url, resolved in failures:
            print(f"  {src}: {url} -> {resolved}", file=sys.stderr)
        return 1
    print("OK: all portfolio-harness file links resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
