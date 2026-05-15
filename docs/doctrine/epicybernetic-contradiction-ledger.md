# EpiCybernetic Contradiction Ledger

Status: v0.1 downstream doctrine binding  
Issue: #42  
Upstream anchor: SocioSphere PR #322 / `standards/epistemic-governance`  
Publication state: public  
Runtime claim: none

## Purpose

This document defines the ProCybernetica doctrine for recording, preserving, reviewing, and repairing contradictions under the Epistemic Governance standard.

A contradiction is not merely an error. It is a control signal. It may indicate stale evidence, scope mismatch, detector drift, ontology conflict, policy conflict, missing counter-test, adversarial manipulation, or a real reversal condition.

The ledger exists so contradiction cannot be silently erased by summarization, cancellation, dashboard smoothing, policy transformation, release compensation, or social pressure.

## Scope

This is doctrine. It does not implement a database, event log, runtime monitor, detector, dashboard, validator, or policy engine.

## Ledger thesis

An epistemic system is stable only if it can preserve contradiction without either collapsing into paralysis or hiding the contradiction to maintain apparent coherence.

The ledger is the system's memory of unresolved, bounded, resolved, superseded, and reversal-forcing contradictions.

## Contradiction classes

| Class | Meaning |
| --- | --- |
| `evidence_conflict` | Evidence items appear to support incompatible conclusions. |
| `scope_conflict` | A claim is valid in one scope but incorrectly applied to another. |
| `freshness_conflict` | A previously valid claim is stale under current conditions. |
| `ontology_conflict` | Terms, enums, identifiers, or mappings conflict across surfaces. |
| `detector_conflict` | Detector output conflicts with counter-test, baseline, or independent review. |
| `policy_conflict` | Two policies or authority paths produce incompatible decisions. |
| `publication_conflict` | Evidence needed for review cannot be published without redaction or synthetic substitute. |
| `human_dignity_conflict` | A claim, detector, or projection risks converting a person into an unsupported score, accusation, or reputation consequence. |
| `runtime_conflict` | Runtime behavior contradicts declared policy, schema, fixture, or doctrine. |
| `dependency_conflict` | Shared ancestry, hidden dependency, or cancellation path undermines claimed independence. |

## Ledger states

| State | Meaning |
| --- | --- |
| `open` | Contradiction is recorded and unresolved. |
| `bounded` | Contradiction is understood within declared scope but not eliminated. |
| `under_review` | Review, counter-test, or evidence collection is active. |
| `repair_required` | Contradiction requires doctrine, schema, adapter, claim, runtime, or policy repair. |
| `reversal_required` | Contradiction invalidates a promoted claim within declared scope. |
| `superseded` | Contradiction is resolved by a newer claim, schema, or doctrine. |
| `resolved` | Contradiction is closed with evidence and repair record. |
| `deferred` | Contradiction is preserved because required evidence or owner is not yet available. |

A contradiction may not be deleted merely because it is inconvenient, reputationally costly, or visually noisy.

## Minimal ledger entry

A contradiction-ledger entry should include:

- `contradiction_id`;
- `class`;
- `state`;
- `summary`;
- affected claims, decisions, schemas, fixtures, policies, or runtime surfaces;
- evidence references;
- counter-test references;
- dependency and ancestry notes;
- publication/privacy boundary;
- human dignity boundary if people are implicated;
- owner;
- required repair action;
- reversal or supersession requirement;
- replay/audit reference;
- closure rationale.

## Preservation law

Contradictions must be preserved when they affect promoted claims, policy decisions, public doctrine, schema semantics, runtime authority, human-facing projections, or downstream estate integration.

Preservation does not mean every contradiction is equally important. It means the system keeps enough structured state to revisit, repair, reverse, or bound the conflict.

## Bounded-uncertainty law

Some contradictions do not force reversal. They establish bounded uncertainty.

A contradiction may be bounded when:

- scope differences are explicit;
- freshness windows are declared;
- downstream decisions do not rely on the disputed part;
- the evidence conflict is known but not material;
- the claim is demoted to supported, held, or under-review state;
- a public-safe substitute preserves the review structure while private evidence is withheld for a narrow reason.

Bounded uncertainty must be explicit. It may not be hidden behind confident prose.

## Reversal-trigger law

A contradiction must trigger reversal review when it affects a promoted claim and any of the following are true:

- core evidence is invalidated;
- source provenance is wrong;
- independence assumption fails;
- counter-test defeats the claim;
- claim scope was broader than evidence scope;
- privacy or consent boundary was violated;
- runtime behavior contradicts the promoted claim;
- downstream action relied on the disputed claim.

If reversal review is triggered, the claim must be held or downgraded until review completes.

## Cancellation-path law

Cancellation paths, overrides, compensating controls, and policy exceptions must not hide contradictions.

If a cancellation path changes the effect of a policy or claim, the contradiction ledger must record:

- the original claim or policy;
- the cancellation reason;
- the authority that permitted cancellation;
- whether the cancellation resolves, bounds, or merely masks the contradiction;
- downstream surfaces affected.

Silent cancellation is a failure condition.

## Dependency law

A contradiction may arise because supposedly independent evidence shares a hidden source, tool, pipeline, model, prompt, policy, or authority path.

The ledger should preserve dependency ancestry when known. If ancestry is unknown but material, the contradiction state should remain `open`, `under_review`, or `deferred`, not `resolved`.

## Human dignity law

When contradiction concerns a person, human digital twin, role, group, or identity-linked projection, the ledger must preserve dignity constraints.

The ledger must not turn disputed findings into hidden reputation penalties, accusation records, or irreversible governance consequences.

Human-facing contradictions require:

- scope limitation;
- appeal or review path;
- evidence boundary;
- prohibited-conclusion note where appropriate;
- consent or redress boundary when downstream consequences are possible.

## Publication law

A contradiction involving private evidence should not force total silence.

The public repository should preserve one or more public-safe substitutes:

- method;
- schema;
- synthetic fixture;
- redacted summary;
- provenance posture;
- withheld-specific reason;
- missing-evidence note.

The ledger should distinguish evidence secrecy from doctrine uncertainty.

## Repair actions

Permitted repair actions include:

- `claim_hold`;
- `claim_reversal`;
- `claim_supersession`;
- `schema_revision`;
- `doctrine_revision`;
- `adapter_revision`;
- `policy_revision`;
- `runtime_mitigation`;
- `deployment_hold`;
- `audit_escalation`;
- `publication_boundary_repair`;
- `countertest_required`;
- `evidence_required`.

A repair action must name what changes and what remains unresolved.

## Closure law

A contradiction can close only when the closure rationale states:

- what evidence resolved or bounded the conflict;
- what claim, schema, doctrine, policy, or runtime surface changed;
- what downstream dependencies were checked;
- whether a reversal, supersession, or notice was required;
- what evidence remains missing, if any.

If closure depends on a future artifact, the correct state is `deferred`, not `resolved`.

## Relationship to falsification doctrine

Relevant falsification observables include:

- F1.2 when source ambiguity is erased;
- F3.3 when reversal or supersession path is missing;
- F4.3 when defeasible support becomes silent authority;
- F5.4 when break-glass or cancellation paths fail open or silently succeed;
- F8.2 when cancellation paths produce silent contradictions;
- B1 when human reputation or governance consequence is mapped without consent.

## Non-claims

This document does not claim a final contradiction-ledger schema or runtime implementation exists. It defines the doctrine constraints that future schema, fixture, validator, policy, and replay work must satisfy.