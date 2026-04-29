# Schemas

This directory contains the public contract surface for ProCybernetica.

Schemas are the doctrine-as-code layer. They turn the Drive corpus into executable validation surfaces for nodes, commands, observations, status reports, replay records, evaluation results, promotion decisions, incidents, and artifacts.

## Initial schema set

Planned core schemas:

- `node_descriptor.schema.json` — identity, node class, lifecycle, authority parent, peer groups, capabilities, memory, world-model, policy, and observability references.
- `command_envelope.schema.json` — typed authority-bearing command.
- `delegation_envelope.schema.json` — bounded transfer of work between nodes.
- `observation_envelope.schema.json` — information-plane observation.
- `status_envelope.schema.json` — upward or peer status report.
- `artifact_envelope.schema.json` — evidence-bearing artifact record.
- `replay_envelope.schema.json` — replay manifest and reconstruction contract.
- `evaluation_result.schema.json` — replay, benchmark, shadow, or conformance result.
- `promotion_decision.schema.json` — constitutional admission, quarantine, or rejection decision.
- `incident_report.schema.json` — failure, contradiction, drift, or safety event.
- `trace_event.schema.json` — normalized event for causal reconstruction.
- `transition_record.schema.json` — lifecycle transition evidence.

## Design rules

1. Schemas define public interfaces, not private implementation internals.
2. Authority-bearing payloads must identify issuer, subject, policy references, and provenance references.
3. Information-plane payloads must preserve source, confidence, timestamp, and evidence references.
4. Promotion decisions must distinguish proposal, shadow-only, limited-authority, full-promotion, quarantine, and rejection.
5. Public examples must use synthetic data unless operational data has been explicitly cleared.
