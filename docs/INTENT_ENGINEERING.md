# Intent Engineering

Intent engineering treats **human intent** as the primary signal. Context and prompts serve intent.

**See also:** [CONTEXT_ENGINEERING.md](CONTEXT_ENGINEERING.md), [state/README.md](../state/README.md).

---

## Intent Schema

| Field | Type | Purpose |
|-------|------|---------|
| **intent** | string | One-line goal |
| **goal_id** | string | Optional. Goal id from goals.json |
| **scope** | string or list | Boundaries: repos, paths, features |
| **constraints** | list | Do-nots, musts |
| **human_gate** | string | Where human approval is required |
| **latency_tolerance** | enum | `sync` (wait for human) vs `async_ok` (handoff and continue later) |

---

## Constraint Architecture

| Category | Purpose | Example |
|----------|---------|--------|
| **Musts** | Required behaviors | Run pytest before marking done |
| **Must-nots** | Forbidden behaviors | Do not touch module X |
| **Preferences** | Preferred options when multiple valid | Prefer PowerShell on Windows |
| **Escalation triggers** | When to stop and ask human | Before changing auth schema |

---

## Failure Modes

1. **Synchronous assumption** — Agents run asynchronously; handoff and spec must carry enough context for the next session to act without you.
2. **Intent misalignment** — Surface the metric that matters before delegating.
3. **Goal-constraint conflict** — When goal X conflicts with constraint Y, escalate.

---

## Latency Negotiation

| Value | Meaning | When to use |
|-------|---------|-------------|
| **sync** | Human must approve before agent continues | Critical decisions, security-sensitive changes |
| **async_ok** | Agent can handoff; human approves when ready | Non-blocking work, multi-phase plans |

**Rule:** Default to `async_ok` for handoff chains. Use `sync` when the human must be present.

---

## Human Gate Protocol

1. **Agent writes handoff** with `Next: "Awaiting approval for <X>. Once approved, <next action>."`
2. **If sync:** Agent stops; human approves.
3. **If async_ok:** Agent hands off; human approves later.
4. **Next session:** If Next says "Awaiting approval", agent asks human. If updated, agent proceeds.

**Example handoff at human gate:**

```markdown
## Next
Awaiting approval for phase 1 implementation. Once approved, implement phase 2 from plan.

## human_gate (optional)
approval_before_phase_2

## latency_tolerance (optional)
async_ok
```

---

## Examples

### Intent-driven handoff

```markdown
decision_id: handoff-YYYYMMDD-HHMM
intent: Ship auth fixes; do not touch other modules
latency_tolerance: async_ok

## Done
- Applied pure-Go SQLite to auth tests
- CI: CGO_ENABLED=0

## Next
Commit auth changes. Verify: `go test ./...` passes. Do not touch other modules.

## scope
backend/auth only
```

### Session brief with intent fields

```markdown
## Intent
Fix RAG pipeline; validate with smoke test.

## Scope
daggr_workflows only.

## Constraints / Do not
Do not change campaign_kb. Do not modify Flask routes.

## human_gate (optional)
approval_before_commit

## Links
state/handoff_latest.md, plans/rag_pipeline_fixes.plan.md
```

---

## Delegation Checklist

Before delegating, ensure handoff includes:

- Acceptable paths (scope or Musts/Must-nots)
- Constraints (Must-nots, Escalation triggers)
- Explicit behavior when goal and constraint conflict: escalate
- Next is self-contained (task, paths, verification)
