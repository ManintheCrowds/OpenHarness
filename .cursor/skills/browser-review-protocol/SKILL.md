---
name: browser-review-protocol
description: Structured manual or MCP-driven frontend review—URL, auth, viewports, flows, evidence. Use for smoke UI, PR UI check, repeatable browser QA.
triggers_any: ["review frontend", "browser review", "smoke UI", "manual UI verification", "verify UI in browser", "frontend QA", "structured browser review", "UI smoke test"]
do_not_trigger_if: ["API only", "no browser", "critic score only"]
exclusive_with: []
required_inputs: ["BrowserReviewSpec or equivalent: base URL, routes, auth, viewports, 3–5 flows with expected outcomes, critical screens"]
forbidden_actions: ["skip console/network check when user asked for full review", "screenshot before snapshot confirms readiness on dynamic sites"]
exit_criteria: "BrowserReviewReport: PASS/FAIL per flow; critical screens have snapshot + screenshot evidence; console and failed network summarized; blockers documented."
output_schema: "Markdown report: Flow | Result | Notes; Evidence (paths/refs); Console summary; Failed requests; Blockers."
---

# Browser-review-protocol (delegated)

**Canonical skill (edit there):** [MiscRepos `browser-review-protocol` SKILL](../../../MiscRepos/.cursor/skills/browser-review-protocol/SKILL.md)

**OpenHarness-only:** Gap-analysis cross-links in the canonical skill may reference paths under this repo’s `docs/research/`; keep those artifacts here.

See [product-scope SKILL](../product-scope/SKILL.md) header for delegation policy and sibling layout.
