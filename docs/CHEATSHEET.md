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

## Memory load order

intent_surface → session_brief → handoff → preferences → rejection_log

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
