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

**Verification:** Server running on port 8080.

## Step 3: Navigate to Viewer

**Action:** Open `http://localhost:8080/brain_map_viewer.html`.

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

**Verification:** WCAG issues reported.

**Manual checklist:** See [BRAIN_MAP_AUDIT.md](BRAIN_MAP_AUDIT.md) — **WCAG 2.1 AA — graph visualizations** when expert/scan is unavailable.

## MCP Tools Reference

| Tool | Server | Use |
|------|--------|-----|
| browser_navigate | Playwright / cursor-ide-browser | Open viewer URL |
| browser_snapshot | Same | Accessibility tree |
| browser_take_screenshot | Same | Visual evidence |
| browser_wait_for | Same | Wait for content |
| startAccessibilityScan | BrowserStack | WCAG scan (public URL) |
| accessibilityExpert | BrowserStack | A11y questions |
