# Brain Map

Visualize agent cognition from session journals and handoffs. Nodes are markdown files; edges represent co-access (files referenced together in the same session).

## Purpose

- See which notes and artifacts are used together across sessions
- Identify clusters (core, memory, publishing, tools, skills)
- Trace session types (strategy, memory, publishing, infrastructure, research)

## Data Sources

| Source | Content |
|--------|---------|
| `state/daily/YYYY-MM-DD.md` | Session summaries; extract .md paths |
| `state/handoff_latest.md` | Paths / artifacts, notes_touched |
| `state/handoff_archive/*.md` | Same |
| `state/decision-log.md` | Referenced files |

Projects using `.cursor/state/` follow the same layout.

## Graph Schema

- **nodes:** `{ id, group, accessCount, path }`
- **edges:** `{ source, target, weight, sessionType, sessions }`
- **groups:** core, memory, publishing, tools, skills, general

## Environment Variables

| Variable | Purpose |
|----------|---------|
| `CURSOR_STATE_DIR` | Override state directory (default: `root/state` or `root/.cursor/state`) |
| `BRAIN_MAP_OUTPUT` | Override output path (default: `state_dir/brain-map-graph.json`) |

## How to Run

From project root (or Harness root):

```powershell
python scripts/build_brain_map.py
```

If your project uses `.cursor/scripts/`:

```powershell
python .cursor/scripts/build_brain_map.py
```

Output: `brain-map-graph.json` in the state directory (or `BRAIN_MAP_OUTPUT`).

## How to View

### Standalone HTML (no Next.js)

1. Put `brain-map-graph.json` next to `brain_map_viewer.html` (e.g. run parser with `BRAIN_MAP_OUTPUT=scripts/brain-map-graph.json`, or copy from `state/`).
2. Serve the directory:
   ```powershell
   cd scripts
   python -m http.server 8080
   ```
3. Open `http://localhost:8080/brain_map_viewer.html`.

Alternatively, use the file input in the viewer to load a JSON file directly (works without a server).

### Next.js / OpenAtlas (folder `OpenAtlas`)

In **portfolio-harness**, the **OpenAtlas** app (folder `OpenAtlas`) serves the graph via `GET /api/brain-map/graph` and the D3 viewer at **`/context-atlas`** (canonical) or **`/brain-map`** (legacy alias). Set `BRAIN_MAP_OUTPUT` to `OpenAtlas/public/brain-map-graph.json` and run the parser before viewing. JSON schema (optional fields, API notes): see portfolio-harness `OpenAtlas/docs/BRAIN_MAP_SCHEMA.md` when that repo is checked out beside OpenHarness. The GitHub remote may still be named `Med-Vis` until the repo is renamed.

## One-Command Audit Flow (Standalone)

For a full visual audit with standalone viewer:

```powershell
$env:BRAIN_MAP_OUTPUT="D:\openharness\scripts\brain-map-graph.json"; python scripts/build_brain_map.py
cd scripts; python -m http.server 8080
```

Then open `http://localhost:8080/brain_map_viewer.html`. See [docs/BRAIN_MAP_AUDIT.md](BRAIN_MAP_AUDIT.md) and [docs/BRAIN_MAP_E2E.md](BRAIN_MAP_E2E.md).

## Skill and Rules

- **Skill:** [brain-map-visualization](../.cursor/skills/brain-map-visualization/SKILL.md) — triggers on "brain map", "cognition visualization", "session journal graph"
- **Rule:** [capability-summary](../.cursor/rules/capability-summary.mdc) — lists `build_brain_map` and `brain_map_viewer.html`
