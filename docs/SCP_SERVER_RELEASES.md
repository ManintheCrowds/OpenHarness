# SCP server releases (contract hash log)

Public log of **SCP MCP server** releases vs **OpenHarness contract** revision. Server **source** stays private; this file only records version ↔ **CONTRACT_HASH** (SHA-256 of `docs/contracts/scp_mcp_v1.md` at time of release).

| Server version / tag | CONTRACT_HASH (sha256 of scp_mcp_v1.md) | Notes |
|------------------------|------------------------------------------|--------|
| scp-mcp 0.1.0 (reference) | `226f19b3cf237a2d7fe6793d4f7f4be5bee5631693f489662c48d126b4094f42` | OpenHarness contract file as of bundle publish; re-hash after any edit to `scp_mcp_v1.md` |

**Compute CONTRACT_HASH (PowerShell, from OpenHarness root):**

```powershell
(Get-FileHash -Algorithm SHA256 -Path docs/contracts/scp_mcp_v1.md).Hash.ToLowerInvariant()
```

After updating `docs/contracts/scp_mcp_v1.sha256`, run `python scripts/verify_contract_hash.py` (must exit `0`).

When you bump the contract file, increment its version section and regenerate hashes; server releases should target an explicit contract revision.
