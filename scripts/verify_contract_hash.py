#!/usr/bin/env python3
"""Verify SHA-256 of docs/contracts/scp_mcp_v1.md matches the committed fingerprint.

After editing the contract, update docs/contracts/scp_mcp_v1.sha256 (one hex line) and
docs/SCP_SERVER_RELEASES.md. Same bytes as VERIFY_NOT_TRUST.md (file hash, not UTF-8 normalize).
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    contract = root / "docs" / "contracts" / "scp_mcp_v1.md"
    expected_file = root / "docs" / "contracts" / "scp_mcp_v1.sha256"
    if not contract.is_file():
        print("Missing docs/contracts/scp_mcp_v1.md", file=sys.stderr)
        return 1
    if not expected_file.is_file():
        print("Missing docs/contracts/scp_mcp_v1.sha256", file=sys.stderr)
        return 1
    digest = hashlib.sha256(contract.read_bytes()).hexdigest()
    line = expected_file.read_text(encoding="utf-8").strip()
    expected = line.split()[0] if line else ""
    if digest.lower() != expected.lower():
        print(
            f"CONTRACT_HASH mismatch: computed {digest} != expected {expected}",
            file=sys.stderr,
        )
        return 1
    print("OK: scp_mcp_v1.md matches scp_mcp_v1.sha256")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
