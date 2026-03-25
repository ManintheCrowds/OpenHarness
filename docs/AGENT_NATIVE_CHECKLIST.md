# Agent-native checklist

When adding UI features or MCP tools, verify **action parity**: whatever a human can do in the product surface, an agent can achieve via tools (or composed primitives).

Use this in PR descriptions or run manually. Link your repo’s **capability map** (e.g. `MCP_CAPABILITY_MAP.md`) and **GUI action map** if you maintain them. **Harness:** [capabilities.harness.yaml](../capabilities.harness.yaml) lists checklist sections (anchors) and script globs; [HARNESS_AUDIT_ALIGNMENT.md](HARNESS_AUDIT_ALIGNMENT.md) maps OpenAtlas audit Part B dimensions to paths in this repo.

## When adding UI or MCP tools

- [ ] Every new UI action has a corresponding agent tool (or documented primitive composition)
- [ ] Capability / MCP map updated for the server or harness section
- [ ] Skill routing updated if new tools change agent workflows
- [ ] Smoke-tested with a natural-language agent request

## When adding harness scripts

- [ ] Script listed in your command README or harness capability table
- [ ] Agent can invoke via documented path (MCP, `run_terminal_cmd`, etc.)
- [ ] **Order of operations:** Update [CHEATSHEET](CHEATSHEET.md) **Agent invocation index** first, then [capabilities.harness.yaml](../capabilities.harness.yaml) `harness_capability.scripts`, then run `python scripts/verify_script_index.py` in the same PR
- [ ] **Harness verification:** Basename in [CHEATSHEET](CHEATSHEET.md) **Agent invocation index** (inline code / backticks) and in [capabilities.harness.yaml](../capabilities.harness.yaml) `harness_capability.scripts` (must match disk); run `python scripts/verify_script_index.py` locally; add or adjust the pre-commit hook in `.pre-commit-config.yaml` if your fork uses it

## When adding or renaming skills

- [ ] [.cursor/skills/README.md](../.cursor/skills/README.md) row matches `description:` in that folder’s `SKILL.md` front matter; run `python scripts/verify_skills_readme.py`
- [ ] After **large** skill additions or restructures, re-run an agent-native pass (e.g. [.cursor/commands/agent-native-audit.md](../.cursor/commands/agent-native-audit.md)) and confirm `verify_skills_readme.py` still passes

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
