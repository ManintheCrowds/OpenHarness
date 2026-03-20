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

# Browser review protocol

Turn “review the frontend” into a **repeatable script**. Task authors fill **BrowserReviewSpec**; executors (agent or human) follow the checklist and emit **BrowserReviewReport**.

**Compose with**

- **qa-verifier** — Treat each flow as a runtime check; overall PASS only if all flows PASS and no unexpected console errors / failed network on critical paths.
- **Browser Ready (dynamic sites):** After `browser_navigate`, use `browser_wait_for` (time or textGone), then `browser_snapshot` until loading UI is gone (2–3 iterations max). Only then click, fill, or screenshot. If your workspace includes the portfolio-harness **browser-web** skill, use it for the full pattern and port registry.

## When to load

- After a frontend change, before merge or “done.”
- User asks for smoke test, manual browser QA, or structured UI review.
- Subagent handoff: paste a filled BrowserReviewSpec and ask for execution + report.

## Task author template (copy-paste)

```markdown
## BrowserReviewSpec
- **Base URL:**
- **Route(s):**
- **Auth:** none | test account | dev bypass (where creds live: credential vault / env — never paste secrets in spec)
- **Viewports:** e.g. 375×667 (mobile), 1280×720 (desktop); optional tablet if relevant
- **Flows (3–5):**
  1. … → **Expected:** …
  2. …
  3. …
- **Critical screens** (snapshot + screenshot each after flow stabilizes): …
```

## Executor checklist (agent)

1. **Resolve URL** — From spec; for local dev use project README or `ports.json` if the repo documents it.
2. **Per viewport** — `browser_resize` → `browser_navigate` → Browser Ready loop (wait → snapshot until ready).
3. **Per flow** — Perform steps; confirm **Expected** via snapshot (and interaction if needed).
4. **Per critical screen** — `browser_snapshot` → `browser_take_screenshot` (snapshot first).
5. **Console** — `browser_console_messages`; summarize errors and material warnings (cap output if huge).
6. **Network** — `browser_network_requests`; list failed requests (4xx, 5xx, blocked, obvious CORS) with URL and status when available.
7. **Report** — Emit **BrowserReviewReport**. Note blockers: missing auth, server down, credential gates.

## BrowserReviewReport (output shape)

| Flow | Result (PASS/FAIL) | Notes |
|------|-------------------|-------|
| 1. … | | |
| … | | |

- **Evidence:** snapshot/screenshot filenames or paths for each critical screen (per viewport if different).
- **Console:** brief summary; list distinct error messages.
- **Failed network:** URL — status / failure reason.
- **Blockers:** env, auth, or tooling gaps.

## Tool map (cursor-ide-browser)

| Step | Tool |
|------|------|
| Set viewport | `browser_resize` |
| Open page | `browser_navigate` |
| Wait | `browser_wait_for` |
| Structure / refs | `browser_snapshot` |
| Visual evidence | `browser_take_screenshot` |
| JS errors / warnings | `browser_console_messages` |
| HTTP failures | `browser_network_requests` |
| Interactions | `browser_click`, `browser_fill`, `browser_fill_form`, `browser_scroll`, … |

## References

- [BROWSER_REVIEW_PROTOCOL.md](../../docs/BROWSER_REVIEW_PROTOCOL.md)
- [docs/BRAIN_MAP_E2E.md](../../../docs/BRAIN_MAP_E2E.md) — example navigate → wait → snapshot → screenshot
