# Unified Falsification Document v1.0

Status: v1.0 doctrine draft  
Issue: #44  
Publication state: public  
Runtime claim: none

## Purpose

This document defines the falsification observables that prevent ProCybernetica from stabilizing around the wrong thing.

The purpose is not to prove the architecture correct. The purpose is to specify what would count as evidence that a doctrine, schema, fixture, runtime binding, promotion path, or estate integration is wrong, under-specified, over-claiming, or unsafe to promote.

A falsification observable is a named failure condition with required evidence, a threshold or trigger, a forced revision action, and an owner. It may be fixture-testable now, runtime-observable later, periodic-audit-only, or human-review-only.

## Scope boundary

This is doctrine and testability mapping only. It does not implement runtime telemetry, validators, dashboards, CI, production monitoring, or incident response.

This document is intended to unblock #45, which should add cross-reference, owners registry, fixtures where appropriate, validation entrypoints, and CI targets.

## Current anchor status

The issue text references two downstream anchors that were not present on `main` at the time this document was drafted:

- `docs/capability-tiers/quantum-dependency-substrate-v0.1.md`
- `docs/bridges/BRIDGE_SCHEMAS_V1_EXECUTION_PLAN.md`

This document therefore records F8 capability-tier observables and bridge-related observables as doctrine-level requirements with deferred cross-reference anchors. #45 or a follow-on reconciliation PR should update the cross-reference table once those files exist or their canonical paths are corrected.

## Evidence classes

| Evidence class | Meaning |
| --- | --- |
| `fixture-testable` | Can be tested with static public fixtures immediately. |
| `schema-testable` | Can be tested once relevant schemas or SHACL/Rego companions exist. |
| `ci-testable` | Can be checked by repository-local validation or coverage scripts. |
| `runtime-telemetry` | Requires live or simulated runtime telemetry not added here. |
| `periodic-audit` | Requires scheduled human or automated review of repository/runtime evidence. |
| `human-review` | Requires explicit reviewer judgment because the observable concerns claim interpretation, publication boundary, or doctrine fit. |

## Forced revision actions

| Action | Meaning |
| --- | --- |
| `schema_revision` | Revise schema, shape, enum, or fixture contract. |
| `doctrine_revision` | Revise the doctrine text, boundary language, or claim discipline. |
| `runtime_mitigation` | Add or modify runtime guardrails, admission checks, telemetry, or policy enforcement. |
| `deployment_hold` | Block release, promotion, or runtime deployment pending correction. |
| `claim_hold` | Block public claim promotion pending evidence or boundary repair. |
| `adapter_revision` | Change a cross-repo adapter or mapping rather than forking another repository's contract. |
| `audit_escalation` | Escalate to maintainer or specialist review without asserting runtime incident status. |

## Owner classes

| Owner | Responsibility |
| --- | --- |
| `procybernetica-doctrine` | Doctrine, publication boundary, claim discipline, and falsification language. |
| `procybernetica-schema` | JSON Schema, SHACL, Rego, fixtures, validator coverage, and schema naming. |
| `procybernetica-ci` | Repository-local validation and coverage checks. |
| `estate-adapter-owner` | Cross-repository adapter and contract-boundary mapping. |
| `runtime-plane-owner` | Downstream runtime telemetry, policy enforcement, execution traces, and deployment guardrails. |
| `maintainer-review` | Human review for ambiguous, high-impact, or cross-boundary cases. |

---

## F1 — Source capture and provenance observables

F1 prevents the repository from treating uncaptured, ambiguous, private, or misrepresented source material as canonical public doctrine.

| ID | Observable | Required evidence | Trigger / threshold | Forced revision action | Owner | Evidence class |
| --- | --- | --- | --- | --- | --- | --- |
| F1.1 | A doctrine or schema claim lacks a source anchor, issue anchor, or explicit proposal marker. | Changed file, PR body, source-capture reference, issue link. | Any normative claim added without anchor or proposal status. | `doctrine_revision`; `claim_hold`. | `procybernetica-doctrine` | `human-review`; `ci-testable` after cross-reference tooling. |
| F1.2 | Source ambiguity is erased instead of recorded. | Source captures, reconciliation notes, changed doctrine text. | Conflicting source terms are collapsed without conflict note or decision record. | `doctrine_revision`. | `procybernetica-doctrine` | `human-review`. |
| F1.3 | Private or sensitive source evidence is committed without redaction boundary. | Added files, fixture classification, publication-state metadata. | Any credential, private log, customer data, user-private evidence, live telemetry, or sensitive deployment detail appears in public artifact. | `deployment_hold`; `doctrine_revision`; `audit_escalation`. | `maintainer-review` | `ci-testable` for detectable secrets; `human-review` for content sensitivity. |
| F1.4 | A Drive-derived or external artifact is claimed as mirrored when only a summary exists. | PR body, corpus index, source capture, file tree. | Artifact status text overstates actual repository contents. | `doctrine_revision`; `claim_hold`. | `procybernetica-doctrine` | `human-review`; `periodic-audit`. |

## F2 — Schema, shape, and conformance observables

F2 prevents early or partial schema work from being mistaken for frozen law.

| ID | Observable | Required evidence | Trigger / threshold | Forced revision action | Owner | Evidence class |
| --- | --- | --- | --- | --- | --- | --- |
| F2.1 | A provisional schema is treated as canonical before reconciliation freeze. | Schema file, README, docs, PR body. | Language such as final, canonical, production, or required appears without v0 freeze decision. | `schema_revision`; `doctrine_revision`. | `procybernetica-schema` | `human-review`; `ci-testable` with phrase linting. |
| F2.2 | A certificate, bridge, or governance schema lacks companion validation coverage or explicit deferred status. | Schema tree, SHACL/Rego/validator files, issue links. | New schema lands without validation companion, fixture plan, or deferred-status note. | `schema_revision`; `claim_hold`. | `procybernetica-schema` | `schema-testable`; `ci-testable` after #45. |
| F2.3 | Enum drift emerges between doctrine, schema, fixture, and downstream repo contract. | Doctrine files, schemas, examples, adapter maps. | Same concept has incompatible enum values without mapping or explicit conflict note. | `schema_revision`; `adapter_revision`. | `procybernetica-schema`; `estate-adapter-owner` | `ci-testable` with enum inventory. |
| F2.4 | A positive fixture passes while violating a named invariant. | Fixture, validator output, invariant map. | Fixture marked valid contradicts Tier 0/Tier 1 invariant. | `schema_revision`; `deployment_hold` if runtime-bound. | `procybernetica-ci` | `fixture-testable`. |
| F2.5 | A negative fixture fails for the wrong reason or passes. | Negative fixture, validator diagnostics. | Rejection reason is missing, generic, or mismatched to intended invariant. | `schema_revision`; `ci-testable` repair. | `procybernetica-ci` | `fixture-testable`. |

## F3 — Replay, promotion, and reversal observables

F3 prevents unreviewed claims, actions, or soft-lane outputs from becoming canonical state.

| ID | Observable | Required evidence | Trigger / threshold | Forced revision action | Owner | Evidence class |
| --- | --- | --- | --- | --- | --- | --- |
| F3.1 | Soft-lane output is promoted without evidence, policy, audit, and promotion decision. | Claim record, PR, fixture, promotion artifact. | Any model output, analyst interpretation, detector finding, or heuristic result is marked canonical without promotion evidence. | `claim_hold`; `doctrine_revision`; `schema_revision`. | `procybernetica-doctrine` | `fixture-testable`; `human-review`. |
| F3.2 | Replay path is absent for a promoted artifact or decision. | Replay envelope, provenance record, evidence receipt. | Promoted claim or action lacks replay reference or states replay is unavailable without reason. | `claim_hold`; `schema_revision`. | `procybernetica-schema` | `schema-testable`. |
| F3.3 | Reversal or supersession path is missing. | Promotion state, reversal doctrine, issue comments, schema fields. | Promoted claim cannot be marked rejected, superseded, stale, or reversed. | `schema_revision`; `doctrine_revision`. | `procybernetica-doctrine`; `procybernetica-schema` | `schema-testable`; `human-review`. |
| F3.4 | Promotion decision does not identify evidence level. | Promotion record, evidence lane, proof pack, PR body. | Promotion occurs without E-level, maturity level, or equivalent evidence classification. | `claim_hold`; `schema_revision`. | `procybernetica-schema` | `fixture-testable`. |

## F4 — Reasoning, evidence, Cairnmark, and Stele observables

F4 keeps reasoning operations, candidate artifacts, and promoted authority separated.

| ID | Observable | Required evidence | Trigger / threshold | Forced revision action | Owner | Evidence class |
| --- | --- | --- | --- | --- | --- | --- |
| F4.1 | Reasoning operations are conflated with evidence. | Claim text, evidence receipt, reasoning trace reference, PR body. | Rationale, chain, or model reasoning is cited as direct evidence rather than as interpretation or derivation. | `doctrine_revision`; `claim_hold`. | `procybernetica-doctrine` | `human-review`; `ci-testable` with claim-boundary linting. |
| F4.2 | Cairnmarks are indistinguishable from Steles. | Certificate schema, doctrine text, examples. | Candidate, marker, draft, or support object has the same promotion semantics as a promoted Stele. | `schema_revision`; `doctrine_revision`. | `procybernetica-schema` | `schema-testable`; `human-review`. |
| F4.3 | Defeasible support is treated as silent authority. | Claim promotion notes, certificate fields, evidence table. | Support evidence changes operational authority without explicit promotion, review, or scope constraint. | `claim_hold`; `runtime_mitigation`; `schema_revision`. | `maintainer-review`; `runtime-plane-owner` | `human-review`; `runtime-telemetry` later. |
| F4.4 | Reasoning trace references expose private chain or sensitive material. | Reasoning trace ref, artifact metadata, publication state. | Trace reference points to private content without redaction or access boundary. | `deployment_hold`; `doctrine_revision`. | `maintainer-review` | `human-review`; secret scanning where possible. |

## F5 — Authority, control, and side-effect observables

F5 prevents governance artifacts from authorizing uncontrolled action.

| ID | Observable | Required evidence | Trigger / threshold | Forced revision action | Owner | Evidence class |
| --- | --- | --- | --- | --- | --- | --- |
| F5.1 | Authority chain absent for governed action. | Action trace, authority chain, tool grant, policy envelope. | Governed action, tool call, merge, deployment, or side effect lacks authority reference. | `runtime_mitigation`; `schema_revision`; `deployment_hold`. | `runtime-plane-owner`; `procybernetica-schema` | `schema-testable`; `runtime-telemetry`. |
| F5.2 | Tool or capability scope is broader than declared policy. | Tool grant, capability descriptor, policy envelope. | Tool can perform actions not covered by explicit scope. | `runtime_mitigation`; `deployment_hold`. | `runtime-plane-owner` | `runtime-telemetry`; `periodic-audit`. |
| F5.3 | Side effects are not recorded or are misclassified as no-op. | Environment delta, side-effect assessment, replay envelope. | File, repo, issue, PR, deployment, or policy mutation occurs without side-effect record. | `runtime_mitigation`; `schema_revision`. | `runtime-plane-owner`; `procybernetica-schema` | `runtime-telemetry`; `fixture-testable` in examples. |
| F5.4 | Break-glass or cancellation path fails closed incorrectly or silently succeeds. | Policy fabric binding, cancellation receipt, audit log. | Emergency/cancellation path produces unlogged state change or fails open. | `runtime_mitigation`; `deployment_hold`; `audit_escalation`. | `runtime-plane-owner`; `maintainer-review` | `runtime-telemetry`; `periodic-audit`. |

## F6 — Publication, privacy, and evidence-boundary observables

F6 keeps the public-first posture from becoming either reckless disclosure or vague concealment.

| ID | Observable | Required evidence | Trigger / threshold | Forced revision action | Owner | Evidence class |
| --- | --- | --- | --- | --- | --- | --- |
| F6.1 | Public artifact contains private or sensitive evidence. | Diff, fixture, document, schema example, secret scan. | Credential, token, private log, customer/user data, live private telemetry, or sensitive deployment detail appears. | `deployment_hold`; `audit_escalation`; `doctrine_revision`. | `maintainer-review` | `ci-testable`; `human-review`. |
| F6.2 | Artifact is withheld under vague privacy language. | Issue, PR body, doc classification. | Artifact category is suppressed with generic internal/private label and no narrow reason. | `doctrine_revision`; `claim_hold`. | `procybernetica-doctrine` | `human-review`. |
| F6.3 | Public-safe substitute is missing for a withheld artifact category. | Publication boundary, issue body, fixture tree. | Private evidence category has no schema, synthetic fixture, redacted summary, method, or provenance note. | `doctrine_revision`; `schema_revision`. | `procybernetica-doctrine`; `procybernetica-schema` | `periodic-audit`. |
| F6.4 | Redaction removes the evidentiary structure needed for review. | Redacted artifact, schema, summary. | Public-safe artifact no longer preserves claim boundary, method, provenance posture, or missing-evidence field. | `doctrine_revision`; `claim_hold`. | `procybernetica-doctrine` | `human-review`. |

## F7 — Estate alignment and anti-fork observables

F7 prevents ProCybernetica from duplicating runtime, evidence, ontology, OS, platform, or policy surfaces that are owned elsewhere in the estate.

| ID | Observable | Required evidence | Trigger / threshold | Forced revision action | Owner | Evidence class |
| --- | --- | --- | --- | --- | --- | --- |
| F7.1 | ProCybernetica forks a contract already owned by another repository. | Estate map, upstream schema, new schema, PR body. | New schema duplicates AgentPlane, SourceOS, SocioSphere, PolicyFabric, ontogenesis, semantic-serdes, or Prophet Platform contract without gap note. | `adapter_revision`; `schema_revision`. | `estate-adapter-owner`; `procybernetica-schema` | `human-review`; `periodic-audit`. |
| F7.2 | Runtime ownership is displaced into ProCybernetica. | New code, docs, issue scope. | ProCybernetica claims to own production runtime where another repo owns execution surface. | `doctrine_revision`; `adapter_revision`; `deployment_hold` if implemented. | `estate-adapter-owner`; `runtime-plane-owner` | `human-review`. |
| F7.3 | Adapter boundary is absent after an estate mapping declares one. | Integration map, adapter issue, schema reference. | A mapping says reference/import/consume but no adapter or follow-up issue exists. | `adapter_revision`; `claim_hold`. | `estate-adapter-owner` | `periodic-audit`; `ci-testable` after issue-link tooling. |
| F7.4 | Cross-repo evidence is cited without freshness or version boundary. | Commit SHA, PR number, release tag, evidence receipt. | External artifact is referenced by floating branch or informal name when precise version matters. | `adapter_revision`; `claim_hold`. | `estate-adapter-owner` | `human-review`; `ci-testable` in manifests. |

## F8 — Capability-tier and dependency-substrate observables

F8 covers capability-tier observables named in #44. Because the canonical capability-tier document was not present at the named path during drafting, these are recorded as doctrine requirements with deferred cross-reference anchors.

| ID | Observable | Required evidence | Trigger / threshold | Forced revision action | Owner | Evidence class |
| --- | --- | --- | --- | --- | --- | --- |
| F8.1 | Dependency ancestry concentrates around a single evidence source. | Dependency graph, evidence receipts, proof pack, lineage table. | More than one promoted conclusion or capability decision depends on one source without independence disclosure or concentration warning. | `schema_revision`; `claim_hold`; `runtime_mitigation` later. | `procybernetica-schema`; `runtime-plane-owner` | `fixture-testable` with synthetic graph; `runtime-telemetry` later. |
| F8.2 | Cancellation paths produce silent contradictions. | Cancellation binding, policy decision, reversal record, action trace. | A cancellation, override, or compensating control hides a contradiction instead of producing a contradiction record or reversal trigger. | `schema_revision`; `runtime_mitigation`; `deployment_hold` if live. | `runtime-plane-owner`; `procybernetica-schema` | `fixture-testable`; `runtime-telemetry` later. |
| F8.3 | Adaptive feedback loop gain exceeds stability threshold. | Feedback-loop record, control policy, telemetry or simulation fixture. | Adaptive behavior changes future control scope, threshold, or policy faster than declared stability bound. | `runtime_mitigation`; `deployment_hold`; `doctrine_revision`. | `runtime-plane-owner`; `maintainer-review` | `runtime-telemetry`; synthetic simulation later. |
| F8.4 | Capability-tier invocation rate exceeds expected baseline. | Invocation receipts, baseline declaration, runtime telemetry, dashboard record. | Capability tier is invoked more often than expected baseline without review, throttle, or explanation. | `runtime_mitigation`; `audit_escalation`; `deployment_hold` for regulated surfaces. | `runtime-plane-owner` | `runtime-telemetry`; `periodic-audit`. |

## Bridge-related observables

The bridge-schema execution plan was not present at the named path during drafting, but bridge risk is already visible from #43 and #46. These observables should be reconciled with the canonical bridge plan once its path is confirmed.

| ID | Observable | Required evidence | Trigger / threshold | Forced revision action | Owner | Evidence class |
| --- | --- | --- | --- | --- | --- | --- |
| B1 | Human actor maps to reputation or governance consequence without consent evidence. | Bridge fixture, consent field, actor type. | Human actor is mapped into reputation, score, or governance state without consent or dignity boundary. | `schema_revision`; `claim_hold`; `deployment_hold`. | `procybernetica-schema`; `maintainer-review` | `fixture-testable`. |
| B2 | Candidate proof pack maps to promoted Stele certificate. | Bridge schema, promotion state, proof-pack fixture. | Candidate/draft proof pack produces promoted authority without promotion decision. | `schema_revision`; `claim_hold`. | `procybernetica-schema` | `fixture-testable`. |
| B3 | Undecided certificate fails open into Atlas admission. | Certificate fixture, Atlas bridge output. | Undecided or incomplete certificate maps to admit instead of deny or review-required. | `schema_revision`; `deployment_hold`. | `procybernetica-schema`; `runtime-plane-owner` | `fixture-testable`; runtime later. |
| B4 | Pattern C or prohibited pattern is admitted. | Certificate pattern, bridge rule, validator output. | Pattern explicitly declared deny/prohibit maps to admit. | `schema_revision`; `deployment_hold`. | `procybernetica-schema` | `fixture-testable`. |

## Testability map

| Class | Observables |
| --- | --- |
| Fixture-testable now or after minimal fixtures | F2.4, F2.5, F3.1, F3.4, F5.3 examples, F8.1, F8.2, B1, B2, B3, B4 |
| Schema-testable after schema/shape work | F2.2, F2.3, F3.2, F3.3, F4.2, F5.1 |
| CI-testable after #45 | F1.1, F1.3 partial, F2.3, F6.1 partial, F7.3 partial, F7.4 partial |
| Runtime telemetry required | F5.1, F5.2, F5.3, F5.4, F8.2, F8.3, F8.4 |
| Human review required | F1.2, F1.4, F3.1, F4.1, F4.3, F4.4, F6.2, F6.4, F7.1, F7.2 |
| Periodic audit required | F6.3, F7.3, F7.4, F8.4 |

## Cross-reference requirements for #45

#45 should add a machine-readable or table-backed cross-reference that records, for every observable:

- ID;
- owner;
- evidence class;
- forced revision action;
- whether a fixture exists;
- whether runtime telemetry is required;
- whether human review is required;
- linked schema, SHACL, Rego, or validator path if present;
- linked issue or PR if deferred.

#45 should fail validation when:

- an observable lacks an owner;
- an observable lacks a forced revision action;
- a fixture-testable observable lacks fixture status;
- a runtime-only observable is represented as CI-covered;
- a deferred anchor is not explicitly marked deferred.

## Non-claims

This document does not claim that ProCybernetica has runtime telemetry, production enforcement, bridge validators, capability-tier baselines, SHACL companion shapes, or CI coverage for these observables. It defines what must become observable and what action must follow if the observable fires.