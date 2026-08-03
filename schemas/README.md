# Schemas

This directory contains the public contract surface for ProCybernetica.

Schemas are the doctrine-as-code layer. They turn the captured corpus into executable validation surfaces for nodes, commands, delegations, observations, status reports, events, transitions, replay records, evaluation results, promotion decisions, incidents, artifacts, claims, provenance, and capability descriptors.

## Canonical v0 schema set

The canonical v0 namespace is:

```text
https://schemas.socioprophet.org/procybernetica/
```

The canonical v0 schema files are:

- `node_descriptor.schema.json` — constitutional identity, lifecycle, conformance, capability, policy, and observability surface for nodes.
- `artifact_envelope.schema.json` — evidence-bearing artifact record.
- `policy_envelope.schema.json` — constitutional policy reference or summary envelope.
- `command_envelope.schema.json` — authority-bearing command wrapper.
- `delegation_envelope.schema.json` — bounded transfer of work or authority between nodes.
- `observation_envelope.schema.json` — information-plane observation wrapper.
- `status_envelope.schema.json` — upward or peer status report.
- `event_envelope.schema.json` — cross-plane event record.
- `trace_event.schema.json` — normalized event for causal reconstruction.
- `transition_record.schema.json` — lifecycle transition evidence.
- `replay_envelope.schema.json` — replay manifest and reconstruction contract.
- `evaluation_result.schema.json` — replay, benchmark, shadow, or conformance result.
- `promotion_decision.schema.json` — constitutional admission, quarantine, rollback, revocation, or review verdict.
- `incident_report.schema.json` — failure, contradiction, drift, safety, or remediation episode report.
- `claim.schema.json` — public claim object for practicum and evidence surfaces.
- `provenance_record.schema.json` — source and evidence lineage record.
- `capability_descriptor.schema.json` — high-level capability gateway descriptor.
- `control_node.schema.json` — Fractal-Control-Fabric ControlNode registry: binds each lawful control node to one of the 11 control-node types (closed enum), the concrete resource it governs (repo/agent/service/gateway/host), and its lawful-promotion obligations (which membrane gates apply). Closes ADR-0002 §8 GAP-3 / prophet-workspace#85. Validated by `tools/cybernetic_governance/validate_control_node.py` (`make control-node-ci`).

## Validation lane

The v0 schema normalization lane is:

```bash
make v0-schemas-ci
python tools/cybernetic_governance/validate_v0_schemas.py
python -m pytest -q tests/test_v0_schema_normalization.py
```

The validator checks:

- every canonical v0 schema file exists;
- every canonical v0 schema is valid JSON Schema draft 2020-12;
- every canonical v0 schema declares `$id`, title, description, required fields, root `object` type, properties, `schema_version`, and explicit `additionalProperties` posture;
- every canonical v0 `$id` uses the v0 namespace above;
- fixture-backed versus deferred-fixture posture is recorded.

## Design rules

1. Schemas define public interfaces, not private implementation internals.
2. Authority-bearing payloads must identify issuer, subject, policy references, and provenance references.
3. Information-plane payloads must preserve source, confidence, timestamp, and evidence references.
4. Promotion decisions must distinguish proposal, shadow-only, limited-authority, full-promotion, quarantine, review, rollback, and revocation.
5. Public examples must use synthetic data unless operational data has been explicitly cleared.
6. v0 schema normalization does not expand runtime implementation.

## Related records

- `docs/decisions/0002-v0-contract-scope.md`
- `docs/reconciliation/SCHEMA_PROFILE_RECONCILIATION.md`
- `docs/schemas/V0_SCHEMA_NORMALIZATION_STATUS.md`
