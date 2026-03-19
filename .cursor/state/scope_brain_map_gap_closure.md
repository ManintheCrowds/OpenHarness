# Brain Map Gap Closure — Scope

**Source:** [BRAIN_MAP_PROCESS_GAP_ANALYSIS.md](../docs/BRAIN_MAP_PROCESS_GAP_ANALYSIS.md)

## Priorities

### Must close (G1–G3, G6–G8)

- **G1–G3 (tool/credential):** Document tunnel or accept manual; accept manual WCAG until credentials fixed; add port fallback
- **G6–G8 (process):** Add stop server steps; define screenshot path; document critic threshold

**Rationale:** Tool/process gaps block repeatability; these are implementable without external dependencies.

### Explicitly accept (G9, G10)

- **G9:** No automated a11y in CI — document as known limitation; manual WCAG checklist when BrowserStack unavailable
- **G10:** Graph viz a11y product gap — keyboard + screen reader not supported; track in product backlog

**Rationale:** A11y gaps are product backlog; not blocking audit repeatability.

### Defer (G12–G17)

- **G12–G17:** Plan drift, canonical flow, context-atlas in plan verification, scan log, cross-repo docs, absolute paths

**Rationale:** Lower risk; can batch later.

---

## Handoff note

When delegating gap closure: implement G1–G3, G6–G8. Do **not** implement G9, G10 (accepted). G12–G17 deferred.
