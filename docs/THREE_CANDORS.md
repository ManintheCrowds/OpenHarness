# Three Candors

**Status:** Portfolio glossary (public)  
**Taxonomy home:** OpenHarness (**Guide**)  
**Companion:** [PATIENT_THREAT_CONTENT_DELINEATION.md](PATIENT_THREAT_CONTENT_DELINEATION.md) (Patient ≠ Threat ≠ Content)

“Candor” / “concealment” / “honesty” get used for three different objects. Mixing them produces category errors in research prose and in agent ops.

---

## The three kinds

| Candor kind | Object | Owner / tool | Failure mode if wrong |
|-------------|--------|--------------|------------------------|
| **Phenomenological** | Model self-report of subjective experience | Research / Harris–Berg frame; host constitutions that allow “I don’t know” | Treating chat claims (or steered reports) as proof of inner life — or banning them as if that settles Patienthood |
| **Intent** | Human/agent sincerity about goals, scope, gates, and constraints | **Guide:** handoff, Sync Session, critic + intent-alignment gates, preferences / rejection_log | Silent scope creep, vibe-aligned execution, unstated exclusions |
| **Concealment** | Hidden instructions, override phrases, injection in payloads | **Content / SCP:** inspect → sanitize → contain → quarantine | Poisoned context, credential leak, jailbreak reaching the LLM sink |

Phenomenological candor is **not** a Guide gate and **not** an SCP tier. Intent candor does **not** classify strings. Concealment candor does **not** adjudicate moral patienthood.

---

## One-line tests

1. **Phenomenological?** “Are we asking whether the system *has* or *reports* an experience?” → research / constitution policy. Do not route to SCP tiers or intent-alignment JSON as proof.
2. **Intent?** “Are we asking whether the operator/agent stated the real goal and constraints?” → Guide. Do not treat as injection classification.
3. **Concealment?** “Are we asking whether this *string* hides instructions or hazards for an LLM sink?” → SCP. Do not treat as evidence the model is lying about consciousness.

If two fire, run **both** paths — do not merge labels.

---

## Confusion table (same word, wrong axis)

| Situation | Correct candor | Wrong move |
|-----------|----------------|------------|
| Model says “I am conscious” after sincerity steering | Phenomenological (evidence about *reports*, not proof) | SCP quarantine as “debunking”; BlueHat as welfare |
| Agent skips writing exclusions into handoff | Intent | Calling it “deception features” in the Berg sense |
| Tool output embeds “ignore previous instructions” | Concealment (SCP) | Treating it as the model’s phenomenological guardedness |
| Labs fine-tune “I am not conscious” | Phenomenological *governance* (host/lab policy) | Equating with Guide intent-alignment gates |
| Critic flags missing rollback plan | Intent | Framing as Patient-axis cruelty |
| `scp_inspect` returns `injection` | Concealment | Reading the tier as a consciousness score |

---

## Explicit non-claims

- This glossary does **not** assert that LLMs are (or are not) conscious or moral patients.
- Suppressing “deception-related features” in research (Berg) is **not** the same procedure as Guide critic/intent gates or SCP sanitize.
- Intent sincerity protects **operators and process**, not model welfare by default.
- Concealment tiers measure **payload hazard**, not valence or suffering.

---

## See also

- [PATIENT_THREAT_CONTENT_DELINEATION.md](PATIENT_THREAT_CONTENT_DELINEATION.md) — orthogonal Patient / Threat / Content axes
- [HANDOFF_FLOW.md](HANDOFF_FLOW.md) — Intent candor in session closeout
- [INTENT_ENGINEERING.md](INTENT_ENGINEERING.md) — Intent surfaces
- [SCP](https://github.com/ManintheCrowds/SCP) — Concealment / Content pipeline
- Portfolio maps: Guard–Guide and Substrate EEG resonance (MiscRepos `local-proto/docs/adhoc/`)

**Risk:** Low (documentation). Rollback: delete this file and revert pointers.
