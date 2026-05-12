# Bridge Schemas v1 Execution Plan

**Status:** Draft v0.1 capture
**Track:** Base-architecture bridge schemas
**Purpose:** Define the Turn 2 bridge-schema tranche that composes the base seven-layer architecture: OpsHistory → Pneumachinalis, Masonmark → M-series certificates, and certificates → TritFabric Atlas promotion decisions.

---

## 1. Purpose

The bridge-schema tranche makes the substrate structurally composable.

It defines how:

1. OpsHistory operational events flow into Pneumachinalis reputation via microbeat contribution events.
2. Masonmark proofpacks specialize into M-series certificate fragments.
3. Certificate verdicts produce Atlas promotion decisions using four-valued resolution.

Each bridge optionally references the quantum dependency substrate capability tier through `capability_tier_invocation`. Base-architecture composition remains the default. Capability-tier invocation is additive and opt-in.

---

## 2. Bridge 1: OpsHistory → Pneumachinalis

Target schema:

- `schemas/bridges/ops-history-to-pneumachinalis.v1.json`

Purpose:

- Mechanically map an OpsHistory operational event to a Pneumachinalis microbeat contribution event.
- Every OpsHistory event with `actor_class != H` produces exactly one corresponding microbeat by this mapping.
- Human actor events produce microbeats only when consent evidence supports reputation stake or promotion to Stele.

Required structural sections:

- `ops_history_event_ref`
- `pneumachinalis_microbeat_ref`
- `actor_translation`
- `role_translation`
- `authority_translation`
- `topology_translation`
- `braid_coordinate_derivation`
- `state_coordinate_derivation`
- `mapping_authority`
- `fail_closed_on_translation_failure`
- optional `capability_tier_invocation`
- `non_claims`

Required positive fixture:

- `tests/fixtures/bridges/ops-history-to-pneumachinalis.machine-actor-tool-call.synthetic.json`

Required negative fixture:

- `tests/fixtures/bridges/ops-history-to-pneumachinalis.human-actor-without-stake-consent.invalid.synthetic.json`

Required cross-field rule:

- `human_actor_requires_consent_for_reputation_microbeat`

---

## 3. Bridge 2: Masonmark → Certificate

Target schema:

- `schemas/bridges/masonmark-to-certificate.v1.json`

Purpose:

- Declare that every M-series certificate is structurally a specialized Masonmark proofpack.
- Record how proofpack fields populate certificate fields.
- Record how Cairnmark/Stele promotion state maps to certificate verdict status.

Required structural sections:

- `proofpack_ref`
- `certificate_ref`
- `query_to_subject`
- `grounding_to_evidence`
- `program_ast_to_claim`
- `verifier_scores_to_verdict`
- `execution_trace_to_replay`
- `signer_set_to_authority`
- `divergence_to_lineage`
- `observability_partition_preserved`
- `promotion_state_inheritance`
- `specialization_authority`
- optional `capability_tier_invocation`
- `non_claims`

Required positive fixture:

- `tests/fixtures/bridges/masonmark-to-certificate.m2-pattern-a-stele.synthetic.json`

Required negative fixture:

- `tests/fixtures/bridges/masonmark-to-certificate.candidate-proofpack-to-stele-certificate.invalid.synthetic.json`

Required cross-field rules:

- `promotion_state_strict_inheritance`
- `verifier_scores_consistent_with_verdict`

---

## 4. Bridge 3: Certificate → Atlas

Target schema:

- `schemas/bridges/certificate-to-atlas.v1.json`

Purpose:

- Map four-valued certificate verdicts to four-valued Atlas promotion decisions.
- Resolve F2.1 with canonical verdict mapping.
- Resolve F2.3 through vector-valued eval delta thresholds.
- Partially address F2.2 by documenting SHACL validation requirements and companion-shape obligations.

Canonical mapping:

| Certificate verdict | Atlas outcome |
|---|---|
| `admitted` | `admit` |
| `partial` + canary follow-up | `admit_with_canary` |
| `partial` + curator follow-up | `admit_with_curator_review` |
| `partial` + no follow-up | `admit_with_curator_review` |
| `rejected` | `deny` |
| `undecided` | `deny` fail-closed |

Required structural sections:

- `certificate_ref`
- `atlas_decision_ref`
- `verdict_mapping`
- `eval_delta_mapping`
- `shacl_validation_required`
- `promotion_authority`
- optional `capability_tier_invocation`
- `non_claims`

Required positive fixtures:

- `tests/fixtures/bridges/certificate-to-atlas.m2-pattern-a-admit.synthetic.json`
- `tests/fixtures/bridges/certificate-to-atlas.undecided-rejected-fail-closed.synthetic.json`

Required cross-field rules:

- `undecided_fails_closed_to_deny`
- `pattern_c_always_denies`

---

## 5. CI lanes

Add CI targets:

```make
bridges-static:
	python -m scripts.validate_schemas schemas/bridges/ops-history-to-pneumachinalis.v1.json
	python -m scripts.validate_schemas schemas/bridges/masonmark-to-certificate.v1.json
	python -m scripts.validate_schemas schemas/bridges/certificate-to-atlas.v1.json

bridges-fixtures-positive:
	python -m scripts.validate_json_schema schemas/bridges/ops-history-to-pneumachinalis.v1.json tests/fixtures/bridges/ops-history-to-pneumachinalis.machine-actor-tool-call.synthetic.json
	python -m scripts.validate_json_schema schemas/bridges/masonmark-to-certificate.v1.json tests/fixtures/bridges/masonmark-to-certificate.m2-pattern-a-stele.synthetic.json
	python -m scripts.validate_json_schema schemas/bridges/certificate-to-atlas.v1.json tests/fixtures/bridges/certificate-to-atlas.m2-pattern-a-admit.synthetic.json
	python -m scripts.validate_json_schema schemas/bridges/certificate-to-atlas.v1.json tests/fixtures/bridges/certificate-to-atlas.undecided-rejected-fail-closed.synthetic.json

bridges-fixtures-negative:
	! python -m scripts.validate_json_schema schemas/bridges/ops-history-to-pneumachinalis.v1.json tests/fixtures/bridges/ops-history-to-pneumachinalis.human-actor-without-stake-consent.invalid.synthetic.json
	! python -m scripts.validate_json_schema schemas/bridges/masonmark-to-certificate.v1.json tests/fixtures/bridges/masonmark-to-certificate.candidate-proofpack-to-stele-certificate.invalid.synthetic.json

bridges-cross-field:
	python -m scripts.validate_cross_field_rules schemas/bridges/ops-history-to-pneumachinalis.v1.json --rule human_actor_requires_consent_for_reputation_microbeat
	python -m scripts.validate_cross_field_rules schemas/bridges/masonmark-to-certificate.v1.json --rule promotion_state_strict_inheritance
	python -m scripts.validate_cross_field_rules schemas/bridges/masonmark-to-certificate.v1.json --rule verifier_scores_consistent_with_verdict
	python -m scripts.validate_cross_field_rules schemas/bridges/certificate-to-atlas.v1.json --rule undecided_fails_closed_to_deny
	python -m scripts.validate_cross_field_rules schemas/bridges/certificate-to-atlas.v1.json --rule pattern_c_always_denies

bridges-ci: bridges-static bridges-fixtures-positive bridges-fixtures-negative bridges-cross-field
certificate-ci: m0-ci m1-ci m1-5-ci m2-ci m3-ci m5-ci v1-1-ci bridges-ci
```

---

## 6. Constitutional invariants enforced

The bridge tranche must enforce:

- CI-1: manifest/latent distinction;
- CI-3: authority bounded by inputs;
- CI-4: promotion-state inheritance;
- CI-5: fail-closed propagation;
- CI-8: consent for human actors in reputation-bearing mappings;
- CI-9: concentration limit;
- CI-10: falsification observables.

---

## 7. Falsification observables addressed

| Observable | Status |
|---|---|
| F2.1 four-valued verdict mapping | Closed by Bridge 3 |
| F2.2 SHACL invariant expression | Partial; companion shapes pending |
| F2.3 vector-valued eval delta | Closed by Bridge 3 |

---

## 8. Capability tier composition

All three bridges include optional `capability_tier_invocation`.

Default value is `null` for routine base-architecture operation.

A bridge may invoke the capability tier only if the invoking artifact carries a valid invocation contract and the deployment/tenant/Stele opt-in composition permits enforcement.

---

## 9. Backward compatibility

This tranche should not mutate existing v1.1 schemas.

Bridges reference existing schemas. They do not modify them.

---

## 10. Non-claims

This execution plan does not itself land the full bridge JSON Schemas or fixtures.

It captures the exact bridge targets, invariants, fixtures, cross-field rules, CI lanes, and falsification coverage needed for the next implementation PR.

The bridge schemas must be implemented with cross-field validators because JSON Schema alone cannot enforce all constitutional invariants.
