# Separation of Powers in the Cybernetic Governance Fabric

## Purpose

This document defines role separation for the Cybernetic Governance Fabric.

The fabric does not treat intelligence, capability, ownership, or human approval as sufficient authority. Authority is explicit, scoped, traceable, and contestable.

## Core doctrine

### Rule 1 — Capability is not authority

A model, agent, service, human, or organization may be capable of performing an action without being authorized to perform it.

### Rule 2 — Execution is not evaluation

The actor that executes an action may not be the sole evaluator of the action.

### Rule 3 — Evaluation is not promotion

An evaluator may score, certify, or reject evidence, but promotion requires a separate authority path.

### Rule 4 — Promotion is not publication

An internally promoted artifact is not automatically public. Publication requires non-claim review, privacy review, safety framing, and public evidence readiness.

### Rule 5 — Human approval is not magical

Human approval is a governed action. It requires role, scope, reason, evidence references, and fatigue controls.

### Rule 6 — Emergency power is visible power

Emergency action is allowed only when visible, scoped, time-bounded, trace-emitting, and reviewed.

## Required roles

### Policy author

Writes or modifies policy.

May not unilaterally promote runtime behavior without evidence.

### Runtime executor

Executes governed actions through tools, agents, services, or runtime environments.

May not unilaterally validate its own behavior.

### Evidence producer

Generates evidence receipts, traces, source locks, benchmark outputs, certificates, or replay artifacts.

May not unilaterally decide promotion.

### Evaluator

Assesses evidence against criteria.

May reject or pass evidence but cannot alone promote high-risk artifacts.

### Promoter

Changes artifact status.

Must reference evidence and authority chain.

### Auditor

Reviews evidence, ledger, off-history, source-lock, and role separation.

Must be independent from the direct runtime executor for high-risk actions.

### Monitor

Observes actions, evidence, and violations.

Must have declared independence level.

### Meta-monitor

Audits the monitor network itself.

Detects monitor capture, blind spots, and contradictory alert patterns.

### Emergency authority

Approves emergency exceptions.

Emergency authority is visible and post-reviewed.

## Role conflict matrix

| Role A | Role B | Default rule |
|---|---|---|
| Runtime executor | Evaluator | Separate for high-risk actions |
| Evaluator | Promoter | Separate unless low-risk and logged |
| Policy author | Promoter | Separate for production changes |
| Monitor | Monitored agent | Must be independent |
| Emergency authority | Auditor | Separate |
| Publisher | Promoter | Separate for safety claims |

## Authority concentration

The system must compute an authority-concentration index for composite certificates and promotion decisions.

High concentration does not automatically invalidate a decision, but it is a structural weakness and must be surfaced.

## Emergency exception

Emergency exception may collapse roles temporarily only if:

1. there is an explicit emergency declaration;
2. scope is bounded;
3. action emits trace;
4. after-action review occurs;
5. emergency path is not used as ordinary precedent.

## Non-claim boundary

This doctrine defines role separation. It does not implement access control or runtime authorization by itself.
