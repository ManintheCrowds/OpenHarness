# PURPOSE: Thin wrapper delegating to SCP package.
# DEPENDENCIES: pip install scp-mcp
# Use in pre-commit to scan handoff/state files before commit.

"""
Scan text for prompt-injection patterns and hidden Unicode. Delegates to scp package.

Usage:
  python sanitize_input.py <file_path>           # Scan file(s)
  python sanitize_input.py -                      # Scan stdin
  python sanitize_input.py --check "text"         # Scan inline text
  python sanitize_input.py --classify "text"      # Output JSON {tier, findings, risk_score}

Exit: 0 if clean (or hostile_ux), 1 if injection/reversal. Use in CI or before writing handoff/state.
"""

import json
import sys
from pathlib import Path

from scp.scp_utils import run_pipeline


def _run_check(content: str, sink: str = "state") -> tuple[bool, dict]:
    """Run pipeline; return (blocked, report)."""
    result = run_pipeline(content, sink=sink)
    blocked = result.get("blocked", False)
    report = result.get("report", {})
    return blocked, report


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__, file=sys.stderr)
        return 2

    if args[0] == "--classify":
        if len(args) < 2:
            print("Usage: sanitize_input.py --classify \"text\"", file=sys.stderr)
            return 2
        from scp.sanitize_input import classify
        result = classify(args[1])
        print(json.dumps(result))
        return 0 if result.get("tier") in ("clean", "hostile_ux") else 1

    if args[0] == "--check":
        if len(args) < 2:
            print("Usage: sanitize_input.py --check \"text\"", file=sys.stderr)
            return 2
        blocked, report = _run_check(args[1])
        if blocked:
            print(f"FINDINGS: <inline> tier={report.get('tier', 'injection')}", file=sys.stderr)
            return 1
        print("OK: <inline> - no injection patterns or hidden Unicode")
        return 0

    if args[0] == "-":
        content = sys.stdin.read()
        blocked, report = _run_check(content)
        if blocked:
            print(f"FINDINGS: <stdin> tier={report.get('tier', 'injection')}", file=sys.stderr)
            return 1
        print("OK: <stdin> - no injection patterns or hidden Unicode")
        return 0

    # File path(s) - pre-commit passes multiple
    failed = False
    for path_arg in args:
        path = Path(path_arg)
        if not path.exists():
            print(f"File not found: {path}", file=sys.stderr)
            failed = True
            continue
        content = path.read_text(encoding="utf-8", errors="replace")
        blocked, report = _run_check(content)
        if blocked:
            failed = True
            print(f"FINDINGS: {path} tier={report.get('tier', 'injection')}", file=sys.stderr)
        else:
            print(f"OK: {path} - no injection patterns or hidden Unicode")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
