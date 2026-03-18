---
name: planning
description: Use when the user wants to plan first, decompose a task, or produce a WBS before implementing. Produces structured work breakdown, gets approval, then implements phase by phase.
triggers_any: ["plan first", "decompose", "multi-step", "complex task", "WBS", "break down"]
do_not_trigger_if: ["single step", "trivial change", "docs only"]
exclusive_with: []
required_inputs: ["task or goal to decompose"]
exit_criteria: "WBS produced and approved; implementation follows phases (or handoff with Next = next phase)"
output_schema: "WBS (numbered steps); optional .plan.md; implementation proceeds phase by phase"
---

# Planning / deliberation role

**Intent:** Plan before act; decompose complex tasks into explicit phases.

## When to use

- User says "plan first", "decompose", "multi-step", "complex task", "WBS", or "break down".
- Task has 3+ distinct steps or touches 3+ files.
- User wants explicit phases before implementation.

## Inputs

- Task or goal to decompose (from user message or handoff Next).

## Steps

1. **Decompose:** Produce a WBS (1. … 2. … 3. …) with dependencies. Number steps; note which can run in parallel. Aim for subtasks under 2 hours each, with clear input/output and independent verification.
2. **Present:** Show WBS to user; ask for approval or modifications.
3. **On approval:** Implement phase by phase. After each phase: update handoff Done/Next; optionally handoff to new chat if context is long.
4. **Optional:** Write `.cursor/plans/<name>.plan.md` for multi-phase plans; link from handoff.

## Handoff

For multi-phase work, handoff when phase boundary or role switch. Include: Next (one clear action), Paths (artifacts, plans), Decisions (gotchas).

## Checks

- WBS is explicit and numbered.
- For non-trivial work: ensure a spec exists (from product-scope or equivalent) before decomposing.
- User approves before implementation.
- Implementation follows phases; handoff updated after each phase.

## Suggested sequence (compose with)

- **Often precedes:** refactor-reuse (implement), critic (review).
- **Typical chain:** planning → refactor-reuse → critic.

## Guardrails

- **Privacy:** Do not expose internal project paths in shared plans; use generic placeholders when handoff may be shared.
- **Human gate:** Escalate when uncertain; do not auto-resolve conflicts between roles.
