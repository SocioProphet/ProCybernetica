# Cybernetic Governance Schemas

**Status:** Draft v0.1
**Track:** Tier 1 schema implementation for the Cybernetic Governance Fabric

This directory contains machine-readable schemas for the ProCybernetica Cybernetic Governance Fabric.

The schemas implement the doctrine captured under:

- `docs/cybernetic-governance/CAPTURE_INDEX.md`
- `docs/cybernetic-governance/GAP_AUDIT_AND_READINESS_MATRIX.md`
- `docs/constitutional/CONSTITUTIONAL_INVARIANTS.md`
- `docs/foundations/CYBERNETIC_GOVERNANCE_FABRIC.md`
- `docs/integrations/AGENTIC_OPS_CMDP_UCO_PERSONA_POLICY.md`

## Implemented in this slice

| Schema | Purpose | Status |
|---|---|---|
| `enums.v1.json` | Canonical enum definitions used by Tier 1 schemas | draft implemented |
| `artifact_lifecycle_state.v1.json` | Current lifecycle state of a governance artifact | draft implemented |
| `lifecycle_transition.v1.json` | Requested or completed artifact lifecycle transition | draft implemented |
| `agentic_persona_policy.v1.yaml` | Persona-specific agentic ops policy, budget, autonomy, reversibility, plan stability, telemetry, and degradation schema | draft implemented |

## Reference implementations in this slice

| Tool | Purpose | Status |
|---|---|---|
| `tools/cybernetic_governance/agentic_persona_substrategy_chooser.py` | Deterministic persona + workload signature -> substrategy bundle resolver | draft reference implementation |

## Required next schemas

Core governance:

- `authority_chain.v1.json`
- `instruction_conflict_case.v1.json`
- `agent_action_trace.v1.json`
- `tool_permission_scope.v1.json`
- `environment_delta.v1.json`
- `side_effect_assessment.v1.json`
- `off_history_evidence.v1.json`
- `monitor_alert.v1.json`
- `meta_monitor_report.v1.json`
- `evidence_receipt.v1.json`
- `promotion_decision.v1.json`
- `cybernetic_safety_case.v1.json`
- `release_delta_report.v1.json`
- `incident_record.v1.json`
- `privacy_evidence_classification.v1.json`
- `authority_graph_snapshot.v1.json`

Hardening and assurance:

- `non_claim.v1.json`
- `artifact_provenance.v1.json`
- `validator_run_receipt.v1.json`
- `proof_pack_manifest.v1.json`
- `proof_pack_disposition.v1.json`

Agentic Ops:

- `agentic_uco_step_cost.v1.json`
- `agentic_task_budget.v1.json`
- `agentic_cmdp_trace.v1.json`
- `agentic_degradation_event.v1.json`
- `loop_detector_signal.v1.json`
- `prefix_cache_prompt_plan.v1.json`
- `agentic_post_hoc_eval.v1.json`

AgentPlane binding:

- `agentplane_run_capsule.v1.json`
- `agentplane_tool_grant.v1.json`
- `agentplane_action_dispatch.v1.json`
- `agentplane_subagent_delegation.v1.json`

Dependency-control calculus:

- `dependency_control_graph.v1.json`
- `control_reachability_record.v1.json`
- `observability_partition.v1.json`
- `shared_dependency_ancestry.v1.json`
- `dependency_cancellation_record.v1.json`
- `adaptive_feedback_loop.v1.json`

Enterprise ontology / environment aperture:

- `agent_unit.v1.json`
- `aperture.v1.json`
- `regime_model.v1.json`
- `enterprise_event_envelope.v1.json`
- `organization_identity_profile.v1.json`
- `service_capability_profile.v1.json`

## Schema rules

Every schema should:

1. declare `$schema` and `$id` where JSON Schema is used;
2. use stable `v1` naming;
3. include a clear `title` and `description`;
4. use canonical enums from `enums.v1.json` where applicable;
5. include invariant traceability through `x_implements_invariants` and/or `implements_invariants`;
6. include examples when practical;
7. avoid claiming runtime readiness until fixtures and validators exist.

## Non-claims

These schemas are draft contracts. They do not imply runtime enforcement until validators, fixtures, and consuming services are implemented.
