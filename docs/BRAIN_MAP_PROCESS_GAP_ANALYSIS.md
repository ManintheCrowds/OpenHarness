# Brain Map Visual Audit Process — Gap Analysis

**Scope:** The Brain Map visual audit and E2E process as defined by the plan, BRAIN_MAP_AUDIT.md, BRAIN_MAP_E2E.md, and execution artifacts.

**Purpose:** Document every gap between intended process, documented process, and actual execution so gaps can be closed or explicitly accepted.

---

## 1. Process Scope (Product-Scope)

### 1.1 What We Are Analyzing

- **Process:** Brain Map full visual audit and E2E analysis
- **Artifacts:** Plan (brain_map_visual_audit_e2e_db0918a7.plan.md), BRAIN_MAP_AUDIT.md, BRAIN_MAP_E2E.md, context-atlas.spec.ts
- **Components:** Parser (OpenHarness + portfolio-harness), standalone viewer (vis-network), OpenAtlas context-atlas (D3)
- **Success criteria:** Parser valid, viewers load, screenshots captured, critic JSON produced, docs updated

### 1.2 Requirements (Explicit)

| ID | Requirement | Source |
|----|-------------|--------|
| R1 | Parser exits 0; JSON has nodes, edges, generated, sessionCount | Plan, Audit |
| R2 | Standalone viewer loads; nodes or dropzone visible | Plan, Audit |
| R3 | OpenAtlas context-atlas loads; graph or empty state visible | Plan, Audit |
| R4 | Screenshot captured for audit evidence | Plan, Audit |
| R5 | Critic JSON produced (domain: workflow_ui) | Plan, critic-loop-gate |
| R6 | BRAIN_MAP_AUDIT.md and BRAIN_MAP_E2E.md updated with findings | Plan |
| R7 | Accessibility scan when feasible (BrowserStack tunnel or staging) | Plan, Audit |
| R8 | WCAG 2.1 AA guidance applied (manual when scan unavailable) | Audit |

---

## 2. Documented Gaps (Every Gap)

### 2.1 Tool / Credential Gaps

| Gap ID | Gap | Detail | Status |
|--------|-----|--------|--------|
| G1 | **BrowserStack scan unreachable** | `startAccessibilityScan` requires public URL. localhost is not reachable from BrowserStack cloud without tunnel. | Documented in Audit; no automated scan possible without tunnel |
| G2 | **accessibilityExpert 401** | BrowserStack MCP returns 401 (Invalid credentials). WCAG guidance must be applied manually. | Documented; credential/config fix required to use expert |
| G3 | **Port collision** | Plan assumes 8080 and 3000. Execution found 8080 (ERR_EMPTY_RESPONSE), 3000/3001 in use → OpenAtlas dev server used 3002. | Partially documented (port fallback in E2E); plan still hardcodes 8080/3000 |

### 2.2 Process Gaps

| Gap ID | Gap | Detail | Status |
|--------|-----|--------|--------|
| G4 | **No standalone viewer E2E spec** | Standalone viewer (brain_map_viewer.html) has no Playwright spec. Only manual browser steps in E2E playbook. | Not automated |
| G5 | **No parser E2E** | Parser verification is manual (run script, check JSON). No automated schema validation in CI. | Not automated |
| G6 | **Server lifecycle not in playbook** | Plan says "Stop HTTP server after audit" and "Stop dev server after audit"; E2E playbook does not include stop steps. | Undocumented in playbook |
| G7 | **Screenshot storage undefined** | Plan says "browser_take_screenshot — visual evidence" but does not specify path, naming, or retention. | Ad hoc in execution |
| G8 | **Critic score threshold undefined** | critic-loop-gate requires pass/score but no explicit threshold (e.g. score ≥ 0.8) is documented. | Implicit |

### 2.3 Accessibility Gaps

| Gap ID | Gap | Detail | Status |
|--------|-----|--------|--------|
| G9 | **No automated a11y in CI** | When BrowserStack is unavailable, accessibility is manual only. No axe-core, pa11y, or similar in Playwright. | No fallback automation |
| G10 | **Graph viz a11y product gap** | WCAG table documents keyboard + screen reader as product gap for D3/vis-network. No parallel accessible data view. | Known limitation; not remediated |
| G11 | **Manual WCAG checklist not in E2E** | BRAIN_MAP_AUDIT.md has WCAG table; E2E playbook Step 8 says "Manual checklist" but does not enumerate steps. | Checklist exists but not integrated into playbook flow |

### 2.4 Documentation Gaps

| Gap ID | Gap | Detail | Status |
|--------|-----|--------|--------|
| G12 | **Plan vs docs drift** | Plan references port 8080, 3000; docs now say 8888 fallback, 3001/3002/3003. Plan file is not edited per user instruction. | Plan stale |
| G13 | **OpenHarness vs portfolio-harness split** | Parser exists in both; output paths differ. Docs reference both but no single "canonical" flow. | Intentional; could be clearer |
| G14 | **context-atlas.spec.ts not in plan verification** | Plan Verification section does not list "context-atlas E2E passes" as a criterion. | Plan incomplete |
| G15 | **BrowserStack scan log empty** | Scan evidence procedure exists in Audit (§Optional — record scan evidence) but is optional; scan log table has no real rows. Gap: integration into main E2E flow or first-scan runbook missing. | Placeholder only |
| G18 | **R6 traceability** | R6 ("docs updated with findings") is not verifiable per run — no checklist or automated check that docs were updated after an audit. | Not verifiable |

### 2.5 Repo / Path Gaps

| Gap ID | Gap | Detail | Status |
|--------|-----|--------|--------|
| G16 | **Docs in OpenHarness, OpenAtlas in portfolio-harness** | BRAIN_MAP_AUDIT.md, BRAIN_MAP_E2E.md live in openharness; context-atlas and OpenAtlas app in portfolio-harness. Cross-repo references. | Architectural; may be intentional |
| G17 | **Standalone viewer path** | Plan says OpenHarness scripts/; E2E says D:\openharness\scripts. Absolute path in docs. | Environment-specific |

---

## 3. Acceptance Criteria for Gap Closure

| Gap | Closure Criteria |
|-----|------------------|
| G1 | **Closed (accept):** Manual/staging only when tunnel unavailable. Tunnel setup documented in BRAIN_MAP_E2E.md Step 8. |
| G2 | **Closed (accept):** Accept manual WCAG until credentials fixed. Documented in scope_brain_map_gap_closure.md. |
| G3 | **Closed (accept):** Plan is reference-only; E2E has port fallback (8888, 3001/3002/3003). |
| G4 | Add standalone-viewer.spec.ts (or equivalent) or document as out-of-scope |
| G5 | Add parser schema check to CI or document as manual |
| G6 | **Closed:** Step 10 (10a Stop HTTP server, 10b Stop OpenAtlas dev server) added to BRAIN_MAP_E2E.md |
| G7 | **Closed:** Screenshot convention added to BRAIN_MAP_AUDIT.md Verification Checklist |
| G8 | **Closed:** Critic score threshold ≥ 0.8 documented in BRAIN_MAP_AUDIT.md |
| G9 | Add axe-core/pa11y to Playwright or document as future |
| G10 | Track as product backlog; or add accessible data view |
| G11 | Add enumerated WCAG substeps (1.4.3, 1.3.1, 2.1.1, 2.4.7, 4.1.2) to E2E Step 8 or link with explicit checklist reference |
| G12 | Update plan (or document plan as reference-only) |
| G13 | Add "canonical flow" section to Audit |
| G14 | Add context-atlas E2E to plan Verification |
| G15 | Add "after first successful scan" procedure |
| G16 | Add cross-repo relationship section to BRAIN_MAP_AUDIT.md or BRAIN_MAP_E2E.md |
| G17 | Use relative paths or env vars in docs |
| G18 | **Closed:** Post-audit checklist added to BRAIN_MAP_E2E.md |

---

## 4. Summary

- **Total gaps:** 18 (G18 added for R6 traceability)
- **Tool/credential:** 3
- **Process:** 5
- **Accessibility:** 3
- **Documentation:** 5 (incl. G18 traceability)
- **Repo/path:** 2

**Next:** Prioritize gaps for closure vs. explicit acceptance.

---

## 5. Critic Report (2026-03-19)

**Domain:** docs | **Score:** 0.88 | **Pass:** true

**Issues addressed:** G15 refined (procedure exists but optional); G11 closure clarified (enumerated substeps); G10/G16 closure specified (backlog location, target doc).
