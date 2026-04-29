# Source Capture: ProCybernetica / Prophet Ecosystem Controlplane Technical Paper

Source title: `ProCybernetica_Prophet_Controlplane_Technical_Paper`

Drive source: https://docs.google.com/document/d/1ldF5xTQkrLyIQXg29jViYDShhPbHAf5jg1DbEvES_II

Capture purpose: preserve the current doctrinal and architectural state of the founding controlplane paper inside the public GitHub repository, so the repo can build from the existing work rather than reconstruct it from memory.

## Document identity

The paper is titled `ProCybernetica / Prophet Ecosystem Controlplane` and is described as a technical design paper prepared in March 2026 as a founding design document for the Prophet Ecosystem, ProCybernetica, and EpiCybernetica.

The subtitle frames the paper as integrating 4D/RCS, classical cognitive architectures, modern robotics middleware, probabilistic control, foundation-model robotics, and world-model design into the Prophet Ecosystem Controlplane.

## Abstract capture

The paper integrates historical and modern control, cognition, robotics, and embodied-AI frameworks into one architectural doctrine for the Prophet Ecosystem and its controlplane.

Its starting point is the NIST 4D/RCS reference model. It then compares reactive control, cognitive architectures, modern robotics middleware, behavior-tree execution, symbolic planning, probabilistic decision making, model predictive control, reinforcement learning, world models, and vision-language-action systems.

The core inherited idea from 4D/RCS is the repeated control node: a recurring architecture that fuses observation, world modeling, valuation, planning, execution, memory, and coordination across multiple time scales.

Modern practice adds lifecycle management, explicit execution scheduling, plugin modularity, behavior-tree recovery, probabilistic belief tracking, receding-horizon optimization, learned priors, foundation models, and synthetic-data loops. The paper argues that modern stacks often lack a unifying doctrine for where these pieces belong.

The synthesis is named ProCybernetica. It is the operational cybernetic framework for the Prophet Ecosystem. EpiCybernetica is the epistemic layer that critiques, updates, calibrates, and governs the operational fabric.

The engineering target is cybernetic consciousness in a non-phenomenological sense: a system that maintains a self-model and world-model, allocates attention, stores memory across time scales, evaluates value and risk, plans and acts under policy constraints, explains itself, and revises its own models.

## Executive thesis

The strongest modern autonomy architecture is not a single planner, policy, or foundation model. It is a disciplined control fabric that keeps the 4D/RCS decomposition explicit while allowing modern probabilistic, optimization, and learned modules to fill internal slots.

The Prophet Ecosystem should therefore be built as a hierarchy-and-graph of fractal control nodes, not as an unstructured swarm of agents or a collection of passive services.

## Problem statement

The system design must scale from repositories and reasoning agents to long-running processes, embodied robots, operator consoles, and supervisory governance.

It must survive partial observability, limited compute, asynchronous events, failures, uncertain models, policy constraints, and multi-time-scale objectives.

The dominant failure mode named in the paper is fragmentation: one team builds retrieval, another builds agent orchestration, another adds behavior trees, another adds reinforcement learning, another adds a VLA, and the result becomes accretion rather than doctrine.

The remedy is to view every component as a control node with a common anatomy, made lifecycle-managed, schedulable, observable, policy-governed, and testable under replay and simulation.

## Architectural lineage captured

The paper treats 4D/RCS as the strongest architectural ancestor. The decisive insight is repeated node anatomy across hierarchy levels. Higher levels reason over longer horizons and larger scopes. Lower levels handle immediate details and execution. The architecture separates command hierarchy from information network: authority remains structured, while data exchange may be richer and more lateral.

The paper captures subsumption architecture as the reflex-layer reminder: fast reactive behavior must remain available even if higher cognition fails.

It captures Soar and ACT-R as sources for operator-centered deliberation, working buffers, memory modularity, and human-facing cognitive design cues.

It captures ROS 2 as production runtime discipline: managed lifecycle, lifecycle states, external supervision, executors, callbacks, services, timers, subscriptions, and action management.

It captures Nav2 and behavior trees as modern modular execution and recovery grammar, while warning that behavior-tree semantics must be fixed and testable.

It captures PlanSys2 as symbolic planning for typed goals, resources, action preconditions, and explicit task decomposition.

It captures POMDPs as belief-state planning under uncertainty, MPC as local constrained receding-horizon optimization, reinforcement learning as learned priors/skills/proposals under governance, and foundation-model robotics/VLA systems as grounding/proposal engines that still require typed safety and control wrappers.

## ProCybernetica doctrine

The Prophet Ecosystem should be built around a single universal contract: every meaningful component is a node.

A repository is a node whose actuators include writes, commits, merges, retractions, replications, index updates, and quarantine actions.

An agent is a node whose actuators include tool invocations, messages, patches, proposals, and delegations.

A process runner is a node whose actuators include job starts, checkpoints, retries, compensations, and handoffs.

A robot or embodied subsystem follows the same contract with physical sensors and actuators.

The node shape remains stable. Embodiment changes.

## Design axioms captured

1. Every component is a node with explicit lifecycle, interfaces, memory, world model, value judgment, behavior generation, execution, learning, coordination, and observability.

2. Authority flows through a typed hierarchy; information flows through a richer graph. These planes must not be collapsed.

3. Every node owns local world state and writes to shared memory with provenance, timestamps, confidence, and policy context.

4. Behavior trees own execution and recovery; symbolic planning owns explicit task decomposition; POMDP and MPC are inserted where uncertainty or constraints dominate; learned models provide priors, proposals, perception, and adaptive policies.

5. The final safety boundary is explicit and typed. No learned model directly owns the last line of irreversible actuation without constraint wrappers, rollback logic, and operator override.

## Foundational substrate and projection discipline

The paper defines the Prophet ecosystem as a constrained world-model substrate:

```text
W = (S_dur, S_act, Theta, T, C, Pi, E)
```

Where:

- `S_dur` is durable state: persistent records, repositories, accepted memory, policy bundles, schemas, model artifacts, and long-lived world-state commitments.
- `S_act` is active state: working memory, open plans, running processes, uncommitted proposals, pending actions, current task graphs, and live execution context.
- `Theta` is the order bundle governing admissible ordering of transitions and commitments.
- `T` is the transition algebra of lawful state changes.
- `C` is the family of policy, safety, legal, resource, and embodiment constraints.
- `Pi` is the projection family of narrower regime models.
- `E` is the evidence layer of provenance, replay, attestation, incidents, and constitutional receipts.

The Fractal Node Contract is a lawful embodiment of this substrate, not an isolated software pattern.

Time is treated as order structure for constrained transformation, not merely scheduler clock time.

No node-local world state, repository view, planner belief state, or embodied controller state is sovereign over the whole ecosystem. Each is a projection of a richer substrate.

EpiCybernetica must distinguish disagreement caused by evidence difference, frame difference, ontology mismatch, and policy or authority conflict.

## Universal Fractal Node Contract capture

The source paper gives this node anatomy:

```yaml
FractalNode:
  identity:
    node_id
    node_class: repository | agent | process | sensor | planner | executor | gateway
    level: strategic | supervisory | task | primitive | actuator
    embodiment: software | data | robotic | human-interface
    authority_parent
    peer_groups

  lifecycle:
    state: unconfigured | inactive | active | degraded | recovery | finalized
    supervisor
    health
    admission_policy

  interfaces:
    command_vocabulary
    observation_schema
    status_schema
    artifact_schema
    policy_schema

  memory:
    immediate_experience
    working_memory
    long_term_memory
    provenance_log
    replay_log

  world_model:
    local_state
    belief_state
    entities_relations
    context_window_or_maps
    predictions
    confidence

  value_judgment:
    objective_weights
    risk_model
    trust_model
    policy_constraints
    resource_model
    utility_estimator

  behavior_generation:
    task_decomposer
    planner
    replanner
    recovery_policies
    handoff_policies

  executor:
    action_runner
    feedback_controller
    safety_guard
    rollback_or_compensation

  learning:
    adaptation_policy
    update_budget
    offline_training_hooks
    online_calibration_hooks

  coordination:
    upward_status
    downward_commands
    peer_queries
    shared_blackboard_refs

  observability:
    traces
    metrics
    explanations
    incident_records
```

The contract is close to 4D/RCS but updated with lifecycle, policy, provenance, and learning hooks.

## Memory model

Immediate experience stores hot observations, raw events, open transactions, and not-yet-stabilized estimates.

Working memory stores the current active state graph, focus of attention, plan prefixes, conflicts, and short-horizon expectations.

Long-term memory stores ontologies, schemas, tools, documents, learned models, embeddings, action histories, formal cases, and accepted policies.

This split is meant to prevent control from dissolving into one giant undifferentiated store.

## Authority plane versus information plane

Commands, priorities, resource budgets, and authorizations belong to the authority plane.

Queries, observations, events, explanations, and shared state belong to the information plane.

This distinction prevents both centralization failure and agentic anarchy. It makes command authority auditable even when information sharing is broad.

## Mathematical control loop

The paper gives a discrete-time cybernetic loop:

```text
observe: o_t = Sense(raw_t)
predict: b^-_t = F(b_{t-1}, a_{t-1}, K_t)
update: b_t = U(b^-_t, o_t, peer_t, K_t)
score: J(P | b_t, G_t, C_t, Pi_t)
plan: P*_t = argmin_{P in feasible_plans} J(...)
execute: a_t = Exec(prefix(P*_t), b_t, safety_guard)
learn: K_{t+1} = Adapt(K_t, trace_t)
report: s_t = Summarize(b_t, P*_t, a_t, confidence, risk, provenance)
```

The objective decomposes into goal, safety, risk, resource, latency, uncertainty, policy, handoff, and terminal costs.

POMDP machinery can inhabit belief update and uncertain planning. MPC can inhabit local execution and constraint satisfaction. BTs can own prefix execution and recovery. RL and foundation models can propose policies, predict costs, or supply learned dynamics. The node contract remains intact.

## Node classes and command vocabularies

| Node class | Primary world state | Typical command verbs | Primary risk |
| --- | --- | --- | --- |
| Repository | facts, schemas, artifacts, lineage | put_fact, retract, branch, commit, merge, quarantine | stale or conflicting truth |
| Agent | task context, tools, beliefs, pending actions | decompose, query, propose, patch, delegate, explain | hallucination or misdelegation |
| Process | job state, retries, resource budgets | start, checkpoint, retry, compensate, abort | partial completion or deadlock |
| Embodiment | pose, environment, constraints, mode | go_to, inspect, pick, place, stop, recover | physical or safety failure |

## Evaluation, replay, and incident review

A control architecture is not serious until it is testable.

Every node should emit replayable traces, policy context, confidence intervals, action proposals, selected actions, and resulting deltas.

The controlplane should support four evaluation modes:

1. offline replay on historical traces;
2. simulation with environment perturbation;
3. shadow mode against production traffic;
4. controlled live execution with automatic incident capture.

This is how EpiCybernetica gains evidence for updating the fabric.

## Design-pattern catalog

The paper defines a pattern language:

- P1 Fractal Node;
- P2 External Supervisor;
- P3 Split Planes;
- P4 Typed Verbs;
- P5 Three-Tier Memory;
- P6 Belief-State World Modeling;
- P7 Behavior-Tree Execution Grammar;
- P8 Optimization Plugins;
- P9 Learned Priors Under Governance;
- P10 Repository as Active Node;
- P11 Replay Before Promotion;
- P12 Epistemic Revision Loop;
- P13 Substrate Ontology;
- P14 Order as Constrained Transformation;
- P15 Projection Discipline;
- P16 Hypergraph Meaning;
- P17 Contradiction Curvature;
- P18 Re-Anchoring Before Drift;
- P19 Typed Tri-State Tension;
- P20 Namespace Discipline.

## EpiCybernetica capture

ProCybernetica is operational doctrine. EpiCybernetica is epistemic doctrine.

ProCybernetica says how the system observes, models, values, plans, acts, and coordinates.

EpiCybernetica says how the system questions assumptions, recalibrates confidence, revises ontologies, updates policies, promotes or rejects learned changes, and improves through evidence.

Without EpiCybernetica, the operational fabric hardens into dogma. Without ProCybernetica, epistemic reflection has nothing stable to govern.

## Implementation roadmap captured from appendix

1. Formalize schemas: node schema, status schema, command vocabularies, provenance records, replay traces, policy envelopes.
2. Build base runtime: lifecycle supervisor, execution manager, event bus, blackboard interfaces, repository node classes.
3. Add planners and controllers: BT runtime, symbolic planner integration, uncertain planning plugin, local MPC or constrained execution layer.
4. Add learning and epistemic governance: calibration metrics, incident capture, replay harness, shadow mode, promotion policy, model registry.
5. Add foundation-model integration: VLA or embodied reasoning adapters with strict typed verbs and policy wrappers.
6. Validate under embodiment diversity: pure software agents, repository-driven workflows, long-running processes, and physical or simulated robots.

## Codification implications

This source supports the following GitHub artifacts:

- `docs/PROGRAM_CAPTURE.md` for program-level thesis;
- `docs/INTEGRATION_MAP.md` for ecosystem mapping;
- `schemas/node_descriptor.schema.json` for node contract;
- `schemas/replay_envelope.schema.json` for replay law;
- `schemas/evaluation_result.schema.json` for evaluation evidence;
- `schemas/promotion_decision.schema.json` for promotion/quarantine decisions;
- `profiles/controlplane_state_machine.yaml` for lifecycle supervision;
- future source captures for BT semantics, Genesis/Inception, policy envelopes, and repository-as-node governance.

## Capture status

Captured into GitHub as a structured source-state document. This is not a replacement for the original Drive document; it is the repo-local codification capture used to make ProCybernetica self-contained enough to build from.
