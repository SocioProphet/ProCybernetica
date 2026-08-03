# ADR-0003: Governed closed-loop control contract (the system that maintains itself)

**Date:** 2026-08-03
**Status:** decided — contract + teeth adopted 2026-08-03
**Context:** set-3 P0 "governed closed-loop AIOps control plane — the system that builds and maintains itself." Seats under the estate cybernetics control plane; measurement/design only (no runtime remediation ships here).

---

## Decision

Formalize self-maintaining Day-0/1/2 operations as a **governed `ControlLoop` record**
(`contracts/control-loop.schema.json`), admitted only when it *closes* the cybernetic loop
under the estate constitution:

> **sense** (Sensory / drift · conformance · flow signal) →
> **model** (WorldModel / KnowledgeDB reference) →
> **judge** (ValueJudgment policy gate) →
> **act** (TaskExecutor remediation) →
> **receipt** (audit evidence).

This is the union of the recurring self-maintaining-ops patterns — Telco Day-0/1/2, the
MLOps drift/quality/bias monitor, process-mining discover→conform→predict→act, and the
digital-twin autonomy arc (Virtualization → … → Autonomous-Optimization) — expressed as **one**
typed, gated record rather than N bespoke automations.

### Home: ProCybernetica

ProCybernetica **owns the ControlNodes** (#124, the 11 Fractal-Control-Fabric node types) that
a `ControlLoop` instantiates, and already carries the adjacent substrate: the
`contracts/governance-loop.schema.json` contract, `schemas/cybernetic-governance/`
(`adaptive_feedback_loop`, `evidence_receipt`, `monitor_alert`, `enums` constitutional
invariants), a `docs/adr/` sequence, and a mature stdlib validator+pytest harness. The RCS/4D
ADR-0003 vocabulary (ValueJudgment/WorldModel/KnowledgeDB/Sensory/TaskPlanner/TaskExecutor)
is **owned by prophet-workspace#113** and is **referenced, not forked** (consume-not-fork):
`control_node_type` and the sense→model→judge→act structure bind upward to it.

## How it seats under the existing planes (bind-upward)

| Upstream authority | Binding in this contract |
|---|---|
| **ControlNodes #124** (Fractal-Control-Fabric) | `control_node_type` enumerates the 11 node roles; each loop declares which it instantiates. |
| **RCS/4D ADR-0003** (prophet-workspace#113) | The record's five parts are exactly sense(`sensor`)→model(`world_model_ref`)→judge(`value_judgment`)→act(`actuator`)→receipt(`audit_receipt`). |
| **Crown / Telos-Truth-Engine** (hellgraph#52) | K1: a `control-max`/`domination`/`unbounded-optimization` objective is **rejected** — no loop may pursue a domination objective. (D1 is respected structurally: a loop is not a truth-asserting authority; it acts on measured signal + policy, never asserts truth.) |
| **agent-cognition ER** (prophet-workspace#115) | ACTION `gated_by` POLICY_CHECK + `recorded_as` AUDIT_EVENT ≡ `actuator` gated by `value_judgment` + carried by `audit_receipt`. |
| **enums.v1.json constitutional invariants** | `implements_invariants` binds each loop to `invariant_0_2_no_action_without_trace`, `invariant_0_5_separation_of_powers`, `invariant_0_6_monitor_independence`, etc. |

## Teeth (both directions)

Enforced by `tools/cybernetic_governance/validate_control_loop.py`, exercised by
`tests/test_control_loop_contract.py`, with positive+negative fixtures under
`tests/fixtures/control-loop/`:

1. **No ungoverned autonomy** — a `ControlLoop` with **no ValueJudgment gate** is REJECTED
   (`NO_VALUE_JUDGMENT_GATE`).
2. **No action without trace** — a fired remediation with **no `audit_receipt`** is REJECTED
   (`NO_AUDIT_RECEIPT_ON_FIRED`; invariant_0_2).
3. **Crown K1** — a **control-max / domination / unbounded** objective is REJECTED
   (`UNCONSTITUTIONAL_OBJECTIVE_CROWN_K1`), fired or not.
4. **Separation of powers** — a remediation that **fired while the judge denied** is REJECTED
   (`JUDGE_DENIED_BUT_FIRED`; invariant_0_5).
5. **No spurious action** — a remediation that **fired without its sensor signal crossing
   threshold** is REJECTED (`SPURIOUS_ACTION_NO_THRESHOLD_CROSS`).
6. **Closed loop VERIFIES** — sense→model→judge→act→receipt with a coherent, bounded objective,
   a crossed threshold, an `allow` verdict, and a receipt is ADMISSIBLE.
7. **No over-rejection** — a passive monitor loop that observes below threshold and does **not**
   act is ADMISSIBLE (the gate governs *action*, not *observation*).

## Consequences

- The contract is **measurement/design only**: it certifies admissibility of a proposed loop; it
  dispatches no actuator and emits no production telemetry. Runtime enforcement is a downstream
  binding (a control-plane service consuming this contract), out of scope here.
- Reason codes are stable identifiers so reviewers and downstream gates assert on *why* a loop is
  inadmissible, not on prose.
- Every automated act in the estate that claims to be "self-healing" now has one place to be
  proven governed before it is allowed to close its loop.

## Alternatives considered

- **Home in prophet-workspace** (owns the RCS ADR): rejected — its `contracts/` and `schemas/`
  are the personal-workspace plane (mail/calendar/tasks/file-naming), not a cybernetics contract
  substrate; and ControlNodes (#124), which the loop instantiates, live in ProCybernetica. We
  reference the RCS ADR upward instead of relocating or forking it.
- **Extend `governance-loop.schema.json` in place**: rejected — the governance loop is the
  OODA-style *decision-authority/escalation* record; the ControlLoop is the *sense→act with
  audit* record. They compose (a ControlLoop's `value_judgment` can escalate into a governance
  loop) but conflating them would blunt both sets of teeth.
