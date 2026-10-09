# Operator diagrams (OpenHarness)

Self-contained **HTML** slides (open locally in a browser) plus **SVG** for GitHub / markdown embeds. Static HTML+SVG; no Mermaid deliverable; no secrets.

**Mode C (standalone):** plates live here. Craft/export uses a **vendor bridge** to MiscRepos’s pinned [diagram-design](https://github.com/cathrynlavery/diagram-design) skill (SHA in that repo’s `.cursor/skills/diagram-design/VENDOR.md`) — this tree does not vendor the full skill. Export:

```text
python <MiscRepos>/.cursor/skills/diagram-design/scripts/export_svg.py docs/diagrams/<name>.html docs/diagrams/<name>.svg
```

(from the OpenHarness repo root; adjust the MiscRepos path if your sibling layout differs)

Tokens: **mic-ghost** dark paper `#0e1114`, ink `#e6e8eb`, accent `#c4a574`. Density ~4/10; accent on 1–2 focal nodes; **static**. Deliverable is **HTML + SVG**, not Mermaid. Profile marker: repo-root `.diagram-design` → `profile: mic-ghost`.

Roll-out modes (A/B/C): [MiscRepos `docs/diagrams/ROLL_OUT.md`](../../MiscRepos/docs/diagrams/ROLL_OUT.md).

## Catalog

| File | Type | Why |
|------|------|-----|
| [hitl-connectivity.html](hitl-connectivity.html) · [svg](hitl-connectivity.svg) | Architecture | OpenHarness `async_tasks` / narrative handoff vs sibling orchestrator wake path; HITL tokens and channel reach the human |

Semantics companion: [ASYNC_HITL_SCOPE.md](../ASYNC_HITL_SCOPE.md). Cross-repo wiring detail: sibling MiscRepos `local-proto/docs/HITL_CONNECTIVITY.md`.
