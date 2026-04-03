# Brain Map E2E Playbook

End-to-end test steps for the Brain Map system.

## Step 1: Run Parser

**Action:** Run parser from project root.

```powershell
cd D:\openharness; python scripts/build_brain_map.py
```

**Verification:** `brain-map-graph.json` exists; JSON has `nodes`, `edges`, `generated`, `sessionCount`.

## Step 2: Start HTTP Server

**Action:** Serve the scripts directory.

```powershell
cd D:\openharness\scripts; python -m http.server 8080
```

If port 8080 fails (ERR_EMPTY_RESPONSE), use 8888 or another free port.

**Verification:** Server running on chosen port.

## Step 3: Navigate to Viewer

**Action:** Open `http://localhost:<port>/brain_map_viewer.html` (replace `<port>` with 8080 or 8888 if 8080 failed).

**Verification:** Page loads.

## Step 4: Wait for Content

**Action:** `browser_wait_for` (text: "nodes" or time: 2–3s).

**Verification:** Content ready (nodes visible or "No nodes" / dropzone).

## Step 5: Snapshot

**Action:** `browser_snapshot`.

**Verification:** Nodes visible or empty state (dropzone) shown; no console errors.

## Step 6: Screenshot

**Action:** `browser_take_screenshot`.

**Verification:** Visual evidence captured.

## Step 7: Optional — File Input

**Action:** If fetch fails, use "Choose JSON file" to load `brain-map-graph.json`.

**Verification:** Graph renders from file.

## Step 8: Optional — Accessibility Scan

**Action:** Start [BrowserStack Local](https://www.browserstack.com/docs/local-testing), then `startAccessibilityScan` with the **tunneled** URL BrowserStack provides (not raw `localhost` unless your setup maps it). Alternatively scan an HTTPS staging URL. Ensure BrowserStack MCP credentials are valid (401 = fix config).

**Accept when unavailable:** Manual/staging only. localhost is not reachable from BrowserStack cloud without tunnel; apply WCAG checklist manually when scan cannot run.

**Verification:** WCAG issues reported (or manual checklist applied).

**Manual checklist:** See [BRAIN_MAP_AUDIT.md](BRAIN_MAP_AUDIT.md) — **WCAG 2.1 AA — graph visualizations** when expert/scan is unavailable.

## Step 9: Optional — OpenGrimoire (portfolio-harness)

**Action:** With portfolio-harness dev server running (`npm run dev` in `OpenGrimoire`), open `http://localhost:3001/context-atlas` (or `/brain-map`). Next.js may use 3002/3003 if 3000/3001 are in use. Ensure `public/brain-map-graph.json` exists (run `python .cursor/scripts/build_brain_map.py` from portfolio-harness root).

**Verification:** Context graph loads or shows empty-state fallback. Schema reference: `OpenGrimoire/docs/BRAIN_MAP_SCHEMA.md` in portfolio-harness. Automated E2E: `OpenGrimoire/e2e/context-atlas.spec.ts`.

## Step 10: Stop Servers (after audit)

**Step 10a — Stop HTTP server:** If you started `python -m http.server` in Step 2, stop it (Ctrl+C in that terminal).

**Step 10b — Stop OpenGrimoire dev server:** If you started `npm run dev` in OpenGrimoire for Step 9, stop it (Ctrl+C in that terminal).

**Verification:** Servers stopped; ports released.

## Post-audit checklist

After completing an audit run:

- [ ] Update [BRAIN_MAP_AUDIT.md](BRAIN_MAP_AUDIT.md) Audit Findings row (date, component status, notes)
- [ ] Update critic JSON in Audit if revised
- [ ] Confirm BRAIN_MAP_E2E.md steps match execution; add any new steps

## MCP Tools Reference

| Tool | Server | Use |
|------|--------|-----|
| browser_navigate | Playwright / cursor-ide-browser | Open viewer URL |
| browser_snapshot | Same | Accessibility tree |
| browser_take_screenshot | Same | Visual evidence |
| browser_wait_for | Same | Wait for content |
| startAccessibilityScan | BrowserStack | WCAG scan (public URL) |
| accessibilityExpert | BrowserStack | A11y questions |
