# State Schema

Shared agent and project memory. Append-only or append-mostly. Use this schema so any agent or human can read and append without inventing a new format.

**Integration:** Copy into your project (e.g. `.cursor/state/`). Adapt paths in scripts and continue_prompt.txt.

**Public OpenHarness checkout:** Root `state/` holds the schema and **synthetic** placeholders safe to commit. **`/.cursor/state/`** is gitignored here so local session files are not pushed; use it in your workspace the same way, or keep real handoffs in a private fork ([`docs/PUBLIC_AND_PRIVATE_HARNESS.md`](../docs/PUBLIC_AND_PRIVATE_HARNESS.md)).

## Layout

| Artifact | Role |
|----------|------|
| handoff_latest.md | Current session target; Done/Next, Paths, Decisions |
| handoff_archive/ | Immutable history; copy handoff_latest before overwrite |
| decision-log.md | Append-only decisions and rationale |
| decision_index.md | Rolling index of handoffs and decisions |
| known-issues.md | Gotchas, fragile spots |
| preferences.md / preferences.json | Human-stated preferences |
| rejection_log.md / rejection_log.json | Rejected proposals and constraints |
| daily/YYYY-MM-DD.md | Session summaries per day |
| session_brief.md | Optional "read first" for new sessions |
| intent_surface.md | Optional canonical intent for multi-phase work |
| continue_prompt.txt | Canonical continue-from-handoff prompt |
| async_tasks.yaml | Machine-readable task ledger (ids, status, owner); validated in CI; see [docs/ASYNC_HITL_SCOPE.md](../docs/ASYNC_HITL_SCOPE.md) |
| swarm_runs/YYYY-MM-DD/*.yaml | Optional machine-readable swarm decision artifacts (synthetic/public examples) |

## Handoff Schema

**Required:** Done, Next, Paths/artifacts.

**Optional:** decision_id, scope, intent, constraints, human_gate, latency_tolerance, Musts, Must-nots, Escalation triggers.

**Archive rule:** Before each write, copy handoff_latest.md to handoff_archive/YYYYMMDD-HHMMSS.md.

**Template:**

```markdown
decision_id: handoff-YYYYMMDD-HHMM
Updated: <ISO8601>

## Done
- <bullet 1>
- <bullet 2>

## Next
<One clear action. Include: what, where, constraints, verification.>

## Paths / artifacts
- <path or branch or plan path>

## Decisions / gotchas (optional)
- <decision or caveat>
- Document **external tool config shims** when the declared registry limits differ from the true model or API limits (e.g. OpenClaw model registry vs. actual context or tool support).

## scope (optional)
<session boundary>

## intent (optional)
<one-line goal>

## latency_tolerance (optional)
sync | async_ok
```

When `latency_tolerance: async_ok` (or whenever multiple sessions may overlap), read **[docs/ASYNC_HITL_SCOPE.md](../docs/ASYNC_HITL_SCOPE.md)** and **`async_tasks.yaml`** after handoff so task ownership matches the machine-readable ledger.

See [docs/HANDOFF_FLOW.md](../docs/HANDOFF_FLOW.md) and [docs/INTENT_ENGINEERING.md](../docs/INTENT_ENGINEERING.md).

## swarm_runs (optional)

- Use for multi-agent/swarm decision records that need machine-readable auditing.
- Contract reference: [docs/contracts/swarm_decision_v0_1.md](../docs/contracts/swarm_decision_v0_1.md).
- Schema helper and examples: [state/swarm_runs/README.md](swarm_runs/README.md).
- Verifier: `python scripts/verify_swarm_contract.py`.

## decision-log.md

- **Section per date:** `## YYYY-MM-DD`
- **Each entry:** `- **[Area]** Decision: <one-line>. Rationale: <optional short>.` Optional: `(plan: <name or path>)`
- **Decision graph projection (optional):** Typed nodes/edges for MCP + OpenGrimoire live in a local SQLite projection (`decision-graph.sqlite`), not in this markdown file. Humans still append here only. Optional causal edges that prose cannot express: `decision-graph-edges.jsonl` beside the log (see OpenGrimoire `docs/DECISION_GRAPH_SCHEMA.md`). Rebuild: `python MiscRepos/.cursor/scripts/project_decision_graph.py` with `DECISION_LOG_PATH` / `DECISION_GRAPH_DB`.

## known-issues.md

- **Section per repo or area:** `## [Repo or area]`
- **Each entry:** `- **Location:** <path>. **Issue:** <one-line>. **Note:** <optional>.`
- **Optional:** `**Symptom:** <exact error>` so agents can search by message.

## preferences / rejection_log

- **preferences:** Human-stated preferences agents follow. Load at session start.
- **rejection_log:** When human rejects a proposal, ask "Log this for future sessions?" If yes, append with reason and constraint (what AI should do next time).

## daily/YYYY-MM-DD.md

- **Schema:** One block per session: `## HH:MM` or `## Session N`, then 2–5 bullets (what was done, key paths), optional "Next" in one line.
- **Summarize today:** Read this file when user asks "summarize everything we worked on today."
