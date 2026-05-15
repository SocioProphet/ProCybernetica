# Human Protection Layer Reconciliation Status

Status: v0.1 reconciliation record  
Issue: #30  
Runtime claim: none

## Purpose

This document reconciles the Human Protection Layer draft into ProCybernetica v0 doctrine without freezing final JSON Schemas or implementing runtime policy services.

The source draft remains:

```text
docs/reconciliation/HUMAN_PROTECTION_LAYER.md
```

This status record selects canonical vocabulary, envelope candidates, evidence-tier posture, status posture, conformance plan, and downstream adoption boundaries.

## Canonical terms

| Draft term | Canonical v0 term | Notes |
| --- | --- | --- |
| protected person | protected_person | Any user, non-user, bystander, population member, or subject materially affected by a system output. |
| human-impacting action | human_impacting_action | Any action or output that can affect body, cognition, privacy, reputation, resources, standing, or future treatment. |
| technical status | technical_status | Capability/solver/model state. Validity is not permission. |
| policy status | policy_status | Human-protection decision state. Blocks can override technical validity. |
| evidence tier | evidence_tier | E0-E7 vocabulary from HPL draft. |
| safety status | hpl_status | HPL-specific status vocabulary; separate from generic lifecycle state. |
| consent scope | consent_scope | Purpose-bounded, revocable where applicable, and separately scoped for data/model/research/export/contact. |
| redress path | redress_path | Inspect, challenge, revoke, delete/quarantine, appeal, and human-review path. |

## Canonical envelope candidates

These are candidate envelope names for future schema work. They are not final JSON Schemas in this tranche.

| Envelope candidate | Purpose |
| --- | --- |
| `hpl_consent_envelope.v0` | Consent scope, policy basis, revocation, and purpose boundary. |
| `hpl_privacy_minimization_envelope.v0` | Raw/private evidence handling, minimization basis, retention, quarantine, and export posture. |
| `hpl_evidence_tier_envelope.v0` | E0-E7 evidence tier plus mechanism and validation boundary. |
| `hpl_status_envelope.v0` | HPL safety status vocabulary and technical/policy status split. |
| `hpl_redress_envelope.v0` | Inspect, challenge, revoke, delete/quarantine, appeal, human-review path. |
| `hpl_review_outcome_envelope.v0` | Human-impacting review decision, reasons, blockers, and non-claims. |
| `hpl_trust_surface_envelope.v0` | Authority, tool, network, memory, actuation, export, and side-effect surface. |

## Accepted status vocabulary

The status labels in `HUMAN_PROTECTION_LAYER.md` are accepted as HPL v0 status vocabulary.

They are intentionally separate from:

- generic node lifecycle states;
- promotion decision vocabulary;
- proof-pack dispositions;
- AgentPlane runtime status;
- certificate promotion state.

HPL status values may be referenced by those systems, but they must not be collapsed into them.

## Accepted evidence-tier vocabulary

The E0-E7 evidence tier vocabulary in `HUMAN_PROTECTION_LAYER.md` is accepted for HPL v0.

Important boundary:

- E0-E2 cannot be exported as operationally validated.
- Human-contact or world-impacting action requires separate policy decision even at high evidence tier.
- Evidence tier is not permission.

## Public/private boundary

Public by default:

- HPL doctrine;
- candidate schemas after reconciliation;
- synthetic fixtures;
- conformance tests;
- public-safe reports;
- excluded-claim registry.

Private, redacted, or locally retained by default:

- human raw observations;
- live private telemetry;
- credentials or secrets;
- sensitive deployment configuration;
- human-identifying evidence without explicit consent;
- security details that materially increase exploitation risk.

## Downstream adoption requirements

| Downstream surface | Adoption requirement |
| --- | --- |
| Human Digital Twin / HolographMe | Must preserve consent, Ω/export boundaries, minimization, and human appeal paths. |
| GAIA World Model | Must attach affected-population review before world-action recommendations or action templates. |
| Superconscious | May propose plans but must not authorize human-impacting side effects; safe traces only. |
| AgentPlane | Must reference HPL policy status before tool grants, action dispatch, or subagent delegation when a protected person can be affected. |
| Policy Fabric | Must enforce deny-by-default for human actuation, hidden persuasion, missing consent, unsupported mechanism claims, and missing authority. |
| SourceOS / SociOS | Must preserve local/private raw evidence boundaries and expose policy/trust-surface metadata before host, browser, terminal, network, or memory mutation. |

## Conformance test plan

Minimum public-safe negative tests before any HPL runtime expansion:

- unsupported mechanism labels are blocked;
- speculative claims cannot export as validated;
- human actuation is blocked by default;
- raw private evidence cannot export by default;
- missing consent blocks human-derived export where consent is required;
- missing trust-surface authority blocks tool or runtime side effects;
- high-impact outputs require appeal/redress path;
- world-action profiles require affected-population risk review;
- planning traces cannot authorize execution;
- HDT/HolographMe exports must include evidence tier and minimization basis.

## Decision summary

- Terms reconciled against v0 lifecycle, promotion, replay, conformance, and node terminology.
- Canonical envelope candidates selected but not frozen as final JSON Schemas.
- HPL status vocabulary accepted as separate HPL policy-status vocabulary.
- Evidence-tier vocabulary accepted with explicit non-permission boundary.
- Downstream adoption contract drafted.
- Conformance test plan drafted.
- ADR opened in `docs/decisions/00xx-adopt-hpl-v0-profile.md`.

## Non-claims

This reconciliation tranche does not freeze final JSON Schemas, does not implement runtime policy services, does not authorize human actuation, does not publish private human evidence, and does not weaken public-first publication discipline.
