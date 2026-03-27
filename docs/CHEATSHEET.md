# Harness Cheat Sheet

One-page harness compression.

## Components

| Component | What it does | Portable? |
| --------- | ----------------------------------------------------- | --------- |
| Rules | Operating principles, tool limits, redundancy scanner | Yes (prose) |
| Skills | JIT-loaded per-task instructions (SKILL.md pattern) | Yes |
| state/ | handoff, decision-log, known-issues, preferences | Yes (schema) |
| Handoff | Archive → write Done/Next → continue prompt | Yes |
| MCP | Context7, browser, etc. | Platform-specific |
| Nogic | Graph / optional MCP for dependencies and coupling; pair with refactor-reuse | Policy: [.cursor/docs/NOGIC_WORKFLOW.md](../.cursor/docs/NOGIC_WORKFLOW.md) |

**Evals / external tools:** See [HARNESS_ARCHITECTURE.md](HARNESS_ARCHITECTURE.md#external-benchmarks-and-sims-implementation-side)—external sims and benchmark runners stay out of core; consume summaries + provenance in implementation repos.

**Maintenance (scripts index):** When you add, rename, or remove anything under `scripts/` that should be discoverable to agents, update the **Agent invocation index** table below and keep [capabilities.harness.yaml](../capabilities.harness.yaml) `harness_capability.scripts` in sync. `python scripts/verify_script_index.py` asserts **YAML `scripts[]` == on-disk script basenames** (PyYAML) and that each basename appears **in backticks** in this file (e.g. `` `build_brain_map.py` ``). **Last reviewed:** 2026-03-26.

### Adding a script (order of operations)

1. Add the file under `scripts/` (supported extensions: `.py`, `.ps1`, `.sh`, `.cmd`).
2. Add a row to the **Agent invocation index** table below (script name in backticks, purpose, typical invocation).
3. Add the basename to [capabilities.harness.yaml](../capabilities.harness.yaml) under `harness_capability.scripts` (sorted list; match existing style).
4. Run `python scripts/verify_script_index.py` — fix CHEATSHEET or YAML until it passes.
5. Commit; pre-commit runs the same check when `docs/CHEATSHEET.md`, `capabilities.harness.yaml`, or `scripts/**` change.

## Cursor slash commands vs agents

**Humans:** Run `/architect` or `/agent-native-audit` in Cursor. **Agents:** Open the same contract as markdown under [`.cursor/commands/`](../.cursor/commands/) (e.g. `architect.md`, `agent-native-audit.md`) and follow the steps—this is **action parity** with slash dispatch.

## Agent invocation index (scripts)

Use this table for **action parity** with humans (same script, agent via `run_terminal_cmd` or equivalent). See [AGENT_NATIVE_CHECKLIST.md](AGENT_NATIVE_CHECKLIST.md).

| Script | Purpose | Typical invocation |
| ------ | ------- | ------------------- |
| `copy_continue_prompt.ps1` / `copy_continue_prompt.sh` / `copy_continue_prompt.cmd` | Copy continue prompt to clipboard | `.\scripts\copy_continue_prompt.ps1` (Windows), `./scripts/copy_continue_prompt.sh`, or `scripts\copy_continue_prompt.cmd` |
| `validate_handoff_scp.py` | Validate `handoff_latest` against SCP rules | `python scripts/validate_handoff_scp.py` |
| `sanitize_input.py` | Sanitize handoff/state before commit | Usually via pre-commit; `python scripts/sanitize_input.py` |
| `build_brain_map.py` | Build brain-map JSON from cursor state | `python scripts/build_brain_map.py` (set `CURSOR_STATE_DIR` / `CURSOR_STATE_DIRS` as in README) |
| `verify_canonical_bundle.ps1` | Verify pinned bundle hashes | `.\scripts\verify_canonical_bundle.ps1` |
| `update_canonical_bundle_hashes.ps1` | Regenerate `docs/canonical-bundle.sha256` after bundle edits | `.\scripts\update_canonical_bundle_hashes.ps1` |
| `check_docs_portfolio_links.py` | Verify `docs/**/*.md` links to sibling `portfolio-harness` | `python scripts/check_docs_portfolio_links.py` |
| `list_capabilities.py` | Emit harness manifest (`capabilities.harness.yaml`) as JSON for scripts/checklist discovery | `python scripts/list_capabilities.py` |
| `verify_async_tasks.py` | Validate `state/async_tasks.yaml` task ledger schema | `python scripts/verify_async_tasks.py` |
| `verify_contract_hash.py` | Verify `docs/contracts/scp_mcp_v1.md` SHA-256 matches `docs/contracts/scp_mcp_v1.sha256` | `python scripts/verify_contract_hash.py` |
| `verify_script_index.py` | Parity: `capabilities.harness.yaml` `scripts[]` == on-disk scripts; each basename in this table | `python scripts/verify_script_index.py` |
| `verify_skills_readme.py` | `.cursor/skills/README.md` table vs each `SKILL.md` `description:` | `python scripts/verify_skills_readme.py` |
| `brain_map_viewer.html` | Local HTML viewer for graph JSON | Open in browser; optional dev aid |

**Clipboard / headless:** `copy_continue_prompt.*` copies to the **system clipboard** and assumes an interactive session with clipboard support. In **headless or CI** environments, agents should read [`state/continue_prompt.txt`](../state/continue_prompt.txt) directly or paste from that file instead of relying on clipboard APIs.

**Skills (JIT primitives):** `.cursor/skills/*/SKILL.md` — loaded by convention; start from [README.md](../README.md) Contents list.

## Memory load order

intent_surface → session_brief → handoff → preferences → rejection_log → decision-log → known-issues → daily (optional) → async scope + `async_tasks.yaml` when `latency_tolerance: async_ok`

See [SESSION_BOOTSTRAP.md](SESSION_BOOTSTRAP.md) for the same sequence with file pointers. See [OPENHARNESS_CONTEXT_MAP.md](OPENHARNESS_CONTEXT_MAP.md) for checklist → path mapping.

## Feedback loops (learning from corrections)

- **Preferences:** Human-stated preferences agents follow. Load at session start.
- **Rejection_log:** When human rejects a proposal, ask "Log this for future sessions?" If yes, append to rejection_log.
- **Flow:** Correction → "Log this?" → preferences (preference) or rejection_log (rejection) → future sessions avoid the same mistake.

## Handoff schema (essential fields)

- decision_id
- Done (2–5 bullets)
- Next (one clear action)
- Paths/artifacts
- scope (optional)
- human_gate (optional)
- latency_tolerance (sync | async_ok)
- intent (optional)

## Archive rule

Before overwriting handoff_latest, copy to handoff_archive/YYYYMMDD-HHMMSS.md.
