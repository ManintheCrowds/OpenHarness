#!/usr/bin/env python3
"""Harness script index integrity.

1. ``capabilities.harness.yaml`` ``harness_capability.scripts`` must match the set of
   ``scripts/*.py|ps1|sh|cmd`` basenames on disk (set equality). Parsed with PyYAML
   (``pip install PyYAML``).
2. Every such basename must appear in ``docs/CHEATSHEET.md`` as markdown inline code
   (the substring backtick + basename + backtick) so names are not matched inside unrelated prose.

**YAML shape (required for ``harness_capability.scripts``):**

- Top-level key ``harness_capability:`` (no leading spaces).
- Under it, a key ``scripts:`` at **exactly two spaces** indent from line start.
- List items at **four spaces** + ``- `` + basename, e.g. ``    - build_brain_map.py``.
- Do not put ``scripts:`` on the same line as a comment; use a line that is only ``  scripts:``.
- The list ends at the next sibling key under ``harness_capability`` at two-space indent
  (e.g. ``  scripts_other:``).

``scripts_other`` files (e.g. ``.html``, ``.json``) are not listed in ``scripts[]`` and are
not part of the disk set this script checks.
"""
from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Install PyYAML: pip install PyYAML", file=sys.stderr)
    raise SystemExit(2) from None

SCRIPT_EXTS = (".py", ".ps1", ".sh", ".cmd")


def disk_script_basenames(scripts_dir: Path) -> set[str]:
    out: set[str] = set()
    if not scripts_dir.is_dir():
        return out
    for path in scripts_dir.iterdir():
        if not path.is_file():
            continue
        if path.suffix.lower() not in SCRIPT_EXTS:
            continue
        out.add(path.name)
    return out


def load_manifest_scripts(manifest_path: Path) -> list[str]:
    raw = manifest_path.read_text(encoding="utf-8")
    data = yaml.safe_load(raw)
    if not isinstance(data, dict):
        raise ValueError(f"{manifest_path}: root must be a mapping")
    hc = data.get("harness_capability")
    if not isinstance(hc, dict):
        raise ValueError(f"{manifest_path}: missing harness_capability mapping")
    scripts = hc.get("scripts")
    if not isinstance(scripts, list):
        raise ValueError(f"{manifest_path}: harness_capability.scripts must be a list")
    out: list[str] = []
    for i, item in enumerate(scripts):
        if not isinstance(item, str):
            raise ValueError(
                f"{manifest_path}: harness_capability.scripts[{i}] must be a string"
            )
        out.append(item)
    return out


def main() -> int:
    from collections import Counter

    root = Path(__file__).resolve().parent.parent
    manifest = root / "capabilities.harness.yaml"
    cheatsheet = root / "docs" / "CHEATSHEET.md"
    scripts_dir = root / "scripts"

    if not manifest.is_file():
        print(f"Missing {manifest}", file=sys.stderr)
        return 2
    if not cheatsheet.is_file():
        print(f"Missing {cheatsheet}", file=sys.stderr)
        return 2

    try:
        yaml_list = load_manifest_scripts(manifest)
    except ValueError as e:
        print(str(e), file=sys.stderr)
        return 2

    dup_counts = Counter(yaml_list)
    dupes = sorted([k for k, v in dup_counts.items() if v > 1])
    if dupes:
        print(f"{manifest}: duplicate entries in scripts: {dupes}", file=sys.stderr)
        return 1

    yaml_set = set(yaml_list)
    disk_set = disk_script_basenames(scripts_dir)

    if disk_set != yaml_set:
        only_disk = sorted(disk_set - yaml_set)
        only_yaml = sorted(yaml_set - disk_set)
        print(
            f"{manifest} harness_capability.scripts must match script files on disk "
            f"({', '.join(SCRIPT_EXTS)}):",
            file=sys.stderr,
        )
        if only_disk:
            print("  Only on disk (add to YAML or remove file):", file=sys.stderr)
            for x in only_disk:
                print(f"    {x}", file=sys.stderr)
        if only_yaml:
            print("  Only in YAML (remove from YAML or add file):", file=sys.stderr)
            for x in only_yaml:
                print(f"    {x}", file=sys.stderr)
        return 1

    text = cheatsheet.read_text(encoding="utf-8")
    missing: list[str] = []
    for name in sorted(disk_set):
        if f"`{name}`" not in text:
            missing.append(name)

    if missing:
        print(
            "CHEATSHEET.md must mention each script basename in backticks, e.g. "
            "`script_name.py` (Agent invocation index table):",
            file=sys.stderr,
        )
        for m in missing:
            print(f"  {m}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
