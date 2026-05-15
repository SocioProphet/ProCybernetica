# Decision: Adopt Human Protection Layer v0 Profile

Status: accepted v0.1  
Issue: #30  
Decision scope: doctrine/profile reconciliation only  
Runtime claim: none

## Context

The Human Protection Layer draft defines the protection boundary for systems that can measure, model, infer about, represent, rank, target, persuade, experiment on, or materially affect a person or population.

The draft must be reconciled before final schemas or runtime implementation because HPL vocabulary touches lifecycle status, promotion status, evidence tier, consent, privacy, redress, review, trust surface, and downstream execution surfaces.

## Decision

Adopt HPL as a v0 ProCybernetica profile and doctrine surface.

The controlling documents are:

```text
docs/reconciliation/HUMAN_PROTECTION_LAYER.md
docs/reconciliation/HUMAN_PROTECTION_LAYER_RECONCILIATION_STATUS.md
```

HPL v0 adopts:

- the seven protection gates;
- the HPL status vocabulary;
- the E0-E7 evidence-tier vocabulary;
- the technical-status versus policy-status separation;
- the principle that validity is not permission;
- the public-first publication boundary;
- candidate envelope names for future schema work.

## Canonical envelope candidates

The accepted candidate envelope names are:

- `hpl_consent_envelope.v0`
- `hpl_privacy_minimization_envelope.v0`
- `hpl_evidence_tier_envelope.v0`
- `hpl_status_envelope.v0`
- `hpl_redress_envelope.v0`
- `hpl_review_outcome_envelope.v0`
- `hpl_trust_surface_envelope.v0`

These are candidate names, not final JSON Schemas.

## Downstream adoption requirement

Downstream surfaces must preserve the HPL policy boundary:

- Human Digital Twin / HolographMe must preserve consent, export, minimization, and appeal semantics.
- GAIA World Model must attach affected-population review before world-action recommendations or action templates.
- Superconscious may propose plans but must not authorize human-impacting side effects.
- AgentPlane must reference HPL policy status before tool grants, action dispatch, or subagent delegation when protected persons may be affected.
- Policy Fabric must enforce deny-by-default for human actuation, hidden persuasion, missing consent, unsupported mechanism claims, and missing authority.
- SourceOS / SociOS must preserve local/private raw evidence boundaries and trust-surface metadata before host, browser, terminal, network, or memory mutation.

## Consequences

HPL status values must not be collapsed into generic lifecycle states, promotion decisions, proof-pack dispositions, AgentPlane runtime status, or certificate promotion state.

Evidence tier must not be treated as permission. Human-contact or world-impacting action requires separate policy decision even at high evidence tier.

Future schema work should start from the candidate envelopes and conformance test plan, not from ad hoc field names.

## Non-goals

This decision does not freeze final JSON Schemas, implement runtime policy services, authorize human actuation, publish private human evidence, adjudicate consent, or change downstream runtime ownership.
