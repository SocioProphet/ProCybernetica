# Cybernetic Governance Capture Index

**Status:** Draft v0.1  
**Track:** ProCybernetica frontier governance doctrine  
**Branch:** `cybernetic-governance-doctrine-v0-1`

This index captures the cybernetic-governance doctrine bundle and reconciles it against the estate-level hybrid control-plane framing from PR #49. The corrected posture is not a new centralized control plane. The major planes already exist; the missing spine is a normalized authority-dependency graph binding trust surfaces, control effects, evidence, cancellation, quarantine, recovery, and proof packaging.

## Canonical reading order

1. [`../constitutional/CONSTITUTIONAL_INVARIANTS.md`](../constitutional/CONSTITUTIONAL_INVARIANTS.md) — non-negotiable governance constraints.
2. [`../foundations/CYBERNETIC_GOVERNANCE_FABRIC.md`](../foundations/CYBERNETIC_GOVERNANCE_FABRIC.md) — full doctrine architecture and plane decomposition, now treated as conformance language rather than centralized ownership.
3. [`PRIOR_SYNTHESIS_RECONCILIATION.md`](PRIOR_SYNTHESIS_RECONCILIATION.md) — explicit translation from prior layer/tier framing to the corrected estate authority-dependency framing.
4. [`../security/THREAT_MODEL.md`](../security/THREAT_MODEL.md) — adversaries, assets, trust boundaries, attack surfaces, and controls.
5. [`../constitutional/SEPARATION_OF_POWERS.md`](../constitutional/SEPARATION_OF_POWERS.md) — role separation and authority-concentration controls.
6. [`GAP_AUDIT_AND_READINESS_MATRIX.md`](GAP_AUDIT_AND_READINESS_MATRIX.md) — post-capture hardening matrix that defines lifecycle states, enums, schema-to-invariant traceability, non-claim structure, disclosure profiles, readiness levels, MVP trace requirements, CI checks, and cross-repo dependency boundaries.
7. [`../assurance/SOCIOPROPHET_PROOF_PACK_TEMPLATE.md`](../assurance/SOCIOPROPHET_PROOF_PACK_TEMPLATE.md) — reviewer-facing proof packet template for buyer, analyst, procurement, architecture, and gate reviews.
8. [`../integrations/AGENTPLANE_CYBERNETIC_GOVERNANCE_BINDING.md`](../integrations/AGENTPLANE_CYBERNETIC_GOVERNANCE_BINDING.md) — runtime-plane contract for AgentPlane run capsules, tool grants, action dispatch, subagent delegation, off-history, operator readouts, and proof-pack exhibits.
9. [`../integrations/AGENTIC_OPS_CMDP_UCO_PERSONA_POLICY.md`](../integrations/AGENTIC_OPS_CMDP_UCO_PERSONA_POLICY.md) — Agentic Ops CMDP/UCO/persona-policy specialization for budgeted stochastic agent workloads.
10. [`../integrations/ZACHMAN_AU_ENVIRONMENT_SEVEN_MODEL_ALIGNMENT.md`](../integrations/ZACHMAN_AU_ENVIRONMENT_SEVEN_MODEL_ALIGNMENT.md) — enterprise ontology, AgentUnit, Environment/Aperture, ORG/FIBO, Seven-Model, and SOA-modernization alignment.
11. [`../foundations/QUANTUM_CYBERNETIC_DEPENDENCE_CALCULUS.md`](../foundations/QUANTUM_CYBERNETIC_DEPENDENCE_CALCULUS.md) — dependency-control calculus aligning quantum unitary-dependence theory with governed agent/runtime systems.
12. [`../release/BIRKHOFF_RELEASE_DELTA.md`](../release/BIRKHOFF_RELEASE_DELTA.md) — release-delta decomposition into counter-terms and renormalized contributions.
13. [`../monitor/MONITOR_NETWORK_AS_QEC.md`](../monitor/MONITOR_NETWORK_AS_QEC.md) — monitor networks as error-correcting systems.
14. [`../assurance/PCP_REPLAY_AUDIT.md`](../assurance/PCP_REPLAY_AUDIT.md) — probabilistically checkable replay and audit artifacts.

## Corrected estate framing

PR #49 corrects the framing from greenfield architecture to estate reconciliation.

| Plane | Owner repo | Role |
|---|---|---|
| Visible cognition/control-loop and trust surface seed | `SocioProphet/superconscious` | Declares trust surfaces and visible cognition/control loop boundaries |
| Estate authority-dependency graph | `SocioProphet/sociosphere` | Owns topology, dependency direction, authority-dependency graph, and operator graph state |
| Cancellation / break-glass / fail-closed law | `SocioProphet/policy-fabric` | Owns admission, inheritance, cancellation, override, revocation, and fail-closed policy semantics |
| Evidence / replay / execution | `SocioProphet/agentplane` | Owns bounded execution, run evidence, replay, placement, and work-order lifecycle |
| Local state-integrity / repair | `SourceOS-Linux/sourceos-syncd` | Owns local-first state integrity, degraded posture, diagnosis, repair, and host/runtime enforcement |
| Doctrine and conformance vocabulary | `SocioProphet/ProCybernetica` | Owns reconciliation doctrine, conformance language, proof-pack linkage, and public assurance posture |

The minimal shared vocabulary should be:

- `AuthorityDependency`
- `ControlEffect`
- `CancellationBinding`

Prior dependency-control schemas are useful as analytical views over this spine, not as a parallel governance universe.

## Captured doctrine commitments

The bundle captures these commitments as doctrine, not loose notes:

- no hidden authority lane;
- no action without trace;
- no promotion by prose alone;
- evidence must be digital, typed, digestible, privacy-classified, and replay-scoped;
- irreversible action requires approval or stronger gate;
- blocked and transformed actions retain off-history evidence;
- monitors require meta-monitoring;
- frontier promotion requires safety cases and non-claims;
- release changes require delta governance;
- authority concentration is measurable and gate-relevant;
- public-safe assurance is publishable by default, with disciplined redaction.

## Agentic Ops specialization

Agentic Ops is a stochastic workload specialization of the UCO/persona canvas. It adds prompt-token decomposition, completion tokens, cache-read tokens, tool-call units, verification tokens, replay/checkpoint storage, and semantic-memory costs.

The control lens is a constrained Markov decision process. Production behavior may remain deterministic: persona policy plus workload signature resolves to a substrategy bundle, admission decision, degradation ladder, and telemetry requirements.

Implemented artifacts in this branch:

- `schemas/cybernetic-governance/agentic_persona_policy.v1.yaml`
- `tools/cybernetic_governance/agentic_persona_substrategy_chooser.py`

## Enterprise ontology and environment alignment

The Zachman-derived AgentUnit and Environment/Aperture alignment supplies the enterprise ontology over which proof packs, AgentPlane run capsules, SourceOS evidence, and SocioSphere graph nodes can be typed.

Core primitives:

- Artifact;
- Capability;
- Locale;
- Principal;
- Event;
- Motive;
- Environment;
- Aperture;
- RegimeModel.

This is doctrine and schema runway, not a new runtime owner.

## Reviewer-facing proof packaging

The proof pack template is the reviewer-facing packaging layer. It does not replace lower-level evidence receipts, action traces, release-delta reports, cybernetic safety cases, or non-claim objects. It organizes those artifacts for buyer, analyst, procurement, architecture, or gate review.

Proof packs should eventually cite AgentPlane run capsules, ProCybernetica safety cases, PolicyFabric decisions, SocioSphere authority-dependency graph entries, SourceOS state-integrity records, event-spine evidence, PRM observations, and ORG/FIBO identity records.

## Post-capture hardening

The doctrine bundle is a captured v0.1 draft, not executable v0.

The work may not be called executable v0 until Tier 1 schemas exist, canonical enums exist, schemas map to invariants, fixtures exist, validators pass and fail correctly, MVP trace examples exist, evidence disclosure profiles exist, non-claim objects exist, readiness state is updated, and integration boundaries are recorded.

## Tier map

### Tier 0 — Constitutional invariants

Doctrine that no future schema or runtime service may violate.

### Tier 1 — Current implemented schema base

Implemented in this branch:

- `enums.v1.json`
- `artifact_lifecycle_state.v1.json`
- `lifecycle_transition.v1.json`
- `agentic_persona_policy.v1.yaml`

### Tier 1 — Required next schemas

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
- `non_claim.v1.json`
- `artifact_provenance.v1.json`
- `validator_run_receipt.v1.json`

AgentPlane and Agentic Ops:

- `agentplane_run_capsule.v1.json`
- `agentplane_tool_grant.v1.json`
- `agentplane_action_dispatch.v1.json`
- `agentplane_subagent_delegation.v1.json`
- `agentic_uco_step_cost.v1.json`
- `agentic_task_budget.v1.json`
- `agentic_cmdp_trace.v1.json`
- `agentic_degradation_event.v1.json`
- `loop_detector_signal.v1.json`
- `prefix_cache_prompt_plan.v1.json`
- `agentic_post_hoc_eval.v1.json`

Proof pack and enterprise ontology:

- `proof_pack_manifest.v1.json`
- `proof_pack_disposition.v1.json`
- `agent_unit.v1.json`
- `aperture.v1.json`
- `regime_model.v1.json`
- `enterprise_event_envelope.v1.json`
- `organization_identity_profile.v1.json`
- `service_capability_profile.v1.json`

Estate reconciliation:

- `AuthorityDependency` schema and registry should land in SocioSphere, not ProCybernetica.
- `ControlEffect` vocabulary should be shared by SocioSphere, PolicyFabric, AgentPlane, and SourceOS.
- `CancellationBinding` should land in PolicyFabric.
- AgentPlane should emit authority-dependency evidence.
- SourceOS should bind authority dependencies to local state integrity and repair posture.

## Explicitly out of scope for this PR

The following are important but should land in separate PRs or repos:

- M-series transition / Cairnmark-to-Stele transition doctrine;
- unified falsification observables and fixtures;
- bridge schema tranche for OpsHistory, Pneumachinalis, Masonmark, certificate, and Atlas;
- capability-tier invocation contract as previously framed;
- runtime implementation in AgentPlane, PolicyFabric, SocioSphere, SourceOS, or Superconscious.

## Implementation next steps

1. Finish branch hygiene so this PR contains only cybernetic-governance and reconciliation artifacts.
2. Merge or reconcile PR #49 first as the corrected estate framing.
3. Treat this branch as the prior synthesis capture/reconciliation branch.
4. Implement `non_claim`, `privacy_evidence_classification`, `artifact_provenance`, and `validator_run_receipt` next.
5. Implement core authority/action/evidence schemas.
6. Implement Agentic Ops fixtures for persona policy and substrategy chooser.
7. Open SocioSphere authority-dependency graph issue after PR #49 lands.
8. Open PolicyFabric cancellation binding issue after graph vocabulary stabilizes.
9. Open AgentPlane authority-dependency evidence issue after core authority references stabilize.
10. Keep Superconscious untouched until concrete trust-surface dependency contracts are ready.

## Non-claims

This bundle does not claim that all formal foundations are implemented.

This bundle does not claim executable v0 status.

This bundle does not centralize runtime ownership in ProCybernetica.

This bundle captures doctrine, schema runway, and reconciliation logic so the estate can converge on a shared authority-dependency spine without erasing existing repo ownership.
