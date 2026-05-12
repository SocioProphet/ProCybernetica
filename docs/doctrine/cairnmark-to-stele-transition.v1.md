# Cairnmark-to-Stele Transition Doctrine

**Status:** v1.0 doctrine. Specifies schema-level promotion rules.  
**Date:** May 12, 2026  
**Scope:** Defines the constitutional discipline that governs when a candidate artifact, or Cairnmark, becomes a promoted, signed, institutionally authorized artifact, or Stele. Applies to every artifact at Layer 2.5 or above: Masonmark proofpacks, M-series certificates, ProCybernetica safety cases, ProRepresentation encoder doctrine, Pneumachinalis contribution events at promotion time, and capability-tier invocations.

---

## 1. What this document is

This document specifies the transition discipline between Cairnmark and Stele states. It is the cross-cutting governance contract that ties together three architectural elements:

- the Adjudication Plane, Masonmark Layer 2.5;
- TritFabric Atlas, Layer 4;
- Pneumachinalis stake resolution, Layer 5.

These three decisions converge on a single artifact's `promotion_state`. This document specifies the rules that make convergence deterministic, auditable, and fail-closed.

The transition is constitutional. CI-4, the Cairnmark/Stele distinction, is the enabling invariant. This doctrine specifies the operational mechanics that make CI-4 enforceable.

---

## 2. Why this discipline matters

Without explicit Cairnmark/Stele discipline, candidate work and admitted work look identical at the schema level. A Cairnmark certificate and a Stele certificate may differ only by runtime status unless the promotion distinction is explicit. Downstream consumers cannot reliably distinguish them without out-of-band knowledge.

The Adjudication Plane also becomes optional if candidate artifacts can flow directly to Atlas without explicit sign-off. The verifier ensemble would degrade from gatekeeper to advisor. The Masonmark four-plane architecture requires Adjudication to be constitutional, not advisory.

Stake resolution also loses its lever. Pneumachinalis stake commitments are predicated on contributions reaching adjudicated outcomes. If contributions can be promoted without adjudication, stakes have nothing to resolve against and the reputation feedback loop breaks.

This doctrine prevents those failure modes by making the transition state machine explicit, the authority chain mandatory, and the rejection path symmetric with the promotion path.

---

## 3. State machine

Every artifact at Layer 2.5 or above carries a `promotion_state` field with one of four values:

```text
candidate -> promoted_stele -> superseded
    |             |
    v             v
rejected       superseded
    |
    v
superseded
```

### 3.1 State transitions

`candidate -> promoted_stele` requires Adjudication Plane sign-off, an institutional-truth signing authority chain, and any configured reputation-requirement satisfaction.

`candidate -> rejected` requires Adjudication Plane sign-off determining that the candidate fails the verifier ensemble or violates a constitutional invariant.

`candidate -> superseded` occurs when a later candidate addressing the same target supersedes the current one before adjudication completes.

`promoted_stele -> superseded` occurs when a later promoted Stele addressing the same target replaces the current one.

`rejected -> superseded` is a historical transition. A rejected candidate is conceptually frozen, but if the certificate authority later reissues with revised content, the original rejection may be marked superseded.

### 3.2 Terminal discipline

`promoted_stele` can only transition to `superseded` under ordinary operation.

`rejected` is terminal except for historical supersession.

There is no transition from `rejected` back to `candidate`. A rejected candidate must be issued as a new artifact with a new artifact ID and explicit lineage through `divergence_parent` or `supersedes`. Relitigation under the same ID is structurally forbidden.

---

## 4. Adjudication Plane sign-off contract

Every transition from `candidate` to `promoted_stele` or `rejected` requires explicit Adjudication Plane sign-off, captured in `reasoning_trace_ref`.

The `reasoning_trace_ref` must reference a Masonmark proofpack or equivalent reasoning artifact that includes:

- verifier ensemble results: grammar, type, policy, fixture pass scores;
- adjudication outcome: `admitted`, `partial`, `rejected`, or `undecided`;
- adjudication authority with at least `grounded_schema` authority layer;
- adjudication timestamp;
- follow-up specification for partial outcomes.

For M-series certificates, `reasoning_trace_ref` references the Masonmark proofpack whose specialization produced the certificate.

For ProCybernetica safety cases or other Layer 3 evidence artifacts, `reasoning_trace_ref` references the proofpack or equivalent reasoning artifact that produced the evidence claim.

---

## 5. Signing authority chain contract

Every transition from `candidate` to `promoted_stele` requires a signing authority chain whose root is `institutional_truth`.

### 5.1 Mandatory fields per signature

- `authority_id`
- `authority_kind`
- `authority_layer`
- `signed_at`
- `signing_method`
- `signature_value`

### 5.2 Chain composition rules

The chain root signature must have `authority_layer: institutional_truth`.

Intermediate signatures may have `authority_layer: grounded_schema` if they delegate from an institutional-truth root.

Signatures with `authority_layer: commonsense_prior` are not permitted in promotion chains.

The chain must satisfy CI-9 authority concentration bounds with `reputation_weighted_index <= 0.8`.

For jointly produced artifacts, all required parties appear in the chain and concentration is computed across the full chain.

---

## 6. Reputation requirement contract

Promotion to Stele may be gated by reputation requirements. When a reputation requirement is specified:

- the signing authority's reputation in the relevant role/domain cell is queried at promotion time;
- if reputation falls below the threshold, configured fallback applies;
- the reputation-check timestamp is recorded;
- reputation requirements operate as additional fail-closed gates;
- reputation can weaken or block a candidate claim, not strengthen it.

Reputation requirements are optional for Layer 3 evidence artifacts in v1.0. They are mandatory for capability-tier invocations and may become mandatory for specific certificate kinds in future doctrine versions.

---

## 7. Transition record

Every transition is captured by a transition record. Transition records are signed by the adjudication authority and the signing authority chain together.

Required transition-record structure:

```json
{
  "transition_kind": "cairnmark-to-stele",
  "transition_id": "transition-...",
  "ts_transitioned": "2026-05-12T00:00:00Z",
  "source_state": "candidate",
  "target_state": "promoted_stele",
  "subject_artifact_ref": {},
  "adjudication_proofpack_ref": {},
  "signing_authority_chain": [],
  "reputation_check_result": null,
  "supersedes_or_divergence_parent": null,
  "transition_authority_signature": "..."
}
```

The transition record is itself an artifact at Layer 2.5. It carries constitutional invariants, its own `promotion_state`, its own `authority_layer`, and its own `reasoning_trace_ref` pointing back to the adjudication proofpack.

---

## 8. Composition with the three constitutional flows

### 8.1 Adjudication Plane outcome to promotion state

| Adjudication outcome | promotion_state result |
|---|---|
| `admitted` | `candidate -> promoted_stele` |
| `partial` with follow-up | `candidate -> promoted_stele` with `followup_required` |
| `partial` with no follow-up | `candidate -> promoted_stele` with default curator review |
| `rejected` | `candidate -> rejected` |
| `undecided` | remains `candidate`; transition deferred |

Critical rule: `undecided` does not transition. Atlas treats undecided certificates as deny under CI-5 fail-closed. Reputation substrate does not award reputation for undecided contributions.

### 8.2 Atlas promotion usage

Atlas consumes only `promoted_stele` certificates.

| promotion_state at Atlas entry | Atlas action |
|---|---|
| `candidate` | deny |
| `promoted_stele` | proceed with verdict mapping |
| `rejected` | deny |
| `superseded` | deny; use successor |

Only `promoted_stele` can reach Atlas verdict-mapping logic.

### 8.3 Pneumachinalis stake resolution

| Transition outcome | Stake resolution |
|---|---|
| `candidate -> promoted_stele` | verified and returned with multiplier |
| `candidate -> rejected` | refuted destroyed or transferred to refuter |
| `candidate -> superseded` | expired returned |
| `promoted_stele -> superseded` | partial verification; doctrine-specific |

This closes the cybernetic feedback loop: contributions produce stakes, stakes resolve based on adjudication outcomes, resolutions update reputation, and reputation gates future stakes.

---

## 9. Edge cases and special rules

### 9.1 Capability-tier invocation transitions

When a Cairnmark-to-Stele transition invokes the quantum dependency substrate capability tier, the adjudication proofpack must include capability-tier-specific verifier scores. The signing authority chain must include at least one signer whose authorization scope covers the invoked capability-tier use case. F8.x observables apply continuously to the resulting Stele.

### 9.2 Promotion of Cairnmark composites

For composite artifacts, all referenced fragments must be in `promoted_stele` state before the composite can transition to `promoted_stele`.

A composite cannot be promoted while it references Cairnmark fragments.

If a referenced fragment is rejected after the composite is promoted, the composite transitions to `superseded` with a re-derivation plan.

### 9.3 Joint promotion under multi-party authority

When multiple authorities must sign jointly, all parties must complete adjudication before any party signs promotion. Sequential adjudication is permitted; serial sign-off is not.

### 9.4 Time-limited Steles

A Stele may carry `stele_expires_at`. Expiration causes automatic transition to `superseded` with no successor, forcing re-adjudication for continued use. Default: no expiration.

### 9.5 Emergency rejection

A promoted Stele may be reverted to rejected only through a glass-break governance procedure with capability-tier invocation, with cascade-authority sign-off equal to or exceeding original promotion authority. Emergency rejection produces a transition record and redaction-cascade record. Reputation effects from the original promotion are unwound under reputation doctrine.

---

## 10. What this doctrine does not commit to

The state machine is a starting specification. Additional states such as `under_review` or `pending_followup` may be introduced in v1.1 if adoption experience demonstrates need.

The reputation requirement contract is permissive in v1.0 and may tighten in future versions.

The transition record schema is structural. Full JSON Schema is a follow-on work item with fixture validation.

Edge cases are working specifications. Real-world adjudication may surface additional cases.

---

## 11. Transition-specific falsification observables

### F4.4: Transition records absent for promoted Steles

If any `promoted_stele` artifact exists without a corresponding transition record referencing it, the audit chain is incomplete.

Severity: S1.

### F4.5: Adjudication outcome inconsistent with promotion_state

If a Stele's `reasoning_trace_ref` references an adjudication proofpack with outcome other than `admitted` or `partial`, the transition rules were violated.

Severity: S1.

### F4.6: Cairnmark composite promoted with Cairnmark fragments

If a composite artifact is in `promoted_stele` state but any referenced fragment is still in `candidate` state, the composite-promotion rule is violated.

Severity: S1.

These additions bring the falsification doctrine from 20 observables to 23 observables, plus the existing three meta-observables.

---

## 12. Status

| Field | Status |
|---|---|
| Doctrine version | v1.0 |
| State machine | specified |
| Adjudication sign-off contract | specified |
| Signing authority chain contract | specified |
| Reputation requirement contract | optional in v1.0 |
| Transition record schema | structural specification; full schema pending |
| Edge cases | five edge cases specified |
| Falsification observables added | F4.4, F4.5, F4.6 |
| Constitutional invariant served | CI-4 primary; CI-3, CI-5, CI-8, CI-9 supporting |
| Composition flows | Adjudication Plane, Atlas, Pneumachinalis |

---

## 13. What this enables downstream

After this doctrine lands:

- v1.3 schema bump can add `authority_layer`, `promotion_state`, `reasoning_trace_ref`, and `cadence_classification` to every M-series schema;
- Atlas SHACL companion shapes can express the candidate-to-Stele fail-closed rule;
- Pneumachinalis stake-resolution receipts can reference transition records as authoritative outcomes;
- F4.1 through F4.6 become monitorable;
- the capability tier inherits transition discipline by reference.

---

## 14. Non-claims

This doctrine does not implement the full transition-record JSON Schema.

It does not claim all existing historical artifacts already carry v1.3 fields.

It does not require direct changes to Superconscious in this PR branch.

It defines the doctrine and additive-field target so downstream schema-owning repositories can adopt it deliberately.
