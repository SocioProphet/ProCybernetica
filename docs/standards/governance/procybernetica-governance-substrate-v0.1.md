# ProCybernetica Governance Substrate Standard v0.1

Status: Draft standard.

## Purpose

This standard defines the governance-attestation substrate slice:

```math
\mathfrak W_{\mathrm{gov}}\hookrightarrow\mathfrak W.
```

The slice contains spheres, tokens, policies, attestations, and retention controls.

## Full substrate reference

```math
\mathfrak W=(\mathcal S_{\mathrm{dur}},\mathcal S_{\mathrm{act}},\Theta,\mathcal T,\mathcal C,\Pi,\mathcal E).
```

## Governance-attestation slice

```math
\mathfrak W_{\mathrm{gov}}=(\mathcal S_{\mathrm{spheres}},\mathcal T_{\mathrm{tokens}},\mathcal P_{\mathrm{policy}},\mathcal A_{\mathrm{attest}},\mathcal R_{\mathrm{retain}}).
```

## Component embeddings

| Component | Embedding | Meaning |
|---|---|---|
| `S_spheres` | `S_spheres subset S_dur` | Durable governance partitions and scopes |
| `T_tokens` | `T_tokens subset Pi cap C` | Tokens carry both projection scope and admissibility certification |
| `P_policy` | `P_policy subset C` | Policies define constraints |
| `A_attest` | `A_attest subset E` | Attestations are evidence objects |
| `R_retain` | `R_retain subset Theta times C` | Retention is temporal and policy-constrained |

## Axiom GOV-TOKEN-INTERSECTION-v0.1

```math
\mathcal T_{\mathrm{tokens}}\subseteq\Pi\cap\mathcal C.
```

A token is valid only if it declares both a projection role and an admissibility role. The JSON Schema `schemas/procybernetica/governance-substrate.v0.1.schema.json` enforces this invariant.

## Operating rule of five

Every governance-touching change must answer:

1. Which object of `W_gov` does it modify?
2. Which policy object in `Pol` governs it?
3. What is its vertical component?
4. What is its cartesian or reindexing component?
5. Which evidence cocone receives its trace?

For this substrate standard, questions 3 through 5 are deferred to the governance-fibration, deterministic-cleavage, factorization, and evidence-cocone standards.
