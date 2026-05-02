---
name: planning
description: Use when the user wants to plan first, decompose a task, or produce a WBS before implementing. Produces structured work breakdown, gets approval, then implements phase by phase.
triggers_any: ["plan first", "decompose", "multi-step", "complex task", "WBS", "break down"]
do_not_trigger_if: ["single step", "trivial change", "docs only"]
exclusive_with: []
required_inputs: ["task or goal to decompose"]
exit_criteria: "WBS produced and approved; implementation follows phases (or handoff with Next = next phase)"
output_schema: "WBS (numbered steps); optional .plan.md; implementation proceeds phase by phase"
tier: 2
upstream_inputs: "Task or goal; optional product-scope output, scope doc, or scope-notes."
downstream_output: "Numbered WBS with dependencies; optional .cursor/plans/*.plan.md; phase boundaries for handoff."
handoff_format: "Numbered steps; each step has verifiable output; Next/Paths/Decisions when handing off between chats."
---

# Planning (delegated)

**Canonical skill (edit there):** [MiscRepos `planning` SKILL](../../../MiscRepos/.cursor/skills/planning/SKILL.md)

See [product-scope SKILL](../product-scope/SKILL.md) header for delegation policy and sibling layout.
