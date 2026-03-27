# Verify, not trust

Operating rules for OpenHarness and consumers.

## Public tree (OpenHarness)

1. **Submodule or checkout** pinned to a **git commit SHA** (not only a branch name).
2. Run `.\scripts\verify_canonical_bundle.ps1` — must exit `0`. This checks `docs/canonical-bundle.sha256` against on-disk files.
3. After editing any bundled file, run `.\scripts\update_canonical_bundle_hashes.ps1` and commit the updated manifest in the **same** PR.

## Private MCP servers

1. Server **CI** runs **contract conformance** tests against the same `scp_mcp_v1.md` (or your versioned contract) pinned in the release.
2. Each release records **CONTRACT_HASH** = SHA-256 of the contract file (UTF-8).
3. Optional: publish a one-line row in [SCP_SERVER_RELEASES.md](SCP_SERVER_RELEASES.md) mapping server version to contract hash—**no** server source required.

## OpenHarness contract file (local check)

From repo root, `python scripts/verify_contract_hash.py` must exit `0`. It compares the SHA-256 of `docs/contracts/scp_mcp_v1.md` to the committed fingerprint in `docs/contracts/scp_mcp_v1.sha256`. After editing the contract, update both the `.sha256` file and [SCP_SERVER_RELEASES.md](SCP_SERVER_RELEASES.md).

## What not to do

- Do not treat skill prose alone as a security guarantee—**tool behavior** must match the **contract** for the **pinned** server version.
- Do not commit API keys, tokens, or internal URLs into OpenHarness.

## Related

- [CANONICAL_AGENT_BUNDLE.md](CANONICAL_AGENT_BUNDLE.md)
- [MCP_TRANSPARENCY.md](MCP_TRANSPARENCY.md)
- [MCP_PRIVATE_HOST.md](MCP_PRIVATE_HOST.md)
- [GOVERNANCE.md](GOVERNANCE.md)
