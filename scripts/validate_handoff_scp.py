# PURPOSE: SCP validation for handoff content before commit.
# Run as pre-commit hook when handoff_latest.md is staged; blocks commit if tier=injection.
#
# Usage:
#   python validate_handoff_scp.py [path]
#   If path omitted, uses state/handoff_latest.md relative to script.
#
# Dependencies: pip install scp (or add scp package to path)

from __future__ import annotations

import os
import sys
from pathlib import Path

_here = Path(__file__).resolve().parent
_state = _here.parent / "state"
DEFAULT_PATH = _state / "handoff_latest.md"

# Allow override for integration (e.g. .cursor/state/handoff_latest.md)
STATE_DIR = os.environ.get("HARNESS_STATE_DIR")
if STATE_DIR:
    DEFAULT_PATH = Path(STATE_DIR) / "handoff_latest.md"


def main() -> int:
    try:
        from scp.scp_utils import run_pipeline
    except ImportError:
        print(
            "SCP package not found. Install: pip install scp",
            file=sys.stderr,
        )
        return 2

    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
    if not path.exists():
        return 0  # No handoff to validate
    content = path.read_text(encoding="utf-8", errors="replace")
    result = run_pipeline(content, sink="handoff")
    if result.get("blocked"):
        report = result.get("report", {})
        tier = report.get("tier", "injection")
        print(
            f"SCP BLOCK: Handoff content detected as tier={tier}. Do not commit.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
