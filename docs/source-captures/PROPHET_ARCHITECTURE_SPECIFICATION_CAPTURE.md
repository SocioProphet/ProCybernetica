# Source Capture: ProCybernetica Volume II — Prophet Architecture Specification

Source title: `ProCybernetica_Volume_II_Prophet_Architecture_Specification.pdf`

Drive source: https://drive.google.com/file/d/17IqDDT_KCKG2_c5U2IFyFKJzM9okL0tG

Capture purpose: preserve the current normative architecture specification in GitHub so the public repository can build from the existing source state.

## Document identity

Volume II is titled `The Prophet Architecture Specification`.

Subtitle: `Controlplane law, fractal node contracts, repository constitutions, and the EpiCybernetic governance loop`.

It is described as a normative architecture manual for repositories, agents, processes, operators, tools, and embodied systems.

Version: 1.0, March 7, 2026.

## Abstract capture

Volume II converts the historical and theoretical survey of Volume I into a normative architecture specification for the Prophet ecosystem.

The central claim is that a durable intelligence fabric requires an explicit control contract that repeats across scales. That contract is the Fractal Node Contract.

Every repository, agent, process, service, robot, operator gateway, and supervisory controller is treated as a node with the same internal anatomy:

- observation;
- world modeling;
- value judgment;
- behavior generation;
- execution;
- memory;
- learning;
- coordination;
- observability.

The document uses ProCybernetica for constructive doctrine: how to build systems that perceive, remember, decide, coordinate, and act across levels.

It uses EpiCybernetica for epistemic doctrine: how to govern evidence, confidence, disagreement, provenance, learning, and policy change.

The volume is explicitly normative. `MUST` denotes binding architecture requirement. `SHOULD` denotes preferred practice whose omission requires rationale and compensating controls. `MAY` denotes optional feature.

## Roadmap captured

| Part | Title | Purpose |
| --- | --- | --- |
| 1 | Lineage compression and design axioms | What survived from earlier frameworks and why explicit architecture still matters |
| 2 | Fractal Node Contract | Universal node anatomy, memory split, world model, value loop, and execution law |
| 3 | Prophet Controlplane | Lifecycle supervision, authority tree, information graph, scheduling, and failure semantics |
| 4 | Repository constitutions | Semantic, episodic, policy, artifact, model, telemetry, simulation, and trust repositories |
| 5 | Agents, processes, and operators | Capability classes, delegation, handoff tokens, closure conditions, and human override |
| 6 | Planning stack composition | Where symbolic planning, BTs, POMDP, HMDP-MPC, RL, and VLAs fit |
| 7 | EpiCybernetica | Belief governance, disagreement handling, evidence, promotion, rollback, and learning admission |
| 8 | Evaluation and conformance | Replay, simulation, shadow mode, incident review, and conformance scorecard |
| Appendix A | Canonical schemas and message envelopes | Machine-oriented schema fragments |
| Appendix B | Node-class templates and command vocabularies | Implementation templates and role vocabularies |

## Design axioms

The Prophet architecture is synthetic. It does not reject older frameworks as obsolete. It compresses surviving lessons from subsumption, RCS/4D-RCS, Soar, ACT-R, ROS 2, Nav2, PlanSys2, POMDPs, HMDP-MPC, reinforcement learning, and foundation-model robotics.

Key axioms:

1. No component is too small to deserve a contract, and no component is too large to be exempt from one.
2. Repositories, agents, processes, planners, policy engines, simulation runners, robot controllers, and operator consoles all become nodes.
3. Memory is not truth. Every memory write carries provenance, freshness, trust, and retention semantics.
4. Planning formalisms are tools, not religions. Symbolic planners, BTs, POMDPs, HMDP-MPC, RL, and VLAs each dominate different operating regions.
5. Cybernetic consciousness must be operationalized as self-model, world model, value model, temporal memory, reflexive reporting, and policy-bound learning.

## Fractal Node Contract

A node is any unit that receives observations, maintains state, evaluates goals and constraints, generates action or write, and can be supervised.

Nodes differ by embodiment rather than constitutional status.

Conforming nodes must expose six external surfaces:

1. identity surface;
2. interface surface;
3. lifecycle surface;
4. memory surface;
5. policy surface;
6. observability surface.

Internally, every node must:

1. observe;
2. update local world model or belief state;
3. evaluate utility, policy, risk, and uncertainty;
4. generate or revise plan;
5. execute command prefix or transactional write;
6. record result as durable evidence;
7. report state upward and laterally;
8. optionally learn under learning budget and promotion path.

## Mandatory memory split

| Tier | Typical horizon | Contents | Repository behavior |
| --- | --- | --- | --- |
| Immediate experience | seconds to minutes | raw observations, live transactions, active prompts, open tool calls | fast, append-heavy, aggressively expired |
| Working memory | minutes to sessions | active entity graph, hypotheses, plan fragments, conflicts, running summaries | mutable, query-rich, versioned |
| Long-term memory | days to years | policies, documents, semantic graph, episodes, models, simulations | durable, indexed, provenance-heavy |

The source explicitly says a system that stores everything in one vector store or message bus does not satisfy the specification.

## Controlplane law

The controlplane is not just an orchestrator or scheduler. It is the supervisory fabric that admits nodes, assigns authority, routes policy, observes health, arbitrates handoffs, and degrades/recovers/quarantines nodes.

The controlplane preserves the distinction between authority tree and information graph.

Every node has one supervisory parent at a time, though parents may delegate limited authority via a delegation token.

Authority grants must specify:

- scope;
- budget;
- deadlines;
- rollback rights;
- artifact requirements;
- override conditions.

Information visibility must not be treated as implicit command authority.

## Temporal execution classes

| Execution class | Cadence | Examples | Primary recovery |
| --- | --- | --- | --- |
| Class A | 1 ms - 100 ms | safety guards, actuator loops, write integrity checks | immediate fail-safe or local recovery |
| Class B | 100 ms - seconds | BT ticks, local planners, transaction executors | retry, alternate branch, supervisor alert |
| Class C | seconds - minutes | mission coordination, delegation, artifact synthesis | replan, handoff, queue reorder |
| Class D | minutes - hours | evaluation, model promotion, policy review | batch reschedule or operator review |

## Delegation token

Delegation is not authority transfer. A delegation token gives a receiver bounded rights to act on behalf of an issuer inside a restricted problem slice.

The token carries:

- issuer;
- receiver;
- goals;
- command prefixes;
- repository scope;
- embodied targets;
- max cost;
- max risk;
- max duration;
- write set;
- required artifacts;
- explanation level;
- replay requirement;
- rollback owner;
- compensation policy;
- policy refs;
- expiry.

## Repository constitutions

A repository in Prophet is not a bucket. It is a governed memory organ.

Each repository class has command vocabulary, consistency regime, replication rules, and admissibility policy.

Repository classes:

- Semantic;
- Episodic;
- Artifact;
- Policy;
- Telemetry;
- Model;
- Simulation;
- Identity-Trust.

Each repository must define admission, retention, conflict, replication, and promotion law.

Every durable write must carry provenance, timestamps, and acting principal or node.

Policy repositories require staged activation and rollback, not overwrite semantics.

Model repositories must not permit promotion without evaluation evidence linked to the model artifact.

## Repository write envelope

The source defines a `RepositoryWriteEnvelope` with:

- write_id;
- target_repo;
- operation;
- subject_keys;
- payload_ref;
- created_by;
- acting_node;
- source_ref;
- event_time;
- write_time;
- provenance_chain;
- trust_basis;
- retention_class;
- freshness_horizon_s;
- policy_refs;
- conflict_policy.

## Agents, processes, and operators

The source sharply distinguishes:

- agent: adaptive problem-solving under delegated intent;
- process: reliable state progression through workflow;
- operator gateway: human-system coupling, intent capture, display, override, and after-action interpretation.

Agent classes:

- scout;
- synthesis;
- planner;
- verifier;
- tool;
- steward.

Process classes:

- promotion;
- publication;
- incident review;
- deployment;
- reconciliation.

Operator gateways are first-class constitutional organs, not last-resort patches.

Completion is defined by artifact and side-effect closure, not by narrative verbosity.

## Planning stack composition

No single planner is sovereign.

Planner allocation:

| Method | Assigned horizon | Strength | Weakness |
| --- | --- | --- | --- |
| Symbolic planner | strategic and supervisory | explicit decomposition, resource/precondition reasoning | brittle under hidden state or poor models |
| Behavior tree | execution and recovery | clear sequencing and fallback | runtime semantics must be pinned |
| POMDP / belief planner | task layer under uncertainty | contingency reasoning with hidden state | modeling and computation cost |
| HMDP-MPC / MPC | task-to-primitive and local control | constraints and continuous optimization | requires dynamics and costs |
| RL policy | primitive/local or proposal layer | learned performant behavior | hard to validate and data hungry |
| VLA / foundation model | perception, proposal, broad reasoning | semantic generalization and dexterity priors | opaque failure modes and evaluation burden |

Learned policies and VLAs may propose or execute actions only within policy envelopes and with replay visibility.

## EpiCybernetica

ProCybernetica governs how the system acts. EpiCybernetica governs how the system is allowed to believe.

Principles:

1. provenance completeness;
2. confidence discipline;
3. disagreement as signal;
4. promotion law;
5. learning budgets.

Epistemic incident taxonomy:

| Code | Incident type | Meaning |
| --- | --- | --- |
| E1 | Provenance gap | durable belief or artifact lacks basis trace |
| E2 | Freshness violation | belief used outside freshness horizon |
| E3 | Confidence misuse | incompatible confidence values fused or misinterpreted |
| E4 | Promotion error | policy or model entered active state without complete evidence |
| E5 | Unauthorized drift | node adapted beyond learning budget or policy scope |
| E6 | Explanation failure | system cannot reconstruct why high-impact action occurred |

## Evaluation, replay, and conformance

Architectures that cannot be replayed cannot be trusted.

Architectures that cannot be shadowed cannot be safely promoted.

Important action paths must be testable through:

1. isolation;
2. simulation;
3. closed-loop scenario playback;
4. shadow mode against live traffic;
5. limited-authority deployment.

Conformance ladder:

| Level | Meaning | Minimum requirements |
| --- | --- | --- |
| Level 0 | Node contract only | identity, interfaces, lifecycle surface |
| Level 1 | Operational traceability | provenance on writes, health, failure semantics |
| Level 2 | Replay capable | replay bundle emission and reconstruction |
| Level 3 | Epistemically governed | promotion law, confidence discipline, disagreement handling |
| Level 4 | Adaptive under constitution | learning budgets, monitored online adaptation, rollback readiness |

## Evaluation profile

Core metrics:

- action success;
- recovery efficacy;
- replay completeness;
- explanation completeness;
- confidence calibration;
- operator burden;
- policy hygiene.

## Operational cybernetic consciousness

The source uses cybernetic consciousness operationally, not metaphysically.

Minimum requirements:

1. self-model;
2. world model;
3. value model;
4. temporal continuity through memory and replay;
5. report channel for important action paths;
6. adaptation only through explicit epistemic constitution.

## Canonical schema fragments in appendix

Appendix A includes fragments for:

- CommandSpec;
- ObservationEnvelope;
- StatusEnvelope;
- ArtifactEnvelope;
- PolicyEnvelope;
- GoalEnvelope;
- LearningBudget.

Appendix B includes node-class templates and command vocabularies for:

- repository steward node;
- planner node;
- execution node;
- operator gateway node;
- model steward node;
- minimal command vocabulary by level.

## Recommended rollout sequence

1. Node census and lifecycle surfaces.
2. Provenance on durable writes.
3. Memory-tier separation and repository constitutions.
4. Process ownership for critical workflows.
5. Replay bundles and shadow mode.
6. Pinned command vocabularies and execution semantics.
7. Belief governance and promotion law.
8. Learning budgets and adaptive rollout.

## Closing claim

The document closes by saying the next logical artifact is a machine-readable specification pack: schemas, protocol buffers, repository DDL, event taxonomies, BT semantic profiles, promotion workflows, and a conformance test harness.

The more capable the parts become, the more dangerous it is to leave the whole implicit.

## Codification implications

This source is the main driver for:

- full schema suite;
- command/observation/status/artifact/policy envelopes;
- delegation token schema;
- repository write envelope;
- lifecycle and controlplane profiles;
- conformance ladder;
- operator override record;
- planning stack profile;
- epistemic incident taxonomy;
- rollout sequence.

## Capture status

Captured into GitHub as structured source-state. This is not a replacement for the original Drive PDF. It is the repo-local normative architecture capture used to make ProCybernetica self-contained enough to build from.
