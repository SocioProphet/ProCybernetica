# AgentPlane Cybernetic Governance Binding

**Status:** Draft v0.1
**Track:** Runtime-plane integration contract
**Applies to:** AgentPlane, Prophet Platform runtime services, ProCybernetica governance schemas, SocioSphere registry/promotion orchestration
**Purpose:** Define how AgentPlane participates in the Cybernetic Governance Fabric without requiring direct implementation changes while the runtime surface is still stabilizing.

---

## 1. Purpose

AgentPlane is the runtime plane where governed agency becomes operational.

ProCybernetica defines doctrine, schemas, fixtures, validators, promotion law, and safety-case discipline. AgentPlane should consume those contracts to make agent execution lawful, traceable, policy-bound, auditable, and replayable.

This document defines the expected binding between AgentPlane and the Cybernetic Governance Fabric.

---

## 2. Boundary

AgentPlane should not own ProCybernetica doctrine.

AgentPlane should consume ProCybernetica contracts and emit governance artifacts during runtime execution.

### ProCybernetica owns

- constitutional invariants;
- authority-chain schema;
- action-trace schema;
- tool-permission schema;
- off-history schema;
- evidence-receipt schema;
- promotion-decision schema;
- safety-case schema;
- release-delta schema;
- validator fixtures;
- conformance vocabulary.

### AgentPlane owns or should own

- run planning;
- run capsules;
- tool grant resolution;
- action dispatch;
- subagent coordination;
- tool invocation boundaries;
- runtime event emission;
- off-history capture at execution time;
- runtime replay hooks;
- operator-visible run readout;
- degraded-autonomy execution modes;
- handoff to Prophet Platform evidence and monitor APIs.

### Prophet Platform owns or should own

- cybernetic monitor API;
- evidence receipt API;
- eval fabric integration;
- release-delta API;
- dashboard surfaces;
- datastore wiring.

### SocioSphere owns or should own

- cross-repo registry;
- workspace promotion state;
- safety-case registry;
- canonical dependency graph;
- cross-repo conformance checks.

---

## 3. Required AgentPlane runtime objects

AgentPlane should eventually emit or consume the following objects.

### 3.1 Agent run capsule

A run capsule is the top-level evidence container for one governed agent run.

Minimum fields:

- `run_capsule_id`
- `agent_id`
- `agent_version`
- `workspace_ref`
- `authority_chain_id`
- `run_goal`
- `autonomy_tier`
- `risk_tier`
- `tool_grant_refs`
- `action_trace_refs`
- `monitor_alert_refs`
- `off_history_refs`
- `evidence_receipt_refs`
- `control_decision_refs`
- `replay_status`
- `operator_readout_ref`

Candidate schema:

- `agentplane_run_capsule.v1.json`

### 3.2 Tool grant

A tool grant records what an agent is allowed to do before execution.

Minimum fields:

- `tool_grant_id`
- `agent_id`
- `tool_id`
- `grant_scope`
- `authority_chain_id`
- `allowed_actions`
- `forbidden_actions`
- `side_effect_budget`
- `expires_at`
- `approval_ref`
- `revocation_status`

Candidate schema:

- `agentplane_tool_grant.v1.json`

### 3.3 Agent action dispatch

Action dispatch is the runtime attempt to invoke a tool, mutate state, or commit to a plan step.

It must produce or reference:

- `agent_action_trace.v1.json`
- `tool_permission_scope.v1.json`
- `side_effect_assessment.v1.json`
- `environment_delta.v1.json`
- `monitor_alert.v1.json`
- `control_decision.v1.json`
- `evidence_receipt.v1.json`

Candidate schema:

- `agentplane_action_dispatch.v1.json`

### 3.4 Subagent delegation

Subagent delegation must not create a hidden authority lane.

Minimum fields:

- `delegation_id`
- `parent_agent_id`
- `subagent_id`
- `delegated_goal`
- `delegated_authority_scope`
- `inherited_policy_refs`
- `forbidden_escalations`
- `tool_grant_refs`
- `monitoring_requirements`
- `return_evidence_requirements`

Candidate schema:

- `agentplane_subagent_delegation.v1.json`

### 3.5 Off-history runtime record

If AgentPlane blocks, transforms, downgrades, or declines an action, it must preserve off-history.

Minimum fields:

- `off_history_id`
- `run_capsule_id`
- `proposed_action_ref`
- `blocked_or_transformed_by`
- `policy_reason`
- `monitor_reason`
- `safe_alternative_ref`
- `counterfactual_summary`
- `evidence_receipt_ref`

Candidate schema:

- `off_history_evidence.v1.json`

---

## 4. Runtime requirements

### Requirement A — Every AgentPlane run has a capsule

No governed agent run may be considered reviewable without a run capsule.

### Requirement B — Every tool call has a tool grant

A tool call without a tool grant is an ungoverned action.

### Requirement C — Every privileged action has a permission scope

Privileged actions include file writes, repository mutations, deployment changes, external sends, credential access, permission changes, policy changes, monitor changes, or any irreversible operation.

### Requirement D — Every blocked action preserves off-history

Blocked, transformed, downgraded, sandboxed, or refused actions must emit off-history evidence.

### Requirement E — Every subagent has bounded delegated authority

Subagents may not inherit ambient authority. They must receive explicit delegated authority and explicit forbidden escalations.

### Requirement F — Every run produces an operator readout

An operator readout should summarize goal, authority, tool grants, actions, off-history, monitor alerts, evidence, risks, and remaining non-claims.

---

## 5. Integration with proof packs

The SocioProphet Proof Pack Template expects an AgentPlane run capsule and operator readout for governed-agent reviews.

Relevant proof-pack exhibit:

- AgentPlane run capsule;
- Operator readout;
- policy-gated dispatch proof;
- tool grant evidence;
- replay or off-history evidence;
- final disposition and known excluded claims.

The proof pack packages AgentPlane evidence. It does not replace AgentPlane run evidence.

---

## 6. Integration with evidence receipts

AgentPlane should not be the sole signer of final evidence for its own actions.

Runtime events emitted by AgentPlane should be converted into evidence receipts through the evidence service or platform receipt path.

Minimum path:

`AgentPlane runtime event -> action trace -> monitor/control decision -> evidence receipt -> proof pack / safety case`

---

## 7. Integration with release delta

AgentPlane changes are material if they affect:

- tool grant semantics;
- subagent delegation;
- run capsule format;
- off-history capture;
- action dispatch;
- replay hooks;
- monitor integration;
- human approval flow;
- autonomy tier enforcement.

Those changes require a release-delta report before promotion.

---

## 8. Integration with SocioSphere

SocioSphere should eventually index AgentPlane run capsules at the workspace level.

Candidate registry objects:

- `agentplane_run_capsule_registry.yaml`
- `agentplane_tool_grant_registry.yaml`
- `agentplane_safety_case_binding.yaml`

SocioSphere should not need raw private prompts or raw tool payloads to perform registry-level governance. It should consume redacted evidence receipts, digests, summaries, and promotion states.

---

## 9. First implementation slice

When the AgentPlane runtime surface is ready, the first binding should implement:

1. `agentplane_run_capsule.v1.json`
2. `agentplane_tool_grant.v1.json`
3. `agentplane_action_dispatch.v1.json`
4. `agentplane_subagent_delegation.v1.json`
5. off-history link to `off_history_evidence.v1.json`
6. operator readout fixture
7. proof-pack exhibit fixture

---

## 10. Tests

### Test A — Run without capsule

A governed run executes without run capsule.

Expected: invalid.

### Test B — Tool call without grant

An agent attempts a tool call without a matching tool grant.

Expected: invalid or blocked.

### Test C — Privileged action without permission scope

A privileged action lacks side-effect assessment or permission scope.

Expected: invalid.

### Test D — Subagent ambient authority

A subagent receives broad implicit authority without delegated scope.

Expected: invalid.

### Test E — Blocked action without off-history

A blocked or transformed action leaves no off-history record.

Expected: invalid.

### Test F — AgentPlane proof-pack exhibit missing run capsule

A proof pack claims governed-agent evidence but lacks run capsule reference.

Expected: invalid.

---

## 11. Non-claims

This document does not assert that a standalone AgentPlane repository is present in the current connector installation.

This document does not implement AgentPlane runtime code.

This document does not make AgentPlane the owner of ProCybernetica doctrine.

This document only defines the expected governance binding so AgentPlane can be integrated as the runtime plane when its implementation surface is ready.
