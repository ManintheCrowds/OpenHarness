# Harness ↔ OpenGrimoire audit alignment (Part B)

**Purpose:** One row per **Part B** agent-native dimension from the OpenGrimoire audit (OpenHarness bundle), mapping **what we improve or maintain here** to concrete paths—without an API. Keeps backlog and audit language aligned when you work in this repo.

**Normative external audit (example):** OpenGrimoire `docs/audit/` (e.g. `agent_native_opengrimoire_2026-03-24.md`), section **Part B — OpenHarness**.

| # | Part B principle | What we improve / maintain in OpenHarness | Primary paths |
|---|------------------|---------------------------------------------|---------------|
| 1 | Action parity | Same scripts documented for humans and agents; index stays current | [CHEATSHEET.md](CHEATSHEET.md) (Agent invocation index), [capabilities.harness.yaml](../capabilities.harness.yaml), `scripts/`, [AGENT_NATIVE_CHECKLIST.md](AGENT_NATIVE_CHECKLIST.md) |
| 2 | Tools as primitives | Skills as composable primitives (`SKILL.md`) | `.cursor/skills/`, [.cursor/skills/README.md](../.cursor/skills/README.md) |
| 3 | Context injection | Handoff and state shape; flow documentation | [HANDOFF_FLOW.md](HANDOFF_FLOW.md), `state/`, portable `.cursor/state/` (see `state/README.md`) |
| 4 | Shared workspace | Files on disk for human + agent; boundary docs | [PUBLIC_AND_PRIVATE_HARNESS.md](PUBLIC_AND_PRIVATE_HARNESS.md), repo root layout |
| 5 | CRUD completeness | **N/A** (no entity API)—honest; state is file CRUD via editor | `state/README.md` |
| 6 | UI integration | **N/A** (no product UI in harness) | — |
| 7 | Capability discovery | Entry points: README, skills index, checklist, YAML manifest | [README.md](../README.md), [.cursor/skills/README.md](../.cursor/skills/README.md), [AGENT_NATIVE_CHECKLIST.md](AGENT_NATIVE_CHECKLIST.md), [capabilities.harness.yaml](../capabilities.harness.yaml) |
| 8 | Prompt-native | Continue prompt + handoff as prompt-forward workflows | [HANDOFF_FLOW.md](HANDOFF_FLOW.md), `state/continue_prompt.txt`, `scripts/copy_continue_prompt.*` |

**Portfolio (MiscRepos):** [`.cursor/docs/AGENT_NATIVE_CHECKLIST.md`](../../MiscRepos/.cursor/docs/AGENT_NATIVE_CHECKLIST.md) is an entry **stub** only (links to this repo’s normative [AGENT_NATIVE_CHECKLIST.md](AGENT_NATIVE_CHECKLIST.md) + [`AGENT_NATIVE_CHECKLIST_MISCOPS.md`](../../MiscRepos/.cursor/docs/AGENT_NATIVE_CHECKLIST_MISCOPS.md)). Do not treat the stub as the full checklist body.

**Related:** Structured manifest [capabilities.harness.yaml](../capabilities.harness.yaml); `python scripts/verify_script_index.py` (YAML ↔ disk ↔ CHEATSHEET backticks); `python scripts/verify_skills_readme.py` (README vs `SKILL.md` descriptions).

## Backlog (agent-native audit follow-up)

**Thin MCP over harness scripts (parity, no new business logic):** Optional future work — an MCP server that **lists** and **runs** only allowlisted scripts from `capabilities.harness.yaml` / [CHEATSHEET](CHEATSHEET.md), subprocess from repo root, no arbitrary shell. Would complement terminal parity for agents that only expose MCP. **Not implemented** here; tracked in [BACKLOG.md](BACKLOG.md). Security and allowlisting would be documented alongside [MCP_PRIVATE_HOST.md](MCP_PRIVATE_HOST.md).
