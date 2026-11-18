# PURPOSE: Pre-commit entry for mask-check.
# Fail closed unless installed scp-mcp is the pinned commit, then delegate.
# Does not vendor the SCP masker.

"""Run SCP mask_secrets --check after verifying the pinned scp-mcp commit."""

from __future__ import annotations

import json
import sys
from importlib.metadata import PackageNotFoundError, distribution
from pathlib import Path

from scp.mask_secrets import main as mask_main

# TODO: repin to a main SHA once https://github.com/ManintheCrowds/SCP/pull/97 merges.
PIN = "6f8bcbdcb2c602b64f0d63b14a42897f8cf92d5a"


def installed_commit() -> str:
    """Return the VCS commit of installed scp-mcp, or empty when unknown."""
    try:
        dist = distribution("scp-mcp")
    except PackageNotFoundError:
        return ""
    metadata = None
    for file in dist.files or []:
        if file.name == "METADATA":
            metadata = Path(str(file.locate()))
            break
    if metadata is None:
        return ""
    direct = metadata.parent / "direct_url.json"
    if not direct.is_file():
        return ""
    try:
        info = json.loads(direct.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return ""
    vcs = info.get("vcs_info")
    if not isinstance(vcs, dict):
        return ""
    commit = vcs.get("commit_id")
    if not isinstance(commit, str):
        return ""
    return commit


def pin_ok(commit: str, pin: str = PIN) -> bool:
    return bool(commit) and commit == pin


def main() -> int:
    if not pin_ok(installed_commit()):
        print("scp-mcp pin mismatch; refusing to scan", file=sys.stderr)
        return 1
    return mask_main()


if __name__ == "__main__":
    sys.exit(main())
