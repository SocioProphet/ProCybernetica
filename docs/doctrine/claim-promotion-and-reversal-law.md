# Claim Promotion and Reversal Law

Status: v0.1 downstream doctrine binding  
Issue: #42  
Upstream anchor: SocioSphere PR #322 / `standards/epistemic-governance`  
Publication state: public  
Runtime claim: none

## Purpose

This document defines the ProCybernetica doctrine for claim promotion, claim hold, reversal, supersession, and repair under the Epistemic Governance standard.

The law exists to prevent prose, model output, detector findings, issue comments, dashboards, and operator impressions from becoming canonical truth without evidence, counter-test posture, authority, and replay.

## Scope

This is doctrine. It does not implement a schema, validator, detector, replay bundle, release gate, or runtime policy.

## Core thesis

A claim becomes authoritative only through promotion law.

Promotion is not emphasis. Promotion is a controlled state transition. It changes how the estate may rely on a claim. Therefore promotion requires evidence, authority, scope, counter-test posture, and reversal path.

## Claim states

The minimum ProCybernetica claim-state vocabulary is:

| State | Meaning |
| --- | --- |
| `proposed` | Claim has been stated but not evaluated. |
| `under_review` | Claim is being assessed, counter-tested, or evidence-linked. |
| `held` | Claim is blocked from promotion pending evidence, scope, or policy repair. |
| `supported` | Evidence supports the claim within declared scope, but authority remains limited. |
| `promoted` | Claim is canonical for a declared scope and may be relied on by downstream decisions. |
| `reversed` | Claim was promoted or supported but is now invalidated within the declared scope. |
| `superseded` | Claim is replaced by a newer or more precise claim. |
| `rejected` | Claim is unsupported, false, out of scope, or prohibited. |
| `stale` | Claim may have been valid but requires freshness review before reliance. |

Schemas may later refine this vocabulary, but they must preserve the distinction between proposed, supported, promoted, reversed, superseded, rejected, and stale.

## Promotion requirements

A claim may move to `promoted` only when all of the following are present:

1. declared claim scope;
2. evidence references;
3. evidence level or maturity class;
4. authority to promote;
5. counter-test posture;
6. replay or audit path;
7. publication/privacy state;
8. reversal or supersession path;
9. downstream-dependency awareness.

If any requirement is missing, the correct state is `held`, `under_review`, or `supported`, not `promoted`.

## Evidence requirement

Promotion requires evidence. Evidence may include:

- direct observation;
- derived fact with named transform;
- fixture validation;
- schema or SHACL/Rego validation;
- reproducible run output;
- provenance record;
- counter-test result;
- review finding;
- external artifact pinned by version, SHA, or stable source reference.

Reasoning may explain why evidence matters. Reasoning does not replace evidence.

## Counter-test requirement

A promotion record must state what could defeat, weaken, stale, or reverse the claim.

Minimum counter-test fields:

- missing evidence;
- alternative explanations or interpretations;
- freshness condition;
- dependency or independence assumption;
- privacy or publication caveat;
- reversal trigger.

## Authority requirement

Promotion requires an explicit authority scope.

Authority scope answers:

- who or what may promote;
- which repository, doctrine, schema, standard, runtime, or decision surface the promotion affects;
- which downstream consumers may rely on the promoted claim;
- which consumers must treat it as non-authoritative.

Promotion authority does not automatically authorize action. Decisions and actions remain separate layers.

## Claim / decision / action separation

A promoted claim may inform a decision. It is not itself a decision.

A decision may authorize an action. It is not itself the action.

An action must carry its own authority, policy, side-effect, and replay surface.

This separation blocks the path:

```text
model output -> claim -> implied decision -> side effect
```

without explicit promotion and policy control.

## Hold law

A claim must be held when:

- evidence is missing;
- source anchors are stale or ambiguous;
- private evidence is required but not redacted;
- counter-tests are absent;
- scope is too broad;
- authority is unclear;
- downstream effects are high-impact;
- human dignity, privacy, or consent boundaries are implicated.

A held claim is not discarded. It is preserved as controlled uncertainty.

## Reversal law

A claim must be reversed when new evidence, counter-test failure, provenance correction, contradiction, or scope repair invalidates the promoted claim within its declared authority scope.

A reversal record must identify:

- original claim;
- original promotion state;
- reversal evidence;
- affected downstream decisions or actions;
- required repair;
- notice or migration requirement;
- whether the claim becomes `reversed`, `superseded`, `rejected`, or `stale`.

## Supersession law

Supersession applies when the prior claim is not necessarily false, but a newer claim is more precise, better evidenced, narrower in scope, or aligned to updated doctrine.

Supersession must preserve the old claim as historical state. It must not erase the prior claim if downstream artifacts relied on it.

## Staleness law

A claim becomes stale when its evidence, dependency, source, baseline, runtime condition, or standard version has aged beyond the declared freshness window.

Stale claims may remain in the archive. They may not be relied on for new decisions without freshness review.

## Prohibited promotions

The following may not be promoted as canonical claims without additional evidence and review:

- detector findings by themselves;
- model-generated summaries by themselves;
- reasoning traces by themselves;
- operator impressions by themselves;
- repeated observations from one dependent pipeline;
- private suspicion;
- unsupported actor attribution;
- dashboard labels that lack evidence lane;
- claims whose publication boundary is unresolved.

## Repair law

Repair must be targeted to the failed transition.

Examples:

- missing evidence -> attach evidence or hold claim;
- overbroad scope -> narrow claim scope;
- stale source -> refresh source or mark stale;
- unsupported attribution -> remove attribution and preserve lower-confidence hypothesis;
- contradiction -> create contradiction-ledger entry and evaluate reversal;
- privacy breach -> remove artifact, add redacted/synthetic substitute, and record boundary failure.

## Downstream dependency law

Promoted claims may become dependencies for other claims, decisions, schemas, fixtures, release gates, or runtime policy.

A reversal must therefore inspect downstream dependencies. A claim cannot be reversed cleanly if the estate does not know what relied on it.

## Relationship to falsification doctrine

Relevant falsification observables include:

- F3.1: soft-lane output promoted without evidence;
- F3.2: replay path absent for promoted artifact or decision;
- F3.3: reversal or supersession path missing;
- F3.4: promotion decision lacks evidence level;
- F4.3: defeasible support treated as silent authority;
- F7.4: cross-repo evidence cited without freshness or version boundary.

## Non-claims

This document does not claim that final promotion schemas or validators exist. It defines the doctrine constraints that those schemas, fixtures, and validators must later satisfy.