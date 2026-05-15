# V0 Schema Normalization Status

Status: v0.1 validation record  
Issue: #6  
Runtime claim: none

## Purpose

This document records the normalized v0 JSON Schema surface after schema/profile reconciliation.

The canonical v0 schema namespace is:

```text
https://schemas.socioprophet.org/procybernetica/
```

This namespace is intentionally preserved for the v0 contract surface. Later specialized schema families may use other package-specific `$id` roots, but the v0 envelope family remains stable under this prefix.

## Canonical v0 schema set

The canonical v0 set contains 17 public schemas:

| Schema | Status | Fixture posture |
| --- | --- | --- |
| `node_descriptor.schema.json` | present | fixture-backed |
| `artifact_envelope.schema.json` | present | fixture-backed |
| `policy_envelope.schema.json` | present | fixture-backed |
| `command_envelope.schema.json` | present | fixture-backed |
| `delegation_envelope.schema.json` | present | fixture-backed |
| `observation_envelope.schema.json` | present | fixture-backed |
| `status_envelope.schema.json` | present | fixture-backed |
| `event_envelope.schema.json` | present | fixture-backed |
| `trace_event.schema.json` | present | fixture-backed |
| `transition_record.schema.json` | present | fixture-backed |
| `replay_envelope.schema.json` | present | fixture-backed |
| `evaluation_result.schema.json` | present | fixture-backed |
| `promotion_decision.schema.json` | present | fixture-backed |
| `incident_report.schema.json` | present | deferred fixture |
| `claim.schema.json` | present | fixture-backed |
| `provenance_record.schema.json` | present | fixture-backed |
| `capability_descriptor.schema.json` | present | fixture-backed |

`incident_report.schema.json` remains a public v0 contract. Its fixture posture is explicitly deferred because incident runtime semantics should not be expanded inside issue #6.

## Validator

The v0 schema validator is:

```text
tools/cybernetic_governance/validate_v0_schemas.py
```

It checks:

- every canonical v0 schema file exists;
- every canonical v0 schema is JSON Schema draft 2020-12;
- every schema has `$id`, title, description, root object type, required fields, properties, `schema_version`, and explicit `additionalProperties` posture;
- every v0 `$id` uses the canonical v0 namespace;
- fixture-backed and deferred-fixture postures are explicit.

## Validation commands

```bash
make v0-schemas-fixtures
make v0-schemas-ci
python tools/cybernetic_governance/validate_v0_schemas.py
python -m pytest -q tests/test_v0_schema_normalization.py
```

## Non-claims

This tranche does not add a new schema family, does not implement runtime validation services, does not alter upstream runtime ownership, does not introduce production telemetry, and does not expand incident runtime behavior. It closes the v0 schema-normalization lane by making the reconciled schema surface explicit and executable in CI.
