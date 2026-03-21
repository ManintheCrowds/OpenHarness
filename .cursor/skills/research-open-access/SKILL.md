---
name: research-open-access
description: Find legal open-access locations and metadata for scholarly works using the Unpaywall API (DOI lookup and search). Use when resolving DOIs, finding OA PDFs or landing pages, or interpreting OA status, license, and version.
triggers_any: ["open access", "Unpaywall", "DOI", "OA PDF", "preprint", "VoR", "green OA", "gold OA", "find free paper", "scholarly metadata"]
do_not_trigger_if: ["paywall bypass", "Sci-Hub", "pirate", "DRM crack"]
exclusive_with: []
required_inputs: ["contact email for API (or env UNPAYWALL_EMAIL / user-provided mailto)", "DOI and/or search query"]
forbidden_actions: ["frame Unpaywall as circumventing publisher paywalls", "omit email parameter on API requests", "use for non-OA scraping where API does not apply"]
exit_criteria: "User has OA locations/metadata from API response or a clear not-found / closed path; provenance (DOI + Unpaywall) stated when feeding downstream."
output_schema: "Structured summary of best OA location(s), license, is_oa; optional raw JSON citation; link to official API docs."
---

# Research: open access via Unpaywall (skill-only)

**Intent:** Repeatable, **legal open-access discovery** — not paywall circumvention. [Unpaywall](https://unpaywall.org/) indexes OA locations; the public API returns metadata and URLs where OA copies exist.

## When to use

- Resolve a **DOI** to OA status and **best OA URL** (landing page or PDF when available).
- **Search** by keywords when the user does not have a DOI.
- Interpret **license**, **version** (e.g. submitted / accepted / published), and **`is_oa`** for literature review or citations.

## When not to use

- Requests to bypass paywalls without an OA copy — outside this skill’s scope.
- Bulk harvesting against API etiquette; prefer batch [data feed](https://unpaywall.org/products/data) for large offline corpora (see reference).

## Prerequisites

1. **Email query parameter** — Unpaywall requires `email=` on requests (polite pool). Use:
   - `UNPAYWALL_EMAIL` from the environment if present, or
   - A contact email the user approves for this purpose (never invent an email).
2. **HTTPS only** — `https://api.unpaywall.org/...`

## Procedure

### A. DOI lookup

1. Normalize the DOI: strip `doi:`, `https://doi.org/`, whitespace; accept form like `10.xxxx/...`.
2. **URL-encode** the DOI for the path segment (slashes → `%2F`).
3. Request: `GET https://api.unpaywall.org/v2/{encoded_doi}?email={encoded_email}`
4. Parse JSON (see **reference.md** for response fields). Summarize:
   - `is_oa`, `oa_status` (e.g. gold, green, hybrid, bronze)
   - `best_oa_location` (URL, license, version, host_type) when present
   - Do **not** promise the PDF always works; hosts change.

### B. Search (optional)

1. `GET https://api.unpaywall.org/v2/search?query={query}&email={email}` (add pagination params per current docs if needed).
2. Present results as a short list with DOIs and titles; offer to resolve specific DOIs via (A).

### C. Provenance for downstream use

When summaries, RAG, or handoffs consume this data, record at minimum:

- **DOI**, **source: Unpaywall API**, and **date accessed** (or API response timestamp if present).

## Agent-native note

- **Primitives:** One lookup per DOI; compose with the user’s workflow (summarize, fetch PDF in browser, cite).
- **No dedicated MCP required** — use terminal `curl`/HTTP or IDE fetch tools with env email; keep logic in prompts + this skill.

## Errors and limits

- **429 / rate limiting:** Back off; do not retry in a tight loop. Check [official API documentation](https://unpaywall.org/products/api) for current limits.
- **404 / empty:** Treat as “no record” or closed OA; do not fabricate OA links.

## References

- **Field details and examples:** [reference.md](./reference.md) in this folder.
- **Official:** [Unpaywall API](https://unpaywall.org/products/api), [API v2](https://unpaywall.org/api/v2), [data format](https://unpaywall.org/data-format).

## Checks

- [ ] Every request includes `email=`.
- [ ] User understands output is **OA discovery**, not guaranteed full text.
- [ ] Downstream use includes DOI + Unpaywall provenance when it matters.

## Guardrails

- **Terms:** Follow Unpaywall’s current terms and citation guidance on their site.
- **Privacy:** Do not log or paste the user’s email into public artifacts unnecessarily; prefer env vars in automation.
- **Accuracy:** If the API returns `is_oa: false`, state that clearly; optional OA may still exist outside Unpaywall’s index.
