# Precedence and steering (macro / micro / escalate)

Short spec aligned with [north-star brainstorm Pass A/B](brainstorms/2026-03-22-org-intent-north-star-brainstorm.md): **weekly human choice** for cross-domain trade-offs, **soft rank** only as a narrow tie-break, and **escalate** when steering is missing and domains conflict.

---

## Macro: weekly steering (overrides)

- **Source:** End-of-week or start-of-week answer to: *Given last week’s outcomes, which domain gets emphasis this week?*
- **Effect:** This one-line **weekly steering constraint** overrides generic habits for that period. Feed it into task decomposition prompts and OpenAtlas alignment tags (e.g. `weekly_steering: wealth`).
- **Authority:** Humans; not inferred by agents from lagging metrics alone.

## Micro: soft rank (when steering is silent)

- **Only when** weekly steering does **not** resolve a **micro-decision** (small, concrete choice).
- **Parent tie-break:** **Health → Wealth → Influence** (within-week, **not** overriding explicit weekly choice).
- **Between Influence lanes (art / open source / collective):** **No** default order—**escalate** or fold into the next weekly steering session (per Pass A soft-rank note).

## Escalate (no silent default)

- When **domains conflict** and **weekly steering is absent** for that decision: **escalate**—do not choose wealth vs health vs influence by model habit.
- When **goal** conflicts with **constraint** or **hard_boundary**: escalate; do not prefer goal by default ([INTENT_ENGINEERING.md](INTENT_ENGINEERING.md), org-intent `value_hierarchy`).

## Intent-alignment gate calibration

- Use for **drift** and **constraint violations**, not every discussion of trade-offs.
- Raise **drift_score** / set **`escalate`: true** when **unresolved conflict** would ship without human choice—not when listing options.

## Related

- [critic-log-org-intent.md](critic-log-org-intent.md) — rolling mitigations and dual-source-of-truth
- [INTENT_ENGINEERING.md](INTENT_ENGINEERING.md) — `latency_tolerance`, `human_gate`
