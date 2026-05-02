---
name: product-scope
description: Use when eliciting requirements, acceptance criteria, or "what are we building?" Captures scope before implementation. Composes with tech-lead and docs.
triggers_any: ["requirements", "acceptance criteria", "what are we building", "scope", "user story", "product scope"]
do_not_trigger_if: ["where does this go", "architecture only", "placement only"]
exclusive_with: []
required_inputs: ["feature or area", "constraints if any"]
exit_criteria: "Requirements or acceptance criteria captured; optional: scope doc"
output_schema: "Markdown: requirements list, acceptance criteria, optional scope doc"
tier: 2
upstream_inputs: "User goal, feature area, or vague idea; optional constraints (time, tech, compliance)."
downstream_output: "Numbered requirements, testable acceptance criteria, optional scope doc path; stack choice if step 5 ran."
handoff_format: "Markdown sections for Requirements and Acceptance criteria; link to scope file if written; include agent parity line if UI/API."
---

# Product-scope (delegated)

**Canonical skill (edit there):** [MiscRepos `product-scope` SKILL](../../../MiscRepos/.cursor/skills/product-scope/SKILL.md)

OpenHarness keeps this file so the skill stays **discoverable** when only this repo is a workspace root. **Procedure, examples, and handoff rules** live in MiscRepos — portfolio harness SSOT for shared skills ([MiscRepos `local-proto/docs/REPO_BOUNDARY_INDEX.md`](../../../MiscRepos/local-proto/docs/REPO_BOUNDARY_INDEX.md) — Cursor skills row).

**If the link 404s:** Clone **MiscRepos** next to **OpenHarness** (same parent folder), or add MiscRepos to your Cursor workspace; when opening **local-proto** alone, run [Ensure-HarnessSkillsJunction.ps1](../../../MiscRepos/local-proto/scripts/Ensure-HarnessSkillsJunction.ps1) with `MISCREPOS_ROOT` set.

**Do not** grow long role bodies here; change requests go to the MiscRepos file above.
