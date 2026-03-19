# Brain Map Visual Audit

How to run a visual audit of the Brain Map system.

## Purpose

Verify the Brain Map parser, standalone viewer, and visualization pipeline end-to-end. Use this guide when auditing visual behavior, accessibility, or schema compliance.

## Prerequisites

- Python 3.9+
- State directory with `daily/`, `handoff_latest.md`, `handoff_archive/`, or `decision-log.md` (optional; empty state is valid)
- HTTP server (Python `http.server`) or **OpenAtlas** in portfolio-harness

## Steps

1. **Run parser** from project root:
   ```powershell
   python scripts/build_brain_map.py
   ```
   For standalone viewer, output JSON to scripts:
   ```powershell
   $env:BRAIN_MAP_OUTPUT="D:\openharness\scripts\brain-map-graph.json"; python scripts/build_brain_map.py
   ```

2. **Serve viewer** (OpenHarness standalone):
   ```powershell
   cd scripts; python -m http.server 8080
   ```

3. **Open URL:** `http://localhost:8080/brain_map_viewer.html`

4. **Optional: Accessibility scan** — See [BrowserStack Local and accessibility scans](#browserstack-local-and-accessibility-scans).

## BrowserStack Local and accessibility scans

`startAccessibilityScan` needs a URL BrowserStack can reach. **Plain `http://localhost:...` is not reachable** from BrowserStack’s cloud unless you tunnel.

**Option A — BrowserStack Local (recommended for dev)**

1. Install and start [BrowserStack Local](https://www.browserstack.com/docs/local-testing) per your OS (Binary, npm, or Desktop app).
2. Sign in with a BrowserStack account that has Accessibility Testing enabled.
3. Keep Local running while your app is up (e.g. `python -m http.server 8080` in `scripts/`, or OpenAtlas dev server on 3000/3001 — often 3002/3003 if lower ports are taken).
4. Use the **exact URL / hostname** BrowserStack shows for *your* product and flow (Accessibility, Automate, etc.). **URL patterns vary by product and change over time**—there is no single “magic” Local URL to hardcode. Rely on [BrowserStack Local docs](https://www.browserstack.com/docs/local-testing) and the Local app output when the tunnel is up.
5. Call `startAccessibilityScan` with that reachable URL (not raw `localhost` unless your Local setup explicitly maps it).

**Option B — Staging / preview URL**

Deploy the viewer (or a static export) to HTTPS staging and pass that URL to `startAccessibilityScan`.

**Credentials**

- `accessibilityExpert` and cloud scans require valid BrowserStack API credentials in MCP config. A **401** means fix keys / plan before relying on expert or scan tools.

**Optional — record scan evidence (after MCP works)**

1. Re-run `accessibilityExpert` for WCAG questions if useful.
2. Run `startAccessibilityScan` on the tunneled or staging URL; capture **scan ID** and **scan run ID** from the MCP response or BrowserStack dashboard.
3. Append to **Audit Findings** (below) or your run log: date, scanned URL, scan ID, scan run ID, short pass/fail or issue count.

## WCAG 2.1 AA — graph visualizations (Brain Map)

Apply when auditing [brain_map_viewer.html](../scripts/brain_map_viewer.html) (vis-network) or OpenAtlas D3 SVG graphs.

| Criterion | Focus for force-directed graphs |
|-----------|----------------------------------|
| **1.4.3 Contrast (Minimum)** | Node fill, edge stroke, and label text vs background meet **4.5:1** (normal text) / **3:1** (large text, UI components). Dark theme: verify grey text on `#1a1a1a` / `#262626`. |
| **1.3.1 Info and Relationships** | Graph structure is not exposed to AT by shapes alone. Provide a **textual or tabular summary** (e.g. “N nodes, M edges” plus list or download of nodes/edges) or document as known limitation for audit. |
| **2.1.1 Keyboard** | All actions (open file dialog, navigation) must be **keyboard-operable**. Canvas/SVG-only drag may exclude keyboard users; prefer documented alternative (e.g. file load, list view). |
| **2.4.7 Focus Visible** | Focusable controls (`button`, `link`, `input`, `label`) show a visible focus ring. |
| **4.1.2 Name, Role, Value** | Interactive elements have **accessible names** (`aria-label` / visible text). Complex SVG nodes often need `role="img"` + `aria-label` or an off-screen summary. |

**OpenAtlas / D3:** Circles and lines are often not announced meaningfully; treat **keyboard + screen reader** as a product gap unless you add ARIA on graph elements or a parallel accessible data view.

## Tools

| Tool | Use |
|------|-----|
| Playwright MCP | `browser_navigate`, `browser_snapshot`, `browser_take_screenshot`, `browser_wait_for` |
| cursor-ide-browser | Same browser actions |
| BrowserStack | `startAccessibilityScan` (public URL), `accessibilityExpert` (WCAG questions) |

## MCP Servers

- **playwright** — Browser automation
- **cursor-ide-browser** — Cursor embedded browser
- **browserstack** — Accessibility scans (if configured)

## Skills

- **browser-web** — Navigate, wait, snapshot, screenshot
- **brain-map-visualization** — Parser and viewer guidance
- **qa-verifier** — E2E verification flow

## Verification Checklist

- [ ] Parser exits 0; `brain-map-graph.json` exists
- [ ] JSON has `nodes`, `edges`, `generated`, `sessionCount`
- [ ] Viewer loads; nodes visible or dropzone shown for empty state
- [ ] Screenshot captured for audit evidence (save to `docs/brain_map_audit_YYYY-MM-DD.png` or equivalent; Playwright defaults to CWD if path not specified)

## Audit Findings (2026-03-19)

| Component | Status | Notes |
|-----------|--------|-------|
| Parser (OpenHarness) | PASS | Exits 0; schema valid |
| Parser (portfolio-harness) | PASS | Output to OpenAtlas/public |
| Standalone viewer | PASS | Dropzone for empty state; file input fallback; use port 8888 if 8080 fails |
| OpenAtlas `/context-atlas` (was `/brain-map`) | PASS | Graph loads; nodes visible; dev server may use 3001/3002/3003 |
| Accessibility scan | SKIP | BrowserStack requires public URL or Local tunnel |
| accessibilityExpert | SKIP | 401 (credentials); document WCAG guidance manually |

**Critic JSON (workflow_ui):** Score threshold ≥ 0.8 for pass.

```json
{
  "pass": true,
  "score": 0.85,
  "issues": [
    {"type": "accessibility", "detail": "BrowserStack scan requires public URL; localhost not directly scannable"},
    {"type": "accessibility", "detail": "accessibilityExpert returned 401 (credentials)"}
  ],
  "fixes": [
    {"action": "document", "detail": "Document BrowserStack Local tunnel for localhost scans"},
    {"action": "wcag", "detail": "Add WCAG 2.1 AA guidance for graph viz (contrast, focus, keyboard, screen reader) to audit doc"}
  ]
}
```

**Follow-up:** Sections *BrowserStack Local and accessibility scans* and *WCAG 2.1 AA — graph visualizations* above implement these fixes; [BRAIN_MAP_E2E.md](BRAIN_MAP_E2E.md) Step 8 links here.

### BrowserStack scan log (optional)

Append a row after each successful scan:

| Date (UTC) | URL scanned | Scan ID | Scan run ID | Summary |
|------------|-------------|---------|-------------|---------|
| _example_ | _https://…_ | _from MCP_ | _from MCP_ | _issue count / pass_ |
