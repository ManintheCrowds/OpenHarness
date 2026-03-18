# Handoff Chain Patterns

Sequential swarm: Agent A does phase 1 → handoff → Agent B does phase 2. Each "agent" is a new chat with handoff context. Use when work spans multiple phases or roles.

---

## When to Break (Handoff Between Phases)

- **Context is long** — ~20–30 exchanges; thread feels heavy.
- **Phase boundary** — One phase (planning, implementation, review) is done; next phase starts.
- **Role switch** — Different skill needed (planner → implementer → critic).
- **Human gate** — Approval or decision required before continuing.

---

## When to Use Subagent vs Handoff

**Use subagent when:** The task is a sub-step of current work; the result is needed in-session; the task is bounded.

**Use handoff when:** Phase boundary; context reset needed; human gate.

---

## What to Put in Next for Multi-Phase Chains

- **Next:** One clear action for the immediate next session.
- **Paths / artifacts:** Include any plan file, paths just created, branch name.
- **Decisions / gotchas:** Note phase-specific decisions.
- **scope (optional):** Restrict the next session.

**Example (planner → implementer):**

```markdown
## Done
- Produced WBS for user auth (5 phases)
- User approved phases 1–3

## Next
Implement phase 1 of WBS: add auth schema and migration. Do not start phase 2.

## Paths / artifacts
- plans/user_auth_wbs.plan.md
```

---

## Chain Patterns

### Planner → Implementer → Critic

1. **Session 1 (planner):** Produce WBS, get approval. Handoff: Next = "Implement phase 1".
2. **Session 2 (implementer):** Do phase 1, update handoff. Next = "Implement phase 2" or "Run critic on phase 1 output".
3. **Session 3 (critic):** Review artifact; suggest fixes. Handoff: Next = "Apply critic fixes" or "Implement phase 2".

### Multi-Phase Plan Execution

- **Next:** "Implement phase N from plan X; then update handoff Next to phase N+1."
- After each phase: update handoff Done, set Next to next phase or "Done" if complete.
- **Progress log:** Done bullets in handoff serve as the log.

---

## Rules

- Each session reads `handoff_latest.md` and any linked plan first.
- Respect `scope` in handoff; do not drift outside without asking.
- Archive before overwrite: copy `handoff_latest.md` to `handoff_archive/YYYYMMDD-HHMMSS.md` before each write.

---

## See Also

- [HANDOFF_FLOW.md](HANDOFF_FLOW.md) — single-session handoff flow
- [state/README.md](../state/README.md) — handoff schema
