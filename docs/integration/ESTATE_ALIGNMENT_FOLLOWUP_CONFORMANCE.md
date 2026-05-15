# Estate Alignment Follow-Up Conformance

Status: v0.1 conformance note  
Issues: #15, #16, #17  
Runtime claim: none

## Purpose

This document closes the shallow estate-alignment follow-up work for Ontogenesis, Foundry/model-governance, and workstation/operator surfaces after the first-pass maps landed.

The controlling maps are:

- `docs/integration/ontogenesis-governance-map.md`
- `docs/integration/foundry-model-governance-map.md`
- `docs/integration/workstation-operator-surface-map.md`

The public-synthetic fixture bundle is:

```text
tests/fixtures/estate-alignment/estate-alignment-followups.synthetic.json
```

The executable validator is:

```text
tools/cybernetic_governance/validate_estate_alignment_followups.py
```

## #15 — Ontogenesis governance follow-ups

Implemented follow-ups:

- ontogenesis adapter fixture added;
- validated claim fixture includes ontology refs;
- validated claim fixture includes SHACL/ledger/signature validation evidence;
- ProCybernetica references Ontogenesis artifacts instead of duplicating ontology, SHACL, ledger, signature, SBOM, SHIR, or module schemas.

Conformance rule:

```text
validated semantic claims must carry ontology_ref and validation evidence refs
```

## #16 — Foundry and model-governance follow-ups

Implemented follow-ups:

- Foundry/model-governance adapter fixture added;
- Foundry maturity and model-route evidence are represented as public score slices;
- EvaluationResult and PromotionDecision examples can cite functional-model-surfaces, model-router, model-governance-ledger, guardrail-fabric, and SourceOS model-carry surfaces.

Conformance rule:

```text
model-governance evidence rows must cite external owning surfaces rather than redefining model lifecycle, routing, guardrail, or carry schemas
```

## #17 — Workstation/operator surface follow-ups

Implemented follow-ups:

- operator/workstation adapter fixture added;
- public conformance plan includes operator/gateway surface invariants;
- dashboards are treated as operator review surfaces;
- CommandEnvelope and CapabilityDescriptor examples can reference upstream operator surfaces without owning terminal, browser, workstation, ChatOps, shell, or UI runtime schemas.

Conformance rule:

```text
operator/gateway surfaces must preserve identity, scope, policy refs, evidence refs, replay/receipt path, approval posture, and public-safe projection
```

## Shared scoring/dashboard posture

Public score slices may reference:

- ontology / SHACL validation evidence;
- Foundry maturity evidence;
- model-route evidence;
- operator review surface evidence;
- dashboard surface projection evidence.

Public score slices must not claim ownership over Ontogenesis, model-governance, router, guardrail, SourceOS, workstation, terminal, browser, or UI runtime schemas.

## Non-claims

This tranche does not implement Ontogenesis validation, Foundry/model-governance runtime, model routing, guardrail runtime, SourceOS model carry, AgentPlane runtime, terminal runtime, browser runtime, workstation runner, dashboard runtime, or UI implementation. It records public-synthetic adapter fixtures and conformance expectations only.
