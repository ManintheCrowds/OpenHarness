# Authority Model

Domain-agnostic framework for gating high-stakes agent actions. Any agent workflow needs a way to distinguish when social approval suffices vs when cryptographic proof is required.

---

## Definitions

### Cryptographic authority

Proof-based, verifiable authority. Private key = proof of ownership; signed actions; capability tokens. Verification is deterministic: anyone can verify a signature or proof without trusting a third party.

### Social/coordination authority

Consensus, reputation, human gates. Identity may be cryptographic but routing and coordination decisions are not proof-based. Verification relies on gossip, reputation, or human approval.

### Pseudoanonymous authority

Authority is provable without revealing real-world identity. Use pubkeys and capability tokens; no PII in verification. Enables audit and delegation without identity disclosure.

---

## When each applies

- **Low-stakes coordination:** Social/coordination authority acceptable. Examples: reversible coordination, documentation, design decisions. Failure modes bounded; no spend, no PII.
- **High-stakes actions:** Cryptographic authority required. Examples: spend, PII access, irreversible actions. Failure modes include theft, harm, or permanent loss.

---

## Authority by risk tier

Aligns with Risk-Tiered Operations:

| Risk Tier | Authority Model | Rationale |
|-----------|-----------------|-----------|
| **Low** | Social/coordination OK | Reversible; no spend, no PII; e.g. coordination, docs |
| **Medium** | Human gate + signed identity | Git tag + backup; two reviewers; identity verified |
| **High** | Cryptographic proof required | Full backup; lead approval; capability tokens, signed actions |
| **Critical** | Full proof chain | Multiple backups; team consensus; capability verification |

**Risk-tier definitions:**

- Low: Git commit, single reviewer
- Medium: Git tag + backup, two reviewers
- High: Full backup + lead approval
- Critical: Multiple backups + team consensus

---

## Capability token concept

For High/Critical tiers, capability tokens provide cryptographic proof of authorization:

- **Issue:** Authority issuer creates token with scope, expiry, holder identity (pubkey)
- **Verify:** Before action, verify token authorizes the action; check scope, expiry, revocation
- **Revoke:** Authority can revoke token; subsequent verification fails

Implementation is project-specific. Harness provides the pattern; your stack (e.g. BFT consensus, on-chain, HSM) provides the implementation.

### Capability token lifecycle

1. **Request:** Agent or human requests capability with pubkey (identity).
2. **Issue:** Authority creates token with scope, expiry, holder.
3. **Present:** Before action, agent presents token.
4. **Verify:** Check scope, expiry, revocation; return true/false.
5. **Revoke:** Authority can revoke; subsequent verify returns false.

### Verification contract

- **Signature:** `verify_capability(token, action_descriptor) -> bool`
- **When:** Call before High/Critical tier actions.
- **If false:** Escalate to human; do not proceed.

---

## Integration

- **Hard boundaries:** Use org-intent or equivalent to define when cryptographic proof is required (e.g. "Do not act on behalf of non-owner without cryptographic proof").
- **Capability verification:** Before High/Critical tier actions, call your `verify_capability(token, action_descriptor)` or equivalent. If verification fails, escalate to human.
- **Agent identity:** Agent identity = pubkey (no PII). Private key stored outside AI access. Used for: audit, capability requests, verifiable "authorized by X".

---

## Optional: Crypto integration patterns

If your stack uses proof-based identity (e.g. secp256k1, Ed25519), agent identity = pubkey; private key outside AI access. For agent spend, prefer open payment rails; capability tokens can gate spend actions. See reference implementations for domain-specific examples.

---

## See also

- [DELINEATION.md](DELINEATION.md) — harness vs portfolio
- [HARNESS_ARCHITECTURE.md](HARNESS_ARCHITECTURE.md) — Guard–Guide–Build taxonomy
