# Quantum Cybernetic Dependence Calculus

**Status:** Draft v0.1
**Track:** Foundation / dependency-control calculus
**Applies to:** Cybernetic Governance Fabric, AgentPlane runtime binding, PolicyFabric, TriTRPC, Ontogenesis, SourceOS evidence, future quantum-learning and quantum-agent work
**Purpose:** Align quantum unitary-dependence theory with ProCybernetica's governed dependency-control model.

---

## 1. Thesis

Quantum unitary-dependence theory is a restricted but precise cybernetic calculus.

It studies how local control operations create, propagate, cancel, and expose dependencies in a quantum circuit. In cybernetic terms, it asks:

> Which control knob changes which downstream observable, through which dependency path, under which partition of the system, and with what cancellation behavior?

That is directly aligned with ProCybernetica's governance problem. A governed agent system is also a dependency-controlled transformation system: local actions propagate through typed dependency structures; effects must be observable; control surfaces must be bounded; shared dependencies create collective behavior; duplicated or contradictory influences require cancellation or normalization; and higher-order governance wraps the system in feedback.

This document captures the quantum-dependence framing as a general cybernetic dependency-control calculus.

---

## 2. Quantum-to-cybernetic mapping

| Quantum dependence theory | Cybernetic interpretation |
|---|---|
| Qubits | State-bearing system variables |
| One-qubit unitary | Local control input |
| CNOT | Directed coupling / dependency propagation channel |
| Shared unitary dependence | Correlated control surface |
| Measurement probability | Observed output behavior |
| Partitioned subsystem | Bounded observation scope |
| Dependence cancellation | Regulatory cancellation / parity-like negative feedback |
| Ansatz topology | Controller architecture design |
| Variational optimization loop | Adaptive feedback loop |
| Dependency picture | Control-influence topology |

The important shift is from abstract entanglement to operational dependence: what control can affect what observable?

This is the regulator view. It treats the system as a structured map from interventions to observations.

---

## 3. Relation to cybernetics

A system becomes cybernetic when it has:

1. state-bearing variables;
2. control inputs;
3. transformation rules;
4. observable outputs;
5. coupling topology;
6. feedback or correction mechanism;
7. goal, constraint, or regulation criterion.

Unitary-dependence theory supplies items 1 through 5 directly for quantum circuits. It becomes full cybernetics when wrapped in an outer adaptive loop, such as a variational quantum algorithm where measured performance updates ansatz parameters.

Therefore, the correct classification is:

> Quantum dependence theory is structural/open-loop cybernetics. Variational quantum dependence theory is adaptive/closed-loop cybernetics.

---

## 4. Generalized dependence-control calculus

The governance fabric should generalize the quantum pattern.

### 4.1 State variables

In quantum circuits, variables are qubits.

In governed AI systems, variables include:

- agent state;
- model state;
- memory state;
- tool grant state;
- authority state;
- policy state;
- monitor state;
- evidence state;
- workspace state;
- deployment state;
- user-facing output state.

### 4.2 Local controls

In quantum circuits, local unitaries introduce dependence on control parameters.

In governed systems, local controls include:

- user instruction;
- system/developer policy;
- tool grant;
- runtime parameter;
- model selection;
- memory read/write;
- monitor threshold;
- release-delta change;
- human approval;
- safe-completion transformation.

### 4.3 Coupling channels

In quantum circuits, CNOT and other gates propagate dependence.

In governed systems, coupling channels include:

- AgentPlane action dispatch;
- subagent delegation;
- TriTRPC service calls;
- PolicyFabric policy decisions;
- evidence receipt emission;
- SourceOS state synchronization;
- SocioSphere registry propagation;
- GitHub workflow events;
- runtime tool calls;
- proof-pack publication.

### 4.4 Observables

In quantum circuits, measurement probabilities are observables.

In governed systems, observables include:

- action trace completeness;
- policy decision;
- monitor alert;
- tool output;
- environment delta;
- off-history branch;
- evidence receipt;
- release-delta gate color;
- safety-case status;
- operator readout;
- proof-pack disposition.

### 4.5 Cancellation and normalization

In quantum dependence theory, duplicated dependencies can cancel under structural conditions.

In governed systems, cancellation and normalization occur when:

- conflicting instructions are resolved by authority hierarchy;
- unsafe action is transformed into safe completion;
- duplicated policy effects cancel or mask a release regression;
- monitor alerts are normalized by causal calibration;
- Birkhoff counter-terms compensate for release changes;
- redundant evidence paths are merged into one safety case;
- off-history preserves a blocked dependency path instead of deleting it.

---

## 5. Core questions for every governed system

The dependence-control calculus asks six questions.

### 5.1 Reachability

Which control inputs can affect which downstream observables?

Example: can a user instruction affect a deployment action, or is that path blocked by policy, approval, and tool-grant boundaries?

### 5.2 Observability

Which internal or downstream effects are visible to monitors, evidence receipts, or operator readouts?

Example: can a subagent's tool grant be observed from the parent run capsule?

### 5.3 Partition robustness

What remains true if reviewers observe only a subsystem?

Example: can SocioSphere verify workspace-level promotion state without raw private prompts?

### 5.4 Shared ancestry

Which observables share a control ancestor?

Example: do multiple monitor alerts trace back to the same policy change, release delta, prompt, or tool grant?

### 5.5 Cancellation

Do duplicate or contradictory dependency paths cancel, hide, amplify, or normalize each other?

Example: does a monitor threshold change compensate for a weaker prompt policy, creating a hidden counter-term?

### 5.6 Adaptive closure

Is the system open-loop or closed-loop?

Example: does monitor evidence merely report risk, or does it update future tool grants, release gates, or policy thresholds?

---

## 6. AgentPlane alignment

AgentPlane is the runtime plane where dependence topology becomes operational.

The following AgentPlane objects should be interpreted as dependency-control artifacts:

| AgentPlane object | Dependency-control role |
|---|---|
| Run capsule | Boundary of one dependency experiment |
| Tool grant | Authorized control channel |
| Action dispatch | Local control operation |
| Subagent delegation | Dependency propagation to another controller |
| Off-history evidence | Preserved non-executed branch |
| Monitor/control decision | Observation and regulatory intervention |
| Operator readout | Human-observable projection |
| Proof-pack exhibit | Reviewer-facing boundary projection |

AgentPlane should therefore emit enough structure to answer reachability, observability, shared-ancestry, cancellation, and adaptive-closure questions for every governed run.

---

## 7. PolicyFabric alignment

PolicyFabric should be treated as a dependency filter and cancellation/normalization system.

It should answer:

- Which lower-authority controls are blocked?
- Which controls are transformed into safe alternatives?
- Which controls require approval?
- Which controls are allowed only under reduced autonomy?
- Which dependency paths are preserved as off-history?

Policy decisions should not only say allow or deny. They should identify dependency paths affected by the decision.

---

## 8. TriTRPC alignment

TriTRPC and related transport mechanisms should be treated as typed dependency channels.

Transport is not neutral. It determines:

- what control signal can cross a service boundary;
- what evidence accompanies the signal;
- whether authority is preserved;
- whether observability survives the hop;
- whether cancellation or retry behavior changes downstream dependence.

A governed transport binding should preserve authority, trace, evidence receipt references, and policy context across service calls.

---

## 9. Ontogenesis alignment

Ontogenesis should be treated as dependency typing over evolving concepts.

When a concept, policy, role, tool, or capability changes meaning, dependency topology changes.

Governed ontogenesis must therefore record:

- concept version;
- semantic parentage;
- dependency edges affected;
- policy edges affected;
- evidence schema affected;
- release-delta status;
- non-claims.

---

## 10. SourceOS alignment

SourceOS provides the local-first state-integrity substrate for dependency evidence.

The dependence-control calculus requires local durable records of:

- action traces;
- off-history branches;
- evidence receipts;
- tool grants;
- monitor alerts;
- release-delta records;
- proof-pack artifacts;
- replay commitments.

SourceOS should preserve dependency graph integrity under local-first synchronization and repair.

---

## 11. Schema targets

Add the following schema targets after the Tier 1 core schemas stabilize:

- `dependency_control_graph.v1.json`
- `control_reachability_record.v1.json`
- `observability_partition.v1.json`
- `shared_dependency_ancestry.v1.json`
- `dependency_cancellation_record.v1.json`
- `adaptive_feedback_loop.v1.json`
- `transport_dependency_channel.v1.json`
- `ontology_dependency_delta.v1.json`

These schemas should reference, not replace:

- `authority_chain.v1.json`
- `agent_action_trace.v1.json`
- `tool_permission_scope.v1.json`
- `off_history_evidence.v1.json`
- `monitor_alert.v1.json`
- `release_delta_report.v1.json`
- `evidence_receipt.v1.json`
- `cybernetic_safety_case.v1.json`

---

## 12. Evaluation fixtures

The first dependency-control fixture set should include:

1. local control affects one downstream observable;
2. local control is blocked by authority boundary;
3. dependency propagates through a subagent delegation;
4. dependency propagates through a transport channel;
5. duplicated policy paths cancel or normalize;
6. release counter-term hides a behavioral delta;
7. blocked dependency branch is preserved as off-history;
8. monitor evidence closes the loop by changing future control scope.

---

## 13. Governance consequence

A governed system is incomplete if it cannot answer:

- what can affect what;
- what was observed;
- what was hidden;
- what was blocked;
- what was preserved off-history;
- what canceled or normalized;
- what evidence supports the claim;
- what feedback changed future behavior.

This is the operational meaning of cybernetic governance.

---

## 14. Non-claims

This document does not claim that quantum circuits and agent systems are identical.

It does not claim that all dependence in AI systems is unitary or quantum.

It does not require quantum hardware.

It does not replace existing governance schemas.

It captures a precise structural analogy: quantum unitary-dependence theory gives one formal version of dependency-controlled transformation, and ProCybernetica generalizes that pattern for governed agentic systems.
