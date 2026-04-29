# ProCybernetica Scoring Rubric

This rubric captures the public scoring surface for ProCybernetica alignment work.

## Primary composites

`POA` — ProCybernetica Operational Alignment.

`EGA` — EpiCybernetica Governance Alignment.

`Composite` — weighted rollup of operational and governance alignment.

## Score scale

| Score | Meaning |
| ---: | --- |
| 0 | absent or directly incompatible |
| 1 | mostly implicit or marketing-only |
| 2 | partial or local evidence |
| 3 | clear subsystem evidence |
| 4 | systematic and repeatable |
| 5 | constitutional or productized |

## Lab dimensions

| Dimension | Meaning |
| --- | --- |
| controlplane explicitness | evidence of explicit controlplane, node law, or runtime supervision |
| lifecycle discipline | lifecycle states, activation, recovery, retirement, quarantine |
| typed interfaces | stable commands, observations, status, artifacts, policy surfaces |
| memory/repository constitution | memory tiers, repository law, retention, conflict, provenance |
| belief/world-model discipline | explicit belief/world model, confidence, uncertainty, projection discipline |
| value judgment and policy constraints | objective, risk, trust, resource, policy, and authority constraints |
| replay/provenance | reconstructable evidence, traces, version pins, replay path |
| learning governance | proposal/promotion split, benchmark admission, rollback, calibration |
| human override | operator review, approval, override, explanation, mixed-initiative control |
| contradiction/re-anchoring | conflict representation, drift, re-anchoring, contradiction handling |
| assurance artifacts | tests, evaluation, attestations, public evidence, conformance artifacts |

## Model-family dimensions

| Dimension | Meaning |
| --- | --- |
| typed action/interface fit | model outputs bind cleanly to typed actions or contracts |
| world-model usefulness | model supports scene/world understanding or prediction |
| calibration discipline | confidence, uncertainty, or evaluation calibration is visible |
| policy-bound execution fit | model can operate within explicit policy and authority envelope |
| replayability | outputs, prompts, versions, and context can be replayed or reconstructed |
| memory compatibility | model integrates with memory tiers and provenance constraints |
| promotion/rollback compatibility | model can be evaluated, promoted, shadowed, rolled back, or quarantined |
| explainability | model supports inspectable rationale or evidence surfacing |
| embodiment separation | model separates high-level proposal from low-level safety/control where needed |
| contradiction/coherence behavior | model handles conflicts, uncertainty, and contested claims responsibly |
| evaluation evidence | public or internal evidence supports the score |

## Evidence confidence

Evidence confidence should reflect the strength of support for the dimension score:

| Confidence | Meaning |
| --- | --- |
| low | thin, indirect, or mostly inferred evidence |
| medium | credible public or structured evidence but incomplete validation |
| high | strong public, repeatable, or validated evidence |

## Public-first note

Raw scoring bodies should be public when public-safe. If raw evidence cannot be published, publish a sanitized or synthetic fixture plus methodology, row counts, and validation checks.
