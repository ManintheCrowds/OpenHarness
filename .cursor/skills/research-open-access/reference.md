# Unpaywall API — quick reference (verify against official docs)

Official pages change; confirm details at [unpaywall.org/products/api](https://unpaywall.org/products/api) and [unpaywall.org/api/v2](https://unpaywall.org/api/v2).

## Base URL

`https://api.unpaywall.org/v2/`

## Required parameter

All calls: `email=` — a reachable contact (polite pool). Example env: `UNPAYWALL_EMAIL`.

## DOI object (GET)

**Pattern:**

```http
GET /v2/{doi}?email={email}
```

The `{doi}` path segment must be **URL-encoded** (e.g. `10.1038/nature12373` or encode `/` as `%2F` in longer DOIs).

**Example (PowerShell):**

```powershell
$doi = [uri]::EscapeDataString("10.1038/nature12373")
$email = $env:UNPAYWALL_EMAIL
Invoke-RestMethod -Uri "https://api.unpaywall.org/v2/$doi`?email=$email"
```

**Example (curl):**

```bash
curl -sS "https://api.unpaywall.org/v2/10.1038/nature12373?email=YOUR_EMAIL@example.com"
```

## Search (GET)

**Pattern (typical):**

```http
GET /v2/search?query={terms}&email={email}
```

Pagination and filters may exist — check current v2 docs for `page`, `is_oa`, etc.

## Response (high level)

The JSON **DOI object** commonly includes (names may vary slightly by record):

| Field | Meaning |
|--------|--------|
| `doi` | DOI string |
| `is_oa` | Boolean: any OA location known |
| `oa_status` | e.g. gold, green, hybrid, bronze, closed |
| `best_oa_location` | Object: preferred OA URL, license, version, `host_type` |
| `oa_locations` | Array of OA location objects |
| Title, year, journal — bibliographic metadata | |

**Interpretation:** `best_oa_location.url` is often a landing page; a PDF may be linked inside or in `url_for_pdf` when present. Always verify links before citing “PDF at X.”

## Rate limits

Daily/request limits are set by Unpaywall — **read the official API page** before automation. For large recurring jobs, use their **data feed** product instead of hammering the REST API.

## Related

- [Data format](https://unpaywall.org/data-format) — field semantics.
- Client libraries exist in the ecosystem (e.g. Python wrappers); this harness skill stays **API + HTTP**-agnostic.
