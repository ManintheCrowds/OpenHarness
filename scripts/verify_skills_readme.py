#!/usr/bin/env python3
"""Fail if .cursor/skills/README.md rows do not match each folder's SKILL.md description: front matter."""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Install PyYAML: pip install PyYAML", file=sys.stderr)
    raise SystemExit(2) from None


def _parse_front_matter(skill_path: Path) -> dict:
    text = skill_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    end = text.find("\n---\n", 3)
    if end == -1:
        return {}
    block = text[3:end]
    data = yaml.safe_load(block)
    return data if isinstance(data, dict) else {}


def _parse_readme_table(readme_path: Path) -> dict[str, str]:
    """Map folder name -> summary column from markdown table rows."""
    text = readme_path.read_text(encoding="utf-8")
    rows: dict[str, str] = {}
    # | `folder` | Summary text |
    row_re = re.compile(r"^\|\s*`([^`]+)`\s*\|\s*(.+?)\s*\|\s*$")
    for line in text.splitlines():
        m = row_re.match(line.strip())
        if m:
            folder, summary = m.group(1), m.group(2).strip()
            if folder != "Folder":  # skip header
                rows[folder] = summary
    return rows


def _norm(s: str) -> str:
    return " ".join(s.split())


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    skills_root = root / ".cursor" / "skills"
    readme = skills_root / "README.md"
    if not readme.is_file():
        print(f"Missing {readme}", file=sys.stderr)
        return 2

    table = _parse_readme_table(readme)
    errors: list[str] = []

    skill_dirs = sorted(
        p for p in skills_root.iterdir() if p.is_dir() and (p / "SKILL.md").is_file()
    )

    for folder in skill_dirs:
        name = folder.name
        fm = _parse_front_matter(folder / "SKILL.md")
        desc = fm.get("description")
        if not desc or not isinstance(desc, str):
            errors.append(f"{name}: SKILL.md front matter missing string description:")
            continue
        desc_n = _norm(desc)
        if name not in table:
            errors.append(f"{name}: no row in README.md for this folder")
            continue
        summary_n = _norm(table[name])
        if desc_n != summary_n:
            errors.append(
                f"{name}: README summary does not match SKILL.md description:\n"
                f"  README: {table[name]!r}\n"
                f"  SKILL:  {desc!r}"
            )

    for name in table:
        if name == "Folder":
            continue
        if not (skills_root / name / "SKILL.md").is_file():
            errors.append(f"README lists `{name}` but no .cursor/skills/{name}/SKILL.md")

    if errors:
        print(
            ".cursor/skills/README.md must match each SKILL.md description: (front matter)\n",
            file=sys.stderr,
        )
        for e in errors:
            print(e, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
