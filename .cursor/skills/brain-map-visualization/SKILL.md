---
name: brain-map-visualization
description: Load when task involves brain map, cognition visualization, session journal graph, or visualizing handoff/note co-access. Runs parser and guides user to viewer.
triggers_any: ["brain map", "cognition visualization", "session journal graph", "visualize handoffs", "note co-access graph", "brain-map"]
do_not_trigger_if: ["only run tests", "only verify behavior"]
exclusive_with: []
required_inputs: []
forbidden_actions: []
exit_criteria: "Parser run; user directed to brain-map-graph.json and viewer."
output_schema: "Graph JSON path; viewer instructions (standalone HTML or Next.js)."
---

# Brain Map visualization role

**Intent:** Build and visualize the agent cognition graph from session journals and handoffs. Nodes = markdown files; edges = co-access (files referenced together).

## When to use

- User asks for brain map, cognition visualization, session journal graph.
- User wants to visualize handoffs or note co-access.
- Task involves understanding which notes/artifacts are used together across sessions.

## Inputs

- Project root (Harness root or project using Harness state schema).
- Optional: `CURSOR_STATE_DIR`, `BRAIN_MAP_OUTPUT` if user has custom paths.

## Steps

1. **Run parser:** `python scripts/build_brain_map.py` from project root. If project uses `.cursor/scripts/`, use `python .cursor/scripts/build_brain_map.py`.
2. **Locate output:** `brain-map-graph.json` in state dir (or `BRAIN_MAP_OUTPUT`).
3. **Viewer options:**
   - **Standalone:** Copy JSON to same dir as `scripts/brain_map_viewer.html`; run `python -m http.server 8080` in that dir; open `http://localhost:8080/brain_map_viewer.html`. Or use file input in viewer to load JSON directly.
   - **Next.js/Med-Vis:** If project has Med-Vis, set `BRAIN_MAP_OUTPUT` to `Med-Vis/public/brain-map-graph.json` and view at `/brain-map`.

## Checks

- Parser completed without error.
- JSON exists at expected path.
- User knows how to open the viewer.

## For visual audit

Load browser-web skill; use Playwright MCP or cursor-ide-browser; run accessibility scan (if public URL); produce critic report per critic-loop-gate. See [docs/BRAIN_MAP_AUDIT.md](../../../docs/BRAIN_MAP_AUDIT.md) and [docs/BRAIN_MAP_E2E.md](../../../docs/BRAIN_MAP_E2E.md).

## References

- [docs/BRAIN_MAP.md](../../../docs/BRAIN_MAP.md) — Purpose, schema, env vars, usage
- [scripts/build_brain_map.py](../../../scripts/build_brain_map.py) — Parser
- [scripts/brain_map_viewer.html](../../../scripts/brain_map_viewer.html) — Standalone vis-network viewer
