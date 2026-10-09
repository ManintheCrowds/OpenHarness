# Operator diagrams (OpenHarness)

Self-contained **HTML** slides (open in a browser) plus **SVG** exports for GitHub / markdown embeds. No build step; HTML is static (no JavaScript).

**Mode A — harness-linked:** Craft rules and export tooling live in sibling **MiscRepos** [diagram-design](../../MiscRepos/.cursor/skills/diagram-design/SKILL.md) ([VENDOR.md](../../MiscRepos/.cursor/skills/diagram-design/VENDOR.md) pin). This folder holds OpenHarness-scoped plates only — do not vendor the full skill tree here.

**GitHub note:** clicking an `.html` file in the repo UI shows source, not a rendered page. Use the `.svg` next to featured plates (or open HTML locally). Export with:

```text
python ../MiscRepos/.cursor/skills/diagram-design/scripts/export_svg.py docs/diagrams/<name>.html docs/diagrams/<name>.svg
```

(from the OpenHarness repo root; adjust the MiscRepos path if your sibling layout differs)

Style: **dark** paper (`#2d3142`), ink `#f5f5f5`, accent `#f08a59`; density ~4/10; accent on 1–2 focal nodes; **static**. Deliverable is **HTML + SVG**, not Mermaid.

Roll-out modes (A/B/C): [MiscRepos `docs/diagrams/ROLL_OUT.md`](../../MiscRepos/docs/diagrams/ROLL_OUT.md).

## Catalog

| File | Type | Why |
|------|------|-----|
| [hitl-connectivity.html](hitl-connectivity.html) · [svg](hitl-connectivity.svg) | Architecture | OpenHarness `async_tasks` / narrative handoff vs sibling orchestrator wake path; HITL tokens and channel reach the human |

Semantics companion: [ASYNC_HITL_SCOPE.md](../ASYNC_HITL_SCOPE.md). Cross-repo wiring detail: sibling MiscRepos `local-proto/docs/HITL_CONNECTIVITY.md`.
