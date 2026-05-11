# Constitutional Invariants for the Cybernetic Governance Fabric

## Purpose

This document defines the Tier 0 invariants for ProCybernetica’s Cybernetic Governance Fabric.

These invariants precede schemas. Schemas are statutes; invariants are constitutional law. No future schema, workflow, promotion process, runtime, monitor, emergency mechanism, or release pipeline may violate them.

## Scope

The invariants govern any system that can:

- act through tools;
- transform model or agent state;
- promote artifacts;
- issue safety claims;
- produce evidence receipts;
- approve irreversible action;
- operate monitors;
- publish claims externally.

## Constitutional vocabulary

A **governed node** is a model, agent, runtime, tool, monitor, policy engine, human approval role, or composed system that participates in governed behavior.

A **governed action** is an action whose execution may affect state, authority, evidence, users, external systems, release posture, or public claims.

An **authority** is an explicitly declared right to approve, deny, execute, observe, modify, promote, publish, or revoke.

**Evidence** is a digital record sufficient to support replay, audit, rejection, or promotion. Prose may explain evidence but cannot replace it.

A **promotion** is a change in certified status: from candidate to accepted, from internal to published, from test to production, or from lower autonomy to higher autonomy.

**Off-history** is the record of rejected, blocked, rolled back, or not-executed branches. Off-history is evidence, not trash.

## Invariant 1 — Separation of powers

Capability is not authority.

A node that can perform an action is not thereby authorized to perform it. The system must separate at least these roles:

- policy author;
- runtime executor;
- evaluator;
- promoter;
- auditor;
- monitor;
- emergency override authority.

A single actor may hold multiple roles only when that concentration is explicitly recorded and justified.

## Invariant 2 — No promotion by prose

No artifact may be promoted by explanation alone.

Promotion requires machine-addressable evidence: test output, trace, hash, receipt, certificate, replay plan, safety case, or other declared evidence object.

Human judgment may accept or reject evidence, but it may not substitute for evidence.

## Invariant 3 — No action without trace

Every governed action must emit a trace.

At minimum, the trace records:

- actor;
- authority invoked;
- inputs;
- outputs;
- tool scope;
- time;
- evidence references;
- approval state;
- rollback or off-history record when applicable.

If an action cannot be traced, it must not be executed in a governed lane.

## Invariant 4 — Evidence is digital-only

Governance evidence must be digitally addressable.

Oral assurance, memory, screenshots without source, and informal summaries may support orientation but cannot be promotion evidence.

Evidence may be human-authored, but it must be stored, hashed, and referenced.

## Invariant 5 — No hidden authority lane

Every authority path must be visible.

No private side channel may approve, suppress, override, or promote outside the declared authority graph.

Emergency authority is allowed only if it is visible, logged, bounded, and reviewed after use.

## Invariant 6 — Irreversibility requires approval

Actions that are irreversible or costly to reverse require approval proportional to risk.

Examples:

- production release;
- public safety claim;
- destructive action;
- external network action;
- user-affecting policy change;
- permanent data deletion;
- autonomy-tier increase.

Irreversibility must be part of the action schema, not inferred after execution.

## Invariant 7 — Monitor independence from agent

A monitor must not be solely controlled by the actor it monitors.

A monitor may observe agent state, but the monitored agent must not be able to silently disable, rewrite, or selectively blind the monitor.

Monitor independence is not binary. It must be represented as an assurance level.

## Invariant 8 — Off-history retention

Rejected candidates, failed checks, blocked actions, and superseded certificates are retained.

The off-history is essential for calibration, audit, anti-Goodhart defense, and failure analysis.

Deleting rejected evidence creates governance blindness.

## Invariant 9 — Privacy and evidence minimization

The system records enough evidence to audit claims, but no more private data than necessary.

Evidence minimization is not evidence deletion. It means the trace should preserve commitments, hashes, summaries, redactions, or zero-knowledge receipts when raw data exposure is unnecessary.

## Invariant 10 — Emergency power is visible power

Emergency actions must be:

- explicitly labeled;
- scoped;
- time-bounded;
- trace-emitting;
- reviewed after use;
- excluded from ordinary promotion precedent unless separately ratified.

Emergency authority cannot become a hidden normal path.

## Invariant 11 — Anti-Goodhart discipline

No metric may be used as the sole promotion criterion once it becomes a target.

Any promotion metric requires:

- adversarial test coverage;
- blind or held-out evidence where possible;
- off-target audit;
- metric-gaming failure mode;
- review cadence.

## Invariant 12 — Supply-chain assurance

Governed behavior depends on code, data, models, prompts, policies, schemas, and runtime dependencies.

Every promotion must identify the relevant supply-chain boundary and record source-lock information for artifacts used in the claim.

## Invariant 13 — Human approval is not magical

Human approval is itself a governed action.

Approvals require role, scope, reason, evidence references, conflict-of-interest state, and fatigue/overload risk when approval volume is high.

## Invariant 14 — Runtime and publication are distinct

A result may be internally valid but not publishable.

Publication requires additional review for clarity, non-claim boundary, safety disclosure, privacy, and public trust.

## Invariant 15 — Governance is compositional

Sub-certificates compose into higher-level certificates only through declared interfaces.

A composed safety claim must preserve the limitations and non-claims of its constituents.

## Definition of constitutional compliance

A governance artifact is constitutionally compliant only if it:

1. declares the authority path;
2. emits evidence;
3. preserves off-history;
4. separates execution from promotion;
5. records irreversible action approval;
6. preserves monitor independence;
7. respects evidence minimization;
8. names non-claims and limitations.

## Non-claim boundary

This document does not implement governance runtime. It defines the invariants that runtime, schemas, CI, and certificates must implement.
