# Contributing to OpenHarness

Portable harness: docs, rules, skills, `state/`, and `scripts/`. There is **no product GUI** in this repo; see [docs/HARNESS_AUDIT_ALIGNMENT.md](docs/HARNESS_AUDIT_ALIGNMENT.md) Part B row 6 and [docs/AGENT_NATIVE_CHECKLIST.md](docs/AGENT_NATIVE_CHECKLIST.md) for agent-native expectations.

## Mechanical checks

From the repository root (Python 3.9+):

```bash
pip install PyYAML
python scripts/verify_script_index.py
python scripts/verify_skills_readme.py
```

- **`verify_script_index.py`** — On-disk script basenames under `scripts/` match [capabilities.harness.yaml](capabilities.harness.yaml) `harness_capability.scripts` and appear in backticks in [docs/CHEATSHEET.md](docs/CHEATSHEET.md) (Agent invocation index).
- **`verify_skills_readme.py`** — [.cursor/skills/README.md](.cursor/skills/README.md) rows match each skill folder’s `SKILL.md` `description:` front matter.

**Optional (sibling layout):** If **portfolio-harness** is cloned next to this repo, you can verify cross-repo markdown links:

```bash
python scripts/check_docs_portfolio_links.py
```

That script is **not** run in default CI (it fails without the sibling checkout).

**Pre-commit:** See [README.md](README.md) for `pre-commit` hooks that run the verifiers when configured.

## CI (GitHub Actions)

If [.github/workflows/ci.yml](.github/workflows/ci.yml) is enabled, it runs **`verify_script_index.py`** and **`verify_skills_readme.py`** only. That covers **inventory and README sync**, not natural-language semantic parity. Treat green CI as necessary, not sufficient, for agent-native readiness.

## Semantic smoke (agent NL parity)

The checklist requires at least **one natural-language** check per release area so mechanical tests are not the only proof ([docs/AGENT_NATIVE_CHECKLIST.md](docs/AGENT_NATIVE_CHECKLIST.md)). Use a **human or an agent** with `run_terminal_cmd` (or equivalent); paste brief evidence in the PR when practical.

**After changing scripts, CHEATSHEET index, or `capabilities.harness.yaml`:**

1. **Prompt (example):** “From the OpenHarness repo root, run `python scripts/verify_script_index.py`. Report exit code; if non-zero, paste stderr.”
2. **Expected:** Exit code `0`.

**After adding or renaming skills or editing `.cursor/skills/README.md`:**

1. **Prompt (example):** “From the OpenHarness repo root, run `python scripts/verify_skills_readme.py`. Report exit code; if non-zero, paste stderr.”
2. **Expected:** Exit code `0`.

**Optional broader discovery check:**

1. **Prompt (example):** “Run `python scripts/list_capabilities.py` and confirm the printed JSON includes a `scripts` array whose entries match what you expect from the manifest.”
2. **Expected:** Valid JSON, `scripts` present, consistent with [capabilities.harness.yaml](capabilities.harness.yaml).

This is **process evidence** (proves an agent—or you—can execute the documented path end-to-end). It does not replace the Python verifiers or pre-commit.

## Related docs

- [docs/AGENT_NATIVE_CHECKLIST.md](docs/AGENT_NATIVE_CHECKLIST.md)
- [docs/CHEATSHEET.md](docs/CHEATSHEET.md)
- [docs/BACKLOG.md](docs/BACKLOG.md) — optional future work (e.g. thin MCP over allowlisted scripts)
