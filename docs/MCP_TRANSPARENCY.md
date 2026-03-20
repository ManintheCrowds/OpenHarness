# MCP transparency model

OpenHarness separates **what agents are told to do** from **where tools run**.

| Layer | Location | Audience | Verified by |
|-------|-----------|----------|-------------|
| Skills / commands | OpenHarness `.cursor/` | Public | `scripts/verify_canonical_bundle.ps1` + `docs/canonical-bundle.sha256` |
| MCP **contracts** | `docs/contracts/` (e.g. `scp_mcp_v1.md`) | Public | Hash in manifest; private server CI against same file |
| MCP **servers** | Private repo, local path, or org package | Operator | Submodule pin, CI, staging smoke |
| Workspace `mcp.json` | Per-machine / per-repo (often gitignored or templated) | Operator | Manual + optional secret scan |

## Contracted vs optional MCPs

- **Contracted:** Documented in `docs/contracts/`; agent skills reference **tool names** and behavior. Example: SCP (`scp_mcp_v1`).
- **Optional / local:** Browser, Context7, org-specific servers—listed in **your** project’s capability map (may live only in a private harness). OpenHarness does not need to duplicate every third-party map.

## Why

Communities that **verify, not trust** need **bytes and hashes** for prompts and contracts, not “read the README.” Server source can remain private while the contract stays public and testable.

See also: [VERIFY_NOT_TRUST.md](VERIFY_NOT_TRUST.md), [PUBLIC_AND_PRIVATE_HARNESS.md](PUBLIC_AND_PRIVATE_HARNESS.md).
