# Nogic workflow (harness)

How we use [Nogic](https://www.nogic.dev/) (graph view + optional MCP) alongside git, tests, and symbol search. This is **operating policy** for this harness, not a full product manual—see Nogic’s site for install, MCP, and privacy details.

**Canonical routing tables** (MCP map, integration audit) live in **portfolio-harness** at `.cursor/docs/MCP_CAPABILITY_MAP.md` and `.cursor/docs/CONTEXT_INTEGRATION_AUDIT.md` if you use that repo; this file stays in sync with the policy there.

---

## 1. Shape layer, not sole source of truth

Use the graph for **dependencies, hotspots, and “what touches what”** before large refactors or unfamiliar modules. **Correctness** still comes from **git history, tests, and human review**. The graph speeds navigation and questions like “who imports this?”—it does not replace execution evidence.

## 2. Index task-scoped repos

With many workspace roots, **index the repo(s) you are actually working on** for the current task so the graph and MCP answers stay relevant and fast. Prefer a **focused index** over everything-at-once unless your setup handles multi-root well and you need cross-repo edges.

## 3. Pair with refactor-reuse

**Refactor-reuse** means: find existing implementations, then **reuse / adapt / new** with rationale ([refactor-reuse SKILL](../skills/refactor-reuse/SKILL.md)).

- **Nogic:** strong for **coupling, call structure, and structural discovery** (edges, fan-in).
- **Still required:** `codebase_search`, `grep`, and **jCodeMunch** (`search_symbols`, `search_text`) to find **similar logic by name, behavior, or duplicate patterns**—not only graph neighbors.

## 4. Privacy and boundaries

If you enable **Nogic’s MCP** in Cursor, confirm **what leaves the machine** against current Nogic documentation and terms. For sensitive codebases, prefer **local-only** workflows and verify whether any **cloud sync** is disabled.

## 5. Language coverage

Nogic’s parsing stack emphasizes **Python, JavaScript, TypeScript, JSX/TSX**. **Other languages** (e.g. C++, Unreal assets, ad-hoc scripts) may be **partially or missing** from the graph—use normal search and file reads there.

---

## See also

- [CONTEXT_ENGINEERING.md](../../docs/CONTEXT_ENGINEERING.md) — retrieval routing, context budget
- [refactor-reuse SKILL](../skills/refactor-reuse/SKILL.md) — redundancy scan before new code
- portfolio-harness `.cursor/docs/MCP_CAPABILITY_MAP.md` — Nogic MCP row when enabled
- portfolio-harness `.cursor/docs/CONTEXT_INTEGRATION_AUDIT.md` — tool routing inventory
