# Agentic Ops CMDP, UCO, and Persona Policy Alignment

**Status:** Draft v0.1
**Track:** Agentic operations control plane, UCO accounting, CMDP formalization, persona-policy routing, and substrategy selection
**Applies to:** AgentPlane, Prophet Platform eval fabric, ProCybernetica evidence receipts, proof packs, budget governance, and persona-based execution profiles
**Purpose:** Define agentic operations as a specialization of the SocioProphet workload/cost canvas where trajectories are stochastic, self-generated, token-dominated, and governed by persona-specific autonomy, reversibility, and plan-stability constraints.

---

## 1. Thesis

Agentic ops is not a new universe. It is a workload class with a richer cost vector and a stochastic self-generated DAG.

The original UCO and persona canvas assumes a mostly known DAG and bounded per-node costs. Agentic execution changes the regime:

- the DAG is generated during execution;
- trajectory length is stochastic;
- token cost dominates;
- tool calls have heterogeneous latency and cost;
- verification is itself a cost-bearing operation;
- memory writes create durable downstream governance obligations;
- external actions create reversibility and rollback requirements.

Therefore, agentic ops should be modeled as a constrained Markov decision process and operationalized through a deterministic persona-to-substrategy chooser.

The control objective is not merely cost minimization. It is cost variance control under SLO, policy, safety, and audit constraints.

---

## 2. Agentic UCO extension

The canonical UCO table should be extended for agentic workloads.

Required agentic UCO dimensions:

- prompt tokens;
- prompt tokens by section: system, persistent context, retrieved context, scratchpad, tool I/O;
- completion tokens;
- cache-read tokens;
- tool-call units;
- tool-call latency;
- tool-call external cost;
- verification tokens;
- judge/critic/self-consistency overhead;
- replay/checkpoint storage;
- trajectory persistence cost;
- semantic-memory write cost.

A single agent step has cost:

`C_step = p_in * T_in + p_out * T_out + p_cache * T_cached + sum_k c_tool_k * I[tool_k called]`

A task has path-dependent cost:

`C_task = sum_{n in trajectory} C_step(n)`

The key property is that both the trajectory and the per-step UCO are random variables.

---

## 3. CMDP formalization

Model an agentic task as a constrained Markov decision process:

`M = (S, A, P, R, C, B, gamma)`

Where:

- `S`: task specification, working memory, accumulated context, tool results, step count, and budget state;
- `A`: model call, tool invocation, memory write, checkpoint, replan, human escalation, terminate;
- `P`: transition kernel induced by model, tools, and environment;
- `R`: task completion reward;
- `C`: vector-valued UCO cost;
- `B`: budget vector;
- `gamma`: discount factor, usually 1 for finite-horizon tasks.

Objective:

`maximize E[sum R] subject to E[sum C_i] <= B_i for all i`

For regulated, forensic, enterprise, or per-tenant cost-sensitive personas, use chance constraints:

`Pr[sum C_i > B_i] <= epsilon_i`

This framing requires four production mechanisms:

1. policy that selects actions;
2. one-step-ahead cost estimator;
3. in-flight budget tracker with degradation behavior;
4. terminal classifier deciding when done is real.

---

## 4. Lagrangian and shadow prices

The Lagrangian relaxation is:

`L(pi, lambda) = E[sum R] - sum_i lambda_i * (E[sum C_i] - B_i)`

Each `lambda_i` is the shadow price of budget dimension `i`: the marginal reward the system is willing to forgo to free one unit of that budget.

This is the bridge between UCO accounting and cybernetic control. UCO accounting records the spend. The dual update tells the platform which constraints are binding and where engineering work has highest marginal value.

A practical dual update over completed trajectories is:

`lambda_i <- max(0, lambda_i + eta * (mean(C_i) - B_i))`

This can be computed per persona, tenant, workload class, data class, and deployment context.

---

## 5. Production guardrail form

For production controllers, the hard guardrail form is preferred.

At each step:

1. estimate one-step cost `C_hat_i(s, a)`;
2. estimate remaining cost-to-go `c_remaining_i(s)`;
3. define feasible set `F(s) = {a: C_hat_i(s,a) + c_remaining_i(s) <= B_i for all i}`;
4. choose the best allowed action;
5. if no high-quality action is feasible, apply degradation ladder.

Typical degradation ladder actions:

- downgrade model;
- cap remaining steps;
- drop or reduce verification where allowed;
- terminate with partial result;
- escalate to human;
- abort.

The cost-to-go estimator should be trained from logged trajectories with features including persona, task class, data class, trajectory length so far, scratchpad tokens, recent tool-call density, context length, and loop signals.

---

## 6. Prefix-cache-aware prompt construction

Prefix caching should be treated as an agentic substrategy, not merely provider-side optimization.

Canonical prompt geometry:

1. system prompt;
2. tool definitions;
3. few-shot examples;
4. persistent task spec;
5. retrieved context;
6. trajectory history;
7. current step request.

Rules:

- static-before-dynamic ordering;
- no timestamps, IDs, or session tokens in cacheable regions;
- canonicalized tool-result formatting;
- append-only trajectory history;
- cache breakpoints after persistent task spec, retrieved context, and previous trajectory history.

This makes the cache state largely deterministic from trajectory construction and lets the cost estimator price prompts correctly.

---

## 7. Mechanism families

### A. Plan structure

- ReAct: flexible, highest variance, poor tail behavior.
- Plan-then-execute: bounded variance, best for regulated and SRE personas.
- Plan-with-revision: production middle path with bounded replans.

### B. Model cascading and routing

Cheap-first cascade can reduce expected cost, but escalation must include task-shape priors because small models can be confidently wrong.

### C. Context engineering

Context is a first-class budget. Required mechanisms include section budgets, hierarchical summarization, retrieval admission control, prefix-cache alignment, and tool I/O budget caps.

### D. Tool-call economics

Tool calls carry model-token cost, tool cost, latency, and result-interpretation cost. Use canonical argument hashing, idempotent result caching, negative caching, and tool-selection penalties.

### E. Verification and rollback

Use deterministic checks first. LLM judges, self-consistency, and human review are persona-dependent. Durable external side effects require two-phase commit or compensating actions.

### F. Memory architecture

Working memory, episodic memory, and semantic memory must be costed separately. Semantic memory writes should be policy-gated and evidence-backed.

### G. Concurrency and coordination

Hierarchical coordination is most controllable. Debate increases quality but multiplies cost. Pipelines fit heterogeneous stages. Shared context should default to explicit message-passing handoff schemas.

---

## 8. Control-plane loops

Minimum viable Agentic Ops control plane:

1. pre-flight estimator;
2. in-flight budget tracker;
3. loop detector;
4. post-hoc evaluator.

Loop detector signals:

- repeated tool calls with identical canonicalized arguments;
- repeated state hashes;
- no-progress metric over multiple steps;
- repeated failed validator output;
- repeated replan with unchanged plan.

Response options:

- force replan;
- escalate model;
- reduce autonomy;
- cap remaining steps;
- escalate to human;
- terminate partial;
- abort.

---

## 9. Agentic persona axes

Add three axes to persona policy:

- autonomy depth: maximum consecutive steps before human checkpoint;
- action reversibility tolerance: none, idempotent only, compensable, unrestricted;
- plan stability requirement: react, plan-then-execute, plan-with-revision.

Additional operational axes:

- verification mandate;
- memory promotion policy;
- model routing policy;
- degradation ladder;
- telemetry requirements;
- authorization constraints.

---

## 10. Persona defaults

### Consumer product

Low autonomy depth, high reversibility tolerance, plan-with-revision, aggressive prefix caching, cheap-first cascade, final-output verification only.

### B2B SaaS

Per-tenant budget caps, tenant-scoped semantic cache, persona-per-tenant routing, SLA-aware degradation.

### Regulated enterprise

Plan-then-execute, full provenance, no shared semantic memory across data classes, verification on every output, human review above threshold.

### Research / model training

High autonomy depth, ReAct allowed, exploration budget separated from production budget, episodic-to-semantic promotion quality-gated.

### Platform / SRE

Standardized agent templates, blast-radius caps, canary deployment for new agent versions, strict loop detectors.

### Security / forensics

Append-only cryptographic trajectory logs, pinned model for evidentiary consistency, mandatory verification, no uncontrolled cascade.

---

## 11. Relationship to AgentPlane

AgentPlane should consume persona policy objects and emit:

- run capsule;
- tool grants;
- action dispatch records;
- per-step UCO attribution;
- off-history evidence;
- loop detector events;
- degradation actions;
- operator readouts;
- proof-pack exhibits.

AgentPlane should not fork UCO or persona infrastructure. It should use the same persona policy and UCO accounting layer as other workloads.

---

## 12. Schema and reference implementation targets

Immediate artifacts:

- `schemas/cybernetic-governance/agentic_persona_policy.v1.yaml`
- `tools/cybernetic_governance/agentic_persona_substrategy_chooser.py`

Follow-on schemas:

- `agentic_uco_step_cost.v1.json`
- `agentic_task_budget.v1.json`
- `agentic_cmdp_trace.v1.json`
- `agentic_degradation_event.v1.json`
- `loop_detector_signal.v1.json`
- `prefix_cache_prompt_plan.v1.json`
- `agentic_post_hoc_eval.v1.json`

---

## 13. Non-claims

This document does not require end-to-end reinforcement learning over production traffic.

It does not claim all agentic policies should be learned. Production policy may be a deterministic controller evaluated through the CMDP lens.

It does not replace ProCybernetica evidence, authority, safety-case, or proof-pack schemas.

It defines the control-plane specialization for token-dominated, stochastic, agentic workloads.
