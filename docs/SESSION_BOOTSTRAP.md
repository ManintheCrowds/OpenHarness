# Session bootstrap

**Purpose:** In a **new session**, load context in a consistent order so intent and memory stay aligned. Matches [CHEATSHEET.md](CHEATSHEET.md) **Memory load order** and [HARNESS_ARCHITECTURE.md](HARNESS_ARCHITECTURE.md) § Memory.

## Order (read / load)

1. **intent_surface** — `state/intent_surface.md` (if present)
2. **session_brief** — `state/session_brief.md` (if present)
3. **handoff** — `state/handoff_latest.md` (or `.cursor/state/handoff_latest.md` when using a local-only copy; see [state/README.md](../state/README.md))
4. **preferences** — `state/preferences.md` or `preferences.json`
5. **rejection_log** — when proposing work similar to past rejections

6. **decision-log** — `state/decision-log.md` (if present)
7. **known-issues** — `state/known-issues.md` (if present)
8. **daily** — optional: `state/daily/YYYY-MM-DD.md` for today or recent days (session summaries)

Then use project-specific docs, rules, and skills as routed (e.g. [.cursor/rules/](../.cursor/rules/), [.cursor/skills/](../.cursor/skills/)).

## Related

- [HANDOFF_FLOW.md](HANDOFF_FLOW.md) — archive, write handoff, continue prompt
- [CHEATSHEET.md](CHEATSHEET.md) — one-page map and script index
- [AGENT_ENTRY.md](AGENT_ENTRY.md) — agent entry chain
- [OPENHARNESS_CONTEXT_MAP.md](OPENHARNESS_CONTEXT_MAP.md) — checklist → file paths
