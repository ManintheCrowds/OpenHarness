# State Schema

Shared agent and project memory. Append-only or append-mostly. Use this schema so any agent or human can read and append without inventing a new format.

**Integration:** Copy into your project (e.g. `.cursor/state/`). Adapt paths in scripts and continue_prompt.txt.

---

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

---

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

## scope (optional)
<session boundary>

## intent (optional)
<one-line goal>

## latency_tolerance (optional)
sync | async_ok
```

See [docs/HANDOFF_FLOW.md](../docs/HANDOFF_FLOW.md) and [docs/INTENT_ENGINEERING.md](../docs/INTENT_ENGINEERING.md).

---

## decision-log.md

- **Section per date:** `## YYYY-MM-DD`
- **Each entry:** `- **[Area]** Decision: <one-line>. Rationale: <optional short>.` Optional: `(plan: <name or path>)`

---

## known-issues.md

- **Section per repo or area:** `## [Repo or area]`
- **Each entry:** `- **Location:** <path>. **Issue:** <one-line>. **Note:** <optional>.`
- **Optional:** `**Symptom:** <exact error>` so agents can search by message.

---

## preferences / rejection_log

- **preferences:** Human-stated preferences agents follow. Load at session start.
- **rejection_log:** When human rejects a proposal, ask "Log this for future sessions?" If yes, append with reason and constraint (what AI should do next time).

---

## daily/YYYY-MM-DD.md

- **Schema:** One block per session: `## HH:MM` or `## Session N`, then 2–5 bullets (what was done, key paths), optional "Next" in one line.
- **Summarize today:** Read this file when user asks "summarize everything we worked on today."
