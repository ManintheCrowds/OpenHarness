# Agent-native checklist

When adding UI features or MCP tools, verify **action parity**: whatever a human can do in the product surface, an agent can achieve via tools (or composed primitives).

Use this in PR descriptions or run manually. Link your repo’s **capability map** (e.g. `MCP_CAPABILITY_MAP.md`) and **GUI action map** if you maintain them.

## When adding UI or MCP tools

- [ ] Every new UI action has a corresponding agent tool (or documented primitive composition)
- [ ] Capability / MCP map updated for the server or harness section
- [ ] Skill routing updated if new tools change agent workflows
- [ ] Smoke-tested with a natural-language agent request

## When adding harness scripts

- [ ] Script listed in your command README or harness capability table
- [ ] Agent can invoke via documented path (MCP, `run_terminal_cmd`, etc.)

## When adding MCP tools

- [ ] CRUD completeness where applicable: Create, Read, Update, Delete per entity
- [ ] Prefer **primitives** over fixed workflows unless the workflow is explicitly a product primitive
- [ ] Add `list_*` or `discover_*` for dynamic APIs when needed
- [ ] Tool outputs are rich enough for the agent to verify success

## Parity test

For each skill or MCP server: *Can the agent achieve everything a human can in this domain?*

For GUI surfaces: *Can the agent navigate, act, and capture evidence (snapshot/screenshot) where required?*

## Reviewer

For substantive UI or MCP additions, run a dedicated **agent-native** or parity review before merge. Load [.cursor/skills/agent-native-architecture/SKILL.md](../.cursor/skills/agent-native-architecture/SKILL.md) for principles and patterns.
