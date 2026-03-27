#!/usr/bin/env python3
"""Emit harness capability manifest as JSON (scripts, checklist pointers, canonical paths).

Reads capabilities.harness.yaml. Use for agent discovery without parsing CHEATSHEET prose.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Install PyYAML: pip install PyYAML", file=sys.stderr)
    raise SystemExit(2) from None


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    path = root / "capabilities.harness.yaml"
    if not path.is_file():
        print("Missing capabilities.harness.yaml", file=sys.stderr)
        return 1
    with path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    hc = data.get("harness_capability", {})
    out = {
        "version": hc.get("version"),
        "scripts": hc.get("scripts", []),
        "scripts_other": hc.get("scripts_other", []),
        "canonical": hc.get("canonical", {}),
        "checklist": hc.get("checklist", {}),
        "scripts_globs": hc.get("scripts_globs", []),
        "skills_globs": hc.get("skills_globs", []),
    }
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
