# Decision log

Append entries below. Schema: Area | Decision | Rationale.

## 2026-03-20

- **[Research / Unpaywall]** Area: Scholarly OA discovery. Decision: **Skill-only** `research-open-access` under `.cursor/skills/research-open-access/` (procedure + `reference.md`); no MCP in harness. Rationale: repeatable HTTP + email param + provenance; optional MCP belongs in product repos if two consumers need it.
- **[Wellbeing / survival PDF corpus]** Area: Private copyrighted PDFs. Decision: Same as portfolio-harness — keep purchases **off-git**; SCP on extracted text only; canonical write-up in sibling `local-proto` docs `HUMAN_WELLBEING_CORPUS.md` and `SURVIVAL_MEDICAL_RAG_DISCLAIMER.md`. Rationale: harness parity; no PDFs in public harness repos.

## 2026-03-19

- **[Brain Map gap prioritization]** Area: Brain Map audit. Decision: Accept G9, G10 as known limitations; prioritize G1–G3, G6–G8 for closure. Rationale: Tool/process gaps block repeatability; a11y gaps are product backlog.
- **[OpenAtlas vs OpenHarness]** Area: Repo boundaries. Decision: OpenAtlas remains a portfolio-harness Next.js app, not nested in openharness; README documents relationship and `CURSOR_STATE_DIR` for brain-map ingest. Rationale: Keeps public harness portable per DELINEATION.md; graph is co-access from state markdown, not a full-repo crawl.
