# Canonical agent bundle (OpenHarness)

**Verify-not-trust:** This repo is the **mechanical source of truth** for listed commands, skills, contracts, and portable docs. Consumers (e.g. portfolio-harness) may submodule this repo and **sync copies** into their `.cursor/` tree; integrity is checked with hashes, not README trust.

## What is bundled

| Path | Role |
|------|------|
| `.cursor/commands/architect.md` | Tech-lead / architect slash command |
| `.cursor/commands/agent-native-audit.md` | Agent-native parity audit command |
| `.cursor/skills/tech-lead/SKILL.md` | Canonical tech-lead skill |
| `.cursor/skills/secure-contain-protect/SKILL.md` | SCP workflow (MCP contract separate) |
| `.cursor/skills/refactor-reuse/SKILL.md` | Redundancy scan before new code |
| `.cursor/skills/agent-native-architecture/` | Vendored skill (MIT) — see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) |
| `.cursor/docs/NOGIC_WORKFLOW.md` | Nogic policy |
| `docs/contracts/scp_mcp_v1.md` | **SCP MCP public contract v1** |
| `docs/AGENT_NATIVE_CHECKLIST.md` | Portable **normative** agent-native checklist (SSOT). Sibling **MiscRepos** keeps [`.cursor/docs/AGENT_NATIVE_CHECKLIST.md`](../../MiscRepos/.cursor/docs/AGENT_NATIVE_CHECKLIST.md) as entry **stub** + [`AGENT_NATIVE_CHECKLIST_MISCOPS.md`](../../MiscRepos/.cursor/docs/AGENT_NATIVE_CHECKLIST_MISCOPS.md) addendum—do not treat the stub as the full checklist body. |
| `docs/CANONICAL_AGENT_BUNDLE.md`, `docs/VERIFY_NOT_TRUST.md`, `docs/MCP_TRANSPARENCY.md`, `docs/MCP_PRIVATE_HOST.md`, `docs/SCP_SERVER_RELEASES.md`, `docs/THIRD_PARTY_NOTICES.md` | Transparency / verify docs |
| `scripts/update_canonical_bundle_hashes.ps1`, `scripts/verify_canonical_bundle.ps1` | Manifest generators and verifier |
| `docs/canonical-bundle.sha256` | Expected SHA-256 per bundled path (regenerate after edits) |

## Verification

1. From repo root: `.\scripts\verify_canonical_bundle.ps1`  
   - Exits `0` if every file in `docs/canonical-bundle.sha256` matches on-disk SHA-256.  
   - Exits non-zero on mismatch or missing file.

2. After **intentionally** changing any bundled file, refresh hashes:  
   `.\scripts\update_canonical_bundle_hashes.ps1`  
   Then commit `docs/canonical-bundle.sha256` (and this doc if the table changed).

## SCP contract hash (releases)

Private SCP server releases should record **CONTRACT_HASH** = SHA-256 of `docs/contracts/scp_mcp_v1.md`. Public log (no server source): [SCP_SERVER_RELEASES.md](SCP_SERVER_RELEASES.md).

## Submodule consumers

Pin `vendor/openharness` (or equivalent) to a **commit SHA**. Run your sync script, then optionally run this repo’s `verify_canonical_bundle.ps1` against **synced paths** or re-run verify inside the submodule checkout.
