# F4 Certificate v1.3 Monitorability Addendum

Status: v0.1 addendum  
Issue: #47  
Parent doctrine: `docs/falsification/unified-falsification-v1.0.md`  
Runtime claim: none

## Purpose

This addendum updates the F4 falsification posture after the certificate-family v1.3 base schema and Cairnmark-to-Stele transition doctrine landed.

The parent doctrine remains the canonical F4 table. This addendum records the concrete monitorability change created by:

- `schemas/certificates/base-certificate.v1.3.json`
- `docs/certificates/CERTIFICATE_FAMILY_INDEX_V1_3.md`
- `docs/certificates/CAIRNMARK_TO_STELE_TRANSITION_DOCTRINE.md`
- `tests/fixtures/transition/*.json`
- `tests/fixtures/falsification/f4-cairnmark-stele.synthetic.json`
- `tools/cybernetic_governance/validate_certificate_v13.py`

## F4.1 — Reasoning operations conflated with evidence

Status after #47: structurally monitorable plus human-review required.

Reasoning traces are now represented by `reasoning_trace_ref`. The field is a reasoning/proofpack/adjudication reference, not direct evidence. Review must still inspect whether claims cite reasoning as evidence without evidentiary support.

Validation status:

- fixture marker present;
- certificate v1.3 validator records presence of `reasoning_trace_ref`;
- human review remains required for claim interpretation.

## F4.2 — Cairnmarks indistinguishable from Steles

Status after #47: schema-testable and fixture-backed.

The `promotion_state` field distinguishes:

- `candidate` = Cairnmark;
- `promoted_stele` = adjudicated Stele;
- `rejected` = adjudicated rejection;
- `superseded` = successor-bound certificate state.

The validator confirms that candidate records cannot use admitted/promoted semantics and that promoted Steles require reasoning and authority evidence.

Validation status:

- shared v1.3 certificate schema exists;
- transition doctrine exists;
- candidate, promoted, rejected, superseded, and invalid-composite fixtures exist;
- F4.2 fixture marker present.

## F4.3 — Defeasible support treated as silent authority

Status after #47: structurally monitorable plus future runtime monitoring.

The v1.3 fields `authority_layer` and `promotion_state` make silent authority drift detectable at the schema/fixture level. Runtime authority changes still require downstream runtime telemetry and policy-plane instrumentation.

Validation status:

- fixture marker present;
- authority and promotion fields exist in the base v1.3 schema;
- runtime monitoring remains future work.

## Non-claims

This addendum does not implement runtime telemetry, production authority checks, Atlas runtime admission, capability-tier schemas, or SHACL/Rego. It records the transition from doctrine-only F4 posture to schema/fixture-backed structural monitorability where applicable.
