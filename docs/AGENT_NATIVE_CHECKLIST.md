# Agent-native checklist

**Canonical (SSOT):** This file is the **single normative** agent-native checklist for the OpenHarness bundle. **Do not** duplicate the sections below in sibling repos—extend with a portfolio **addendum** instead. When **MiscRepos** (or another portfolio root) is cloned next to OpenHarness, apply **[`MiscRepos/.cursor/docs/AGENT_NATIVE_CHECKLIST_MISCOPS.md`](../../MiscRepos/.cursor/docs/AGENT_NATIVE_CHECKLIST_MISCOPS.md)** for baseline audits, GUI wave ritual, MCP-specific tables, and E2E/GUI map hooks.

When adding UI features or MCP tools, verify **action parity**: whatever a human can do in the product surface, an agent can achieve via tools (or composed primitives).

Use this in PR descriptions or run manually. Link your repo’s **capability map** (e.g. `MCP_CAPABILITY_MAP.md`). **GUI:** If the product has a **browser or native GUI**, maintain a **GUI action map** (or equivalent) and evidence rules—or document a **waiver in the PR** (owner, date, reason: e.g. headless-only library). **Harness:** [capabilities.harness.yaml](../capabilities.harness.yaml) lists checklist sections (anchors) and script globs; [HARNESS_AUDIT_ALIGNMENT.md](HARNESS_AUDIT_ALIGNMENT.md) maps OpenGrimoire audit Part B dimensions to paths in this repo.

## Minimum bundle (audit honesty)

A **full** harness audit (scripts ↔ YAML ↔ CHEATSHEET parity) requires this repo to include at least:

- This checklist, [.cursor/skills/agent-native-architecture/SKILL.md](../.cursor/skills/agent-native-architecture/SKILL.md), [CHEATSHEET.md](CHEATSHEET.md) **Agent invocation index**, [capabilities.harness.yaml](../capabilities.harness.yaml), and `python scripts/verify_script_index.py` (plus `verify_skills_readme.py` when skills change).

If you only copied markdown without the YAML and verifiers, treat agent-native review as **documentation-only** until the manifest and scripts exist on disk.

## When adding UI or MCP tools

- [ ] Every new UI action has a corresponding agent tool (or documented primitive composition)
- [ ] Capability / MCP map updated for the server or harness section
- [ ] Skill routing updated if new tools change agent workflows
- [ ] Smoke-tested with a natural-language agent request
- [ ] **Semantic outcome parity:** For each release area you touch, at least **one** natural-language agent request that proves an **end-to-end outcome** (not only that script names exist in an index). Log or paste evidence in the PR when practical.
- [ ] **GUI (required or waived):** If there is a GUI, link or update the **GUI action map** and capture rules (e.g. snapshot/screenshot/E2E on failure). If no GUI applies, state **waiver** in the PR description.

## When adding harness scripts

- [ ] Script listed in your command README or harness capability table
- [ ] Agent can invoke via documented path (MCP, `run_terminal_cmd`, etc.)
- [ ] **Order of operations:** Update [CHEATSHEET](CHEATSHEET.md) **Agent invocation index** first, then [capabilities.harness.yaml](../capabilities.harness.yaml) `harness_capability.scripts`, then run `python scripts/verify_script_index.py` in the same PR
- [ ] **Harness verification:** Basename in [CHEATSHEET](CHEATSHEET.md) **Agent invocation index** (inline code / backticks) and in [capabilities.harness.yaml](../capabilities.harness.yaml) `harness_capability.scripts` (must match disk); run `python scripts/verify_script_index.py` locally; add or adjust the pre-commit hook in `.pre-commit-config.yaml` if your fork uses it
- [ ] **Note:** Passing `verify_script_index.py` is **necessary, not sufficient** for semantic parity—combine with NL smoke above. Example prompts and CI scope: [CONTRIBUTING.md](../CONTRIBUTING.md) (**Semantic smoke**).

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

For GUI surfaces: *Can the agent navigate, act, and capture evidence (snapshot/screenshot) where required?* If your stack is HTTP-only, see sibling [OpenGrimoire `docs/ACTION_PARITY_FILE_INDEX.md`](../../OpenGrimoire/docs/ACTION_PARITY_FILE_INDEX.md) for REST/MCP parity pointers.

## Reviewer

For substantive UI or MCP additions, run a dedicated **agent-native** or parity review before merge. Load [.cursor/skills/agent-native-architecture/SKILL.md](../.cursor/skills/agent-native-architecture/SKILL.md) for principles and patterns.
