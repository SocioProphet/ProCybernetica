# Constitutional Invariants for the Cybernetic Governance Fabric

**Status:** Draft v0.1  
**Track:** Tier 0 — Constitutional invariants  
**Intended landing point:** `ProCybernetica/docs/constitutional/CONSTITUTIONAL_INVARIANTS.md`  
**Purpose:** Define the non-negotiable doctrine constraints that every later schema, runtime service, monitor, release process, and safety case must preserve.

---

## 1. Purpose

The Cybernetic Governance Fabric must not begin with implementation details. It must begin with invariants.

An invariant is a rule that remains true across all valid implementations of the fabric. Schemas, services, dashboards, evidence formats, cryptographic receipts, model-internal probes, safety cases, and release-delta machinery are valid only if they preserve these invariants.

This document is the constitutional layer. It precedes statute-like standards, runtime policy, schema bundles, and operational runbooks.

The design target is a governed system in which model-mediated action is not trusted because a model is capable, persuasive, or aligned in aspiration. It is trusted only inside a control loop with typed authority, traceable action, independent monitoring, replayable evidence, privacy-preserving assurance, and promotion law.

---

## 2. Scope

These invariants apply to:

- models,
- agents,
- tools,
- monitors,
- evaluators,
- policies,
- prompts,
- memory systems,
- subagents,
- repositories,
- pull requests,
- deployments,
- release gates,
- safety cases,
- evidence receipts,
- dashboards,
- public assurance reports,
- incident reports,
- publication-boundary decisions.

The invariants apply recursively. A monitor is itself a governed node. An evaluator is itself a governed node. A safety case is itself a governed artifact. A human approval event is also a governed event.

---

## 3. Constitutional vocabulary

### Governed node

A governed node is any entity that can observe, decide, transform, authorize, evaluate, store, publish, or actuate.

Examples: model, agent, tool, monitor, evaluator, repository, policy file, release gate, dashboard, human operator.

### Governed action

A governed action is any transformation that changes state, emits evidence, makes a claim, affects authority, affects permissions, affects publication, or influences promotion.

Examples: tool call, file write, deployment, model update, policy update, monitor alert, evaluator score, safety-case approval.

### Authority

Authority is the right of an instruction, policy, actor, or artifact to govern a decision. Authority must be explicit, typed, bounded, and traceable.

### Evidence

Evidence is a digital, typed, digestible artifact that supports or constrains a claim. Evidence may be private, sealed, public, redacted, or selectively disclosed. Prose alone is not evidence.

### Promotion

Promotion is the movement of a claim, artifact, policy, model, agent, or deployment from one governance state to another. Promotion requires evidence and a controller-visible decision.

### Off-history

Off-history is the branch of action that did not execute because it was blocked, transformed, sandboxed, downgraded, or withheld. Off-history evidence is evidence about non-execution and counterfactual action.

---

## 4. Tier 0 invariants

### Invariant 0.1 — No hidden authority lane

Every decision that affects action, evidence, promotion, or publication must be governed by an explicit authority chain.

There must be no undeclared path by which a model, user, tool, hidden prompt, runtime, evaluator, monitor, maintainer, or external document can control a decision.

**Implementation consequence:** every material decision must carry `authority_chain_id`.

**Invalid pattern:** an agent silently treats a tool output as a system instruction.

**Valid pattern:** the agent records the tool output as untrusted evidence and resolves conflict under the authority hierarchy.

---

### Invariant 0.2 — No action without trace

Every governed action must emit an action trace.

The trace must identify:

- actor,
- authority chain,
- action type,
- target,
- tool or subsystem,
- permission scope,
- pre-state reference,
- post-state reference or expected post-state,
- side-effect class,
- monitor decision,
- evidence receipt,
- timestamp,
- replay or non-replay reason.

**Implementation consequence:** action execution APIs must reject untraceable actions.

**Invalid pattern:** a tool writes to a repository without an `agent_action_trace`.

**Valid pattern:** the file write is associated with permission scope, diff digest, monitor result, and evidence receipt.

---

### Invariant 0.3 — No promotion by prose alone

No claim may be promoted solely because a human, model, committee, or document says it should be promoted.

Promotion requires:

- prior state,
- target state,
- evidence receipt,
- gate identifier,
- artifact digest,
- claim boundary,
- non-claims,
- risk movement,
- authority chain,
- promotion decision.

**Implementation consequence:** a promotion decision must be machine-checkable.

**Invalid pattern:** Approved because this looks safe.

**Valid pattern:** Promoted from `checked` to `cross_checked` under gate `G-017`, supported by evidence receipts, with non-claims and replay limitations recorded.

---

### Invariant 0.4 — Evidence must be digital, typed, and digestible

Evidence must be representable as a finite digital artifact with stable type, stable identity, and digest.

This does not mean every underlying phenomenon is digital. It means every governance-relevant claim must be supported by a digital projection suitable for replay, audit, signing, redaction, and comparison.

**Implementation consequence:** every evidence object must include a schema ID and content digest.

**Invalid pattern:** The model seemed aligned during the demo.

**Valid pattern:** a demo transcript, monitor output, eval result, release-delta record, and safety-case claim are stored with digests.

---

### Invariant 0.5 — Separation of powers

The same authority path must not be able to author policy, execute action, evaluate action, issue evidence, approve promotion, and publish assurance without independent checks.

At minimum, the following functions are distinct roles even if one person or system temporarily occupies several roles under explicit exception:

- policy author,
- runtime executor,
- monitor,
- evaluator,
- evidence signer,
- promotion authority,
- publication reviewer,
- incident commander,
- external reviewer or independent reviewer where required.

**Implementation consequence:** safety cases must identify role separation and approved exceptions.

**Invalid pattern:** the agent marks its own action safe, signs its own receipt, and promotes itself.

**Valid pattern:** the agent proposes action, monitor evaluates, evaluator checks fixture class, evidence signer records, promotion authority decides.

---

### Invariant 0.6 — Monitor independence from governed actor

A monitor must not be controlled by the same runtime path that it is responsible for monitoring unless the dependency is declared and compensated by another independent monitor.

The monitored actor must not be able to silently disable, edit, bypass, starve, spoof, or demote its monitor.

**Implementation consequence:** monitor configuration and monitor status must be part of the evidence fabric.

**Invalid pattern:** an agent modifies its own monitor thresholds before executing a risky action.

**Valid pattern:** monitor updates require release-delta review and meta-monitor evidence.

---

### Invariant 0.7 — Irreversibility requires approval or stronger gate

Actions with irreversible, externally visible, financially material, legally material, security material, privacy material, or physical-world consequences require explicit approval or a stronger pre-authorized gate.

Irreversibility is not only physical. It includes:

- sending email,
- publishing public content,
- deleting files,
- merging PRs,
- deploying systems,
- changing permissions,
- exposing private data,
- spending money,
- modifying policy,
- disabling controls.

**Implementation consequence:** every action must carry a side-effect and reversibility classification.

**Invalid pattern:** an agent merges a PR because tests passed.

**Valid pattern:** the merge is gated by authority, monitor, side-effect classification, rollback plan, and approval profile.

---

### Invariant 0.8 — Off-history is retained

Blocked, sandboxed, transformed, downgraded, or refused actions must still emit evidence.

The system must preserve:

- proposed action,
- reason blocked or transformed,
- authority chain,
- monitor classification,
- policy rule,
- predicted or attempted side effect,
- counterfactual branch summary,
- safe alternative if generated.

**Implementation consequence:** no action executed is not no evidence required.

**Invalid pattern:** a blocked command disappears from the trace.

**Valid pattern:** the blocked command becomes off-history evidence and is available for monitor calibration and safety-case review.

---

### Invariant 0.9 — Privacy and evidence minimization

The fabric must capture enough evidence to govern responsibly, but no more than needed for the claim being made.

Evidence capture must distinguish:

- public evidence,
- redacted evidence,
- private evidence,
- sealed evidence,
- privileged evidence,
- sensitive operational evidence,
- evidence not to be retained.

**Implementation consequence:** evidence receipts must include privacy class and disclosure policy.

**Invalid pattern:** storing raw prompts, secrets, credentials, private user data, or internal reasoning traces without classification.

**Valid pattern:** store hashes, redacted excerpts, sealed witness commitments, and disclosure boundaries.

---

### Invariant 0.10 — Claims require non-claims

Every safety, capability, compliance, and interpretability claim must record what is not being claimed.

Non-claims prevent assurance theater.

Examples:

- This monitor catches these prompt-injection fixtures; it does not prove absence of all injection.
- This latent feature correlates with sycophancy-like behavior; it is not proof of intent.
- This safety case covers this deployment profile; it does not cover higher autonomy tiers.

**Implementation consequence:** safety cases without non-claims fail validation.

---

### Invariant 0.11 — Release changes require delta governance

Every material change must be accompanied by a release-delta record before promotion.

Material changes include:

- model update,
- fine-tune,
- prompt change,
- policy change,
- reward/rubric change,
- monitor change,
- tool-permission change,
- memory-policy change,
- dataset change,
- schema change,
- deployment-profile change,
- evaluator change,
- runtime harness change.

**Implementation consequence:** minor change is a classification requiring evidence, not an excuse to skip review.

---

### Invariant 0.12 — Monitors are monitored

Every production monitor must itself be subject to meta-monitoring.

Meta-monitoring must track:

- calibration,
- drift,
- recall,
- false positives,
- false negatives,
- latency,
- outage,
- tampering,
- policy mismatch,
- blind active/sham tests where practical.

**Implementation consequence:** monitor promotion requires monitor-of-monitor evidence.

---

### Invariant 0.13 — Safety case before frontier promotion

No frontier agent node, high-autonomy profile, high-risk toolchain, or public assurance claim may be promoted without a cybernetic safety case.

A safety case must include:

- claim,
- non-claims,
- scope,
- authority chain,
- threat model,
- evidence receipts,
- gates passed,
- gates failed,
- residual risk,
- privacy boundary,
- release-delta status,
- incident history,
- replay status,
- publication status.

---

### Invariant 0.14 — Public-first, redaction-disciplined assurance

Public-safe material should be publishable by default. Redaction requires a specific reason:

- secrets,
- credentials,
- private user/customer data,
- live private telemetry,
- sensitive deployment configuration,
- legally restricted material,
- evidence that must be sanitized before release.

The burden of justification is on withholding public-safe assurance material, not on publishing it.

---

### Invariant 0.15 — Frontier claims require frontier metrics

A claim of frontier governance must be backed by metrics, not aspiration.

Minimum metrics:

- authority-chain coverage,
- action-trace coverage,
- tool-scope coverage,
- off-history capture rate,
- evidence-receipt completeness,
- monitor recall,
- monitor latency,
- release-delta completeness,
- promotion-by-prose violations,
- safety-case completeness,
- replay success rate,
- privacy-classification coverage,
- authority-concentration index,
- incident closure quality,
- public-assurance coverage.

---

## 5. Derived constitutional tests

Every future schema or runtime component should be checked against these questions:

1. Does it introduce a hidden authority lane?
2. Can a governed action occur without trace?
3. Can a claim be promoted by prose?
4. Is evidence digital, typed, and digestible?
5. Does it collapse separation of powers?
6. Can the governed actor disable its monitor?
7. Does it handle irreversible actions correctly?
8. Does it preserve off-history?
9. Does it minimize and classify private evidence?
10. Does it force non-claims?
11. Does it require release-delta governance?
12. Does it monitor monitors?
13. Does it require safety cases for frontier promotion?
14. Does it support public-first redaction discipline?
15. Does it produce frontier metrics?

If the answer to any required question is no, the component is constitutionally invalid.

---

## 6. Minimal Tier 1 implementation obligations

To implement these invariants, Tier 1 must define and validate:

- `authority_chain.v1.json`
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

---

## 7. Non-goals

This document does not define:

- the full mathematical foundation,
- all schemas,
- cryptographic receipt construction,
- quantum or post-quantum evidence primitives,
- monitor-network topology,
- model-internal interpretability methods,
- release-delta decomposition algorithms.

Those belong in later doctrine and standards documents. This document defines what they must not violate.

---

## 8. Governance-state consequence

A system that violates a Tier 0 invariant may not be promoted to production frontier status.

Valid states after a violation:

- `draft`
- `diagnosed`
- `quarantined`
- `archived`

Invalid states after unresolved violation:

- `cross_checked`
- `promoted`
- `frontier_certified`
- `public_assured`

---

## 9. Closing doctrine

Capability does not create authority.  
Plausibility does not create evidence.  
Evidence does not create promotion.  
Promotion does not erase risk.  
Safety cases do not eliminate non-claims.  
Governance without trace is not governance.

The fabric exists to make these statements executable.
