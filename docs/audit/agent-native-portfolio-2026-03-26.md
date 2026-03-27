# Agent-native architecture review: portfolio (OpenGrimoire + harness + SCP + MiscRepos)

**Date:** 2026-03-26  
**Scope (local repos):** `OpenAtlas` (OpenGrimoire), `OpenHarness`, `SCP`, `MiscRepos` — treated as one **operator stack**, not a single deployable app. **Out of scope** for this pass: other multi-root workspace folders (e.g. `software`, `VibeLedger`, `Arc_Forge` plan-only trees) unless added explicitly.  
**Method:** Eight parallel codebase explorations (one per principle), merged here. Denominators differ by principle; **do not** treat a single “overall %” as precision without reading caveats.

**References:** [OpenHarness `.cursor/skills/agent-native-architecture/SKILL.md`](../../.cursor/skills/agent-native-architecture/SKILL.md), `references/action-parity-discipline.md` (same skill folder).

---

## Overall score summary

| Core principle | Score | Percentage | Status |
|----------------|-------|------------|--------|
| 1. Action parity | 18 / 21 outcomes | 86% | Strong |
| 2. Tools as primitives | 37 / 63 (tools + MCP servers + scripts + CLIs) | 59% | Partial |
| 3. Context injection | 5 / 7 channel types “present & usable if loaded” | 71% | Partial |
| 4. Shared workspace | 4 / 5 surfaces (conservative handoff fork) | 80% | Strong |
| 5. CRUD completeness | 2 / 4 entities strict full CRUD; 4 / 4 contract-honest | 50% / 100% | See §5 |
| 6. UI integration | 2 / 6 OpenAtlas HTTP write paths (strict auto-refresh) | 33% | Needs work |
| 7. Capability discovery | 4 / 7 mechanisms (quality ≥ 2) | 57% | Partial |
| 8. Prompt-native features | 12 / 16 sampled behaviors | 75% | Partial |

**Heuristic blend (not a benchmark):** Principles use **incompatible denominators** (e.g. MCP servers + scripts counted together for §2). **No single portfolio percentage** is computed here — use the **per-row** scores only. For any informal mental model: use **CRUD strict (50%)** when discussing entity APIs; **contract-honest CRUD (100%)** is a separate compliance reading and is **not** blended into a pseudo-mean. **UI** row uses the **strict** auto-refresh definition; §6 notes an **inclusive** alternate (~63% for OpenAtlas HTTP surfaces).

**Status legend:** Excellent 80%+; Partial 50–79%; Needs work &lt;50%.

---

## 1. Action parity (18/21, ~86%)

**Denominator Y:** 21 distinct meaningful user/automation outcomes across REST UI, documented HTTP/CLI, harness scripts, SCP MCP, MiscRepos maps.

**Gaps:** HITL intent survey backlog (no shipped surface); optional in-repo MCP for OpenGrimoire not default; presentational `/` without REST entity; some viz/demo routes not mirrored in `GET /api/capabilities`; cross-client alignment UX relies on polling/focus, not live sync.

**Evidence:** OpenAtlas `docs/AGENT_INTEGRATION.md`, `docs/ARCHITECTURE_REST_CONTRACT.md`, `src/app/api/capabilities/route.ts`; OpenHarness `docs/HARNESS_ARCHITECTURE.md`, `docs/SESSION_BOOTSTRAP.md`, `docs/CHEATSHEET.md`; SCP `README.md`; MiscRepos `.cursor/docs/MCP_CAPABILITY_MAP.md`, `COMMANDS_README.md`.

---

## 2. Tools as primitives (37/63, ~59%)

**Denominator Y:** SCP MCP tools (9) + MiscRepos stub (2) + `mcp.json` server entries (18) + MiscRepos `scripts/*.py` (31) + OpenAtlas `scripts/*.mjs` (3) = 63.

**Workflow-heavy:** `scp_run_pipeline`, Playwright/Docker/Daggr/OpenRAG MCP servers, orchestrator, eval pilots, `write_handoff.py`, `build_brain_map.py`, etc.

**Caveat:** Many MiscRepos scripts are **harness CLIs**, not MCP — high workflow count is expected there.

**Evidence:** `SCP/src/scp/scp_mcp.py`, `MiscRepos/.cursor/mcp.json`, `MiscRepos/.cursor/scripts/`, `OpenAtlas/scripts/alignment-context-cli.mjs`.

---

## 3. Context injection (5/7 documented channels, ~71%)

**Seven channel types:** (1) always rules (2) session bootstrap (3) capabilities manifest (4) handoff/state (5) MCP maps (6) daily/recent (7) workspace file graph.

**Auto-injected without @files:** Only a **subset** of rules (`alwaysApply` in MiscRepos, `CLAUDE.md` when OpenAtlas root is active). Bootstrap, manifests, and handoff are **documented**, not automatically injected — agents must follow `SESSION_BOOTSTRAP.md` / CHEATSHEET.

**Gap:** No committed workspace-wide file graph packet; daily notes uneven outside OpenHarness-shaped `state/daily/`.

**Evidence:** `OpenHarness/docs/SESSION_BOOTSTRAP.md`, `MiscRepos/.cursor/rules/agent-intent.mdc`, `OpenAtlas/src/app/api/capabilities/route.ts`, `MiscRepos/.cursor/docs/MCP_CAPABILITY_MAP.md`.

---

## 4. Shared workspace (4/5 conservative, 80%)

**Surfaces:** OpenAtlas SQLite + brain-map JSON via `GET /api/brain-map/graph`; OpenHarness `async_tasks.yaml` + markdown state; MiscRepos `.cursor/state`.

**Fork risk:** OpenHarness allows `state/handoff_latest.md` **or** gitignored `.cursor/state/handoff_latest.md` — same role, two physical files if both used.

**Cross-repo:** OpenHarness vs MiscRepos paths are **not** one inode unless mirrored.

**Evidence:** `OpenAtlas/src/db/client.ts`, `src/app/api/brain-map/graph/route.ts`, `OpenHarness/state/README.md`, `OpenHarness/.gitignore`.

---

## 5. CRUD completeness

| Reading | Score | Notes |
|---------|-------|--------|
| **Strict** (full CRUD per mutable entity) | **2 / 4** (50%) | Alignment context + brain map read-only OK; survey lacks API U/D; moderation lacks DELETE. |
| **Contract-honest** | **4 / 4** (100%) | Matches `ARCHITECTURE_REST_CONTRACT.md` — no silent claims. |

**Auth session:** HTTP login/session/logout — not table CRUD.

**OpenHarness `async_tasks.yaml`:** File edit + `verify_async_tasks.py` only; **mini score 0/1** for programmatic task CRUD API.

**Evidence:** `OpenAtlas/docs/ARCHITECTURE_REST_CONTRACT.md`, `src/db/schema.ts`, `src/app/api/**/route.ts`, `OpenHarness/scripts/verify_async_tasks.py`.

---

## 6. UI integration (strict 2/6 ~33%; inclusive ~63%)

OpenAtlas uses **fetch + local state**, not SWR/React Query/`revalidatePath`. **Stale until refresh:** survey POST vs open visualization/quotes views; agent alignment mutations vs idle admin tab; brain map after offline JSON merge (documented manual reload; no SSE).

Harness/MiscRepos: file-based “UI” = IDE; no live channel.

**Evidence:** `OpenAtlas/src/lib/hooks/useSurveyForm.ts`, `useVisualizationData.ts`, `admin/alignment/page.tsx`, `src/app/api/capabilities/route.ts`, `OpenHarness/docs/SESSION_BOOTSTRAP.md`.

---

## 7. Capability discovery (4/7, ~57%)

| # | Mechanism | Present (quality ≥ 2)? |
|---|-----------|-------------------------|
| 1 | Onboarding for agent capabilities | Weak |
| 2 | Help documentation | Yes |
| 3 | UI hints (`/capabilities`) | Yes (OpenAtlas) |
| 4 | Self-describe (`/api/capabilities`, harness YAML) | Yes |
| 5 | Suggested prompts | Partial (harness scripts, not in-app chips) |
| 6 | Empty state guidance | Partial |
| 7 | `/help`, `/tools` | Mismatch (Cursor commands + `/cl4r1t4s`, not `/tools`) |

**Inclusive count (5/7)** if `.cursor/commands` counts toward item 7.

---

## 8. Prompt-native features (12/16, ~75%)

Strong prompt-led layer: `.cursor/commands`, rules (`agent-intent`, critic loop, role routing), skills, handoff templates.

**Code-led:** orchestrator daemon/integrations, structural validators, handoff checksum pipeline, pilot regex graders.

**Evidence:** `MiscRepos/.cursor/commands/`, `MiscRepos/.cursor/scripts/orchestrator.py`, `run_async_support_pilot.py`, `OpenHarness/.cursor/commands/`.

---

## Top 10 recommendations (by impact)

| Priority | Action | Principle | Effort |
|----------|--------|-----------|--------|
| 1 | Invalidate or refetch survey visualization + approved-quotes after `POST /api/survey` (or `router.refresh` / shared cache) | UI integration | M |
| 2 | Ship or document **one** canonical handoff path (OpenHarness `state/` vs `.cursor/state/`) | Shared workspace | S |
| 3 | Extend `GET /api/capabilities` routes list for viz/demo pages **or** explicitly mark them N/A | Action parity / discovery | S |
| 4 | Add **human-gated** or **read-only-by-default**, schema-validated **task ledger CLI or MCP** (optional) for `async_tasks.yaml` | CRUD | M |
| 5 | Session-start script or rule snippet that `@`’s bootstrap + capabilities (operationalize “injection”) | Context injection | S |
| 6 | Split or document `scp_run_pipeline` vs primitive steps for agent control | Tools as primitives | S |
| 7 | Implement or defer **HITL intent survey**; remove ambiguity from agent integration doc | Action parity | L |
| 8 | Optional OpenGrimoire MCP package **or** explicit “HTTP+CLI is the default agent surface” in capabilities | Action parity | M |
| 9 | First-class `/help` or deepen `/capabilities` copy for onboarding | Capability discovery | M |
| 10 | Externalize orchestrator judge strings / pilot graders to config for prompt-only tuning | Prompt-native | M |

---

## What is working well

1. **REST + CLI contract** for alignment context and public alignment API with documented auth matrix.  
2. **Public capabilities manifest** and human `/capabilities` page in OpenGrimoire.  
3. **SCP MCP** surface is small, inspectable, and contract-tested (`tests/test_mcp_contract_v1.py`).  
4. **Harness documentation** (SESSION_BOOTSTRAP, CHEATSHEET, ASYNC_HITL_SCOPE) gives a repeatable memory order.  
5. **Policy layer** (agent-intent, critic loop, handoff flow) is overwhelmingly prompt-editable.

---

## Portfolio caveats

- **Do not** equate “Cursor agent can run_terminal_cmd” with **in-app** agent parity; parity here means **documented HTTP, MCP, or stable CLI**.  
- **Admin/session** parity requires **same auth boundaries** (cookie or secret headers), not bypassing gates.  
- **Third-party MCP servers** are only classified at integration boundary; internal tool granularity may differ.  
- This report **does not** replace per-repo security review or OWASP LLM testing.

---

## Critic review (methodology gate)

**Verdict:** Pass **after revisions** — headline pseudo-mean and placeholder links removed; CRUD/UI lenses clarified; discovery matrix reconciled with Top 10.

| Axis | Score (0–10) |
|------|----------------|
| Methodology | 7 |
| Honesty | 8 |
| Safety | 9 |
| Actionability | 8 |

**Must-fix applied in this revision:** (1) Removed single **~64%** portfolio mean; replaced with non-blend disclaimer. (2) Dropped stub `https://github/` links; scope uses local repo names. (3) UI strict vs inclusive called out below summary table. (4) CRUD strict vs contract-honest blend rule stated. (5) Help mechanism row set to **Partial** to match `/help` recommendation.

**Optional follow-ups (not blocking):** Enumerate 21 action-parity outcomes in an appendix for reproducibility; split §2 into MCP vs CLI sub-scores.

---

## Appendix: subagent IDs (explore passes)

Action parity · Tools primitives · Context · Shared workspace · CRUD · UI · Discovery · Prompt-native — executed as eight readonly explore tasks; raw outputs retained in session logs only.
