# Bridge Schemas v1 Execution Plan

Status: v0.1 implementation plan  
Issue: #43  
Runtime claim: none

## Purpose

This plan defines the bridge-schema tranche for connecting OpsHistory, Masonmark, certificate-state, and Atlas admission surfaces without mutating the certificate-family schemas.

## Bridge schemas

This tranche owns three additive bridge schemas:

```text
schemas/bridges/ops-history-to-pneumachinalis.v1.json
schemas/bridges/masonmark-to-certificate.v1.json
schemas/bridges/certificate-to-atlas.v1.json
```

## Bridge fixtures

The public-synthetic fixture lane covers:

- OpsHistory machine actor to Pneumachinalis microbeat;
- Masonmark proofpack to M2 Pattern A certificate;
- M2 Pattern A certificate to Atlas admit;
- undecided certificate to Atlas deny fail-closed;
- human actor mapped to reputation microbeat without required consent evidence;
- candidate proofpack mapped to promoted Stele certificate.

## Cross-field validator rules

JSON Schema validates bridge shape. The Python validator enforces rules that require semantic comparison across fields:

- `human_actor_requires_consent_for_reputation_microbeat`;
- `promotion_state_strict_inheritance`;
- `verifier_scores_consistent_with_verdict`;
- `undecided_fails_closed_to_deny`;
- `pattern_c_always_denies`.

## Certificate-family boundary

This tranche references certificate-family concepts and states but does not mutate the certificate-family schemas. The requested #47 v1.3 certificate-family schema bump remains blocked until canonical M0-M5 schema anchors are identified or created.

## Capability-tier boundary

Bridge schemas may include optional `capability_tier_invocation` metadata. This field is additive and does not implement the six full capability-tier schemas.

## Validation lane

The local validation lane is:

```bash
make bridges-ci
```

The lane validates:

- all three bridge JSON Schemas;
- positive fixture pass behavior;
- negative fixture intended failure reasons;
- specific cross-field diagnostics.

## Non-claims

This plan does not implement runtime bridge execution, Atlas admission runtime, Masonmark proof adjudication, OpsHistory ingestion, Pneumachinalis scoring, certificate-family schema mutation, capability-tier schema implementation, SHACL, or Rego.
