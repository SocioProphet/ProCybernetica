# Source Capture: ProCybernetica Scoring Methodology and Data Provenance Dossier

Source title: `ProCybernetica Scoring Methodology and Data Provenance Dossier - v1`

Drive source: https://docs.google.com/document/d/1_aEc0bFS2z1c_aRwd6VIDUcgWSx2SEAQMqMycboou0M

Capture purpose: preserve the scoring methodology, evidence model, dashboard payload concept, and known limitations from the existing blueprint state.

## Purpose

The scoring dossier explains how ProCybernetica alignment scoring artifacts were produced, where the data came from, how scores were derived, what was directly evidenced versus heuristically inferred, what validations were performed, and what limitations remain.

## Deliverables covered by the source

The source covers:

- full 100-lab scoring body;
- model-family seed scoring set;
- dimension-level evidence registry;
- monitoring delta layer;
- customer-facing dashboard export and starter assets;
- local scoring workbook and Drive-native scoring workbooks.

## Doctrinal source corpus

The scoring doctrine was derived from the ProCybernetica Drive corpus. The highest-weight sources were:

- ProCybernetica / Prophet Ecosystem Controlplane technical paper;
- ProCybernetica Volume I Expanded Monograph;
- ProCybernetica Volume II Prophet Architecture Specification;
- ProCybernetica Volume III Executable Specification Pack and Conformance Law;
- ProCybernetica Volume VIII Autonomic Constitution and Collective Stabilization;
- Book VIII lawful-learning / constitutional control draft;
- coherence / contradiction / re-anchoring addendum.

These sources supplied the constitutional scoring logic:

- Fractal Node Contract;
- lifecycle supervision;
- typed verbs;
- three-tier memory;
- belief-state world modeling;
- explicit value judgment;
- replay and provenance;
- promotion law;
- contradiction handling;
- constitutional stabilization;
- re-anchoring.

## Non-doctrinal input data

The lab universe and live public-surface state came from the previously built frontier-lab monitoring and dossier pipeline, not generic web crawling in the scoring step.

That monitoring system already held:

- 100-lab roster;
- region buckets;
- monitoring priority;
- footprint class;
- public-surface verification confidence;
- repeat-pass status;
- route-retune history;
- escalation state;
- monitoring deltas;
- contradiction/risk flags.

## Scoring model

Two primary composite scores are defined:

- `POA` — ProCybernetica Operational Alignment;
- `EGA` — EpiCybernetica Governance Alignment.

The final composite is a weighted total.

## Scoring scale

The score scale is 0–5:

| Score | Meaning |
| --- | --- |
| 0 | absent or directly incompatible |
| 1 | mostly implicit or marketing-only |
| 2 | partial or local evidence |
| 3 | clear subsystem evidence |
| 4 | systematic and repeatable |
| 5 | constitutional or productized |

## Lab dimensions

Labs were scored on 11 dimensions:

- controlplane explicitness;
- lifecycle discipline;
- typed interfaces;
- memory/repository constitution;
- belief/world-model discipline;
- value judgment and policy constraints;
- replay/provenance;
- learning governance;
- human override;
- contradiction/re-anchoring;
- assurance artifacts.

## Model dimensions

Models were scored on 11 parallel dimensions:

- typed action/interface fit;
- world-model usefulness;
- calibration discipline;
- policy-bound execution fit;
- replayability;
- memory compatibility;
- promotion/rollback compatibility;
- explainability;
- embodiment separation;
- contradiction/coherence behavior;
- evaluation evidence.

## Production method

The scoring pipeline had two layers.

Layer A: calibration override. A small anchor set of labs and model families received analyst-seeded calibration scores because their public surfaces and doctrinal fit were rich enough to support stronger constitutional judgment.

Layer B: heuristic seed scoring. The remainder of the 100-lab universe was scored from monitored public-surface state.

Heuristic variables included:

- footprint class;
- region bucket;
- monitoring priority;
- public verification confidence;
- availability of public repos, docs, model hubs, blogs, and community surfaces;
- repeat-pass stability and route-retune state;
- open escalation and contradiction/risk flags.

These variables mapped into constitutional heuristics for explicitness, replayability, governance visibility, and re-anchoring readiness.

## Evidence registry

The evidence registry was expanded to subject-by-dimension granularity.

For labs, this yielded 100 labs × 11 dimensions = 1,100 evidence rows.

Each row records:

- subject type;
- subject;
- watch ID;
- dimension;
- score;
- weight;
- rollup mapping;
- evidence confidence;
- primary evidence URLs;
- monitoring evidence summary;
- scoring basis;
- interpretation note.

The source states this is materially stronger than a subject-level note, but not yet a final citation-grade evidence book for every long-tail row.

## Monitoring delta layer

A 100-row monitoring delta layer was built from live monitoring console state. It carries:

- total change count;
- change severity;
- repeat-pass count;
- repeat SLA status;
- surface stability trend;
- persistent issue flag;
- issue-resolved flag;
- open escalation after repeat;
- last event type;
- last trigger class;
- changed fields;
- contradiction flags;
- top risk.

This layer feeds dashboard drift and contradiction views.

## Dashboard asset generation

The dashboard payload joins:

- scoring;
- evidence confidence;
- model-family seed scoring;
- monitoring deltas.

Dashboard views include leaderboard, evidence, drift, contradiction, and subject profile surfaces.

## Validation performed

The source says validation included:

- rebuilding the local scoring workbook from repaired v2 body;
- checking row counts for 100-lab body, 20 model-family seed rows, 1,100 evidence rows, and 100 monitoring delta rows;
- generating a live dashboard export payload;
- building customer-facing starter assets;
- creating Drive-native scoring workbooks and notes;
- rendering local PDF dossier.

## Known limitations

- Long-tail 100-lab scoring remains provisional seed scoring beyond calibration anchors.
- Evidence registry is structurally complete but not fully curated to citation-grade depth on every dimension.
- Monitoring drift is represented through console metadata, not yet full historical score-time series.
- Some public vendor surfaces remain brittle or gated, affecting evidence confidence.

## Current-state caution

There is some tension between Drive notes:

- `ProCybernetica Dashboard Asset Notes - v1` states that the Drive-native scoring workbook includes the full lab scoring body, model-family seed sheet, and dashboard export full tab.
- `ProCybernetica Full Scoring Mirror Status and Artifact Inventory - v1` states that the clean workbook shell and structural tabs exist, but the 100-row full scoring body, 1,100-row evidence registry, 100-row monitoring delta layer, and 120-row live dashboard export body were not yet fully mirrored into the Drive workbook.

Observed through the connector during capture:

- the workbook metadata shows tabs for Summary, Rubric_Definitions, Full_Lab_Scoring_v2, Model_Families_Seed, Evidence_Registry_Detail, Monitoring_Deltas, Dashboard_Export_Live, and Artifact_Inventory;
- the Summary tab reports Lab rows = 100, Model-family rows = 20, Evidence registry rows = 1100, Monitoring delta rows = 100, Dashboard export rows = 120;
- direct range reads of `Full_Lab_Scoring_v2!A1:Z10` and `Dashboard_Export_Live!A1:Z5` returned no values through the connector during this pass.

Therefore the repo should record the intended artifact state and the observed connector-visible state separately. If material is missing, it can be recreated or re-ingested later. This capture records what we have and what we observed.

## Immediate next steps from source

- promote repaired scoring, evidence, monitoring, and export tabs into a single canonical Drive-native full workbook;
- deepen long-tail evidence from structural rows into curated dimension-level support;
- wire dashboard starter to live monitoring refresh cycle;
- update drift and contradiction views over time.

## Codification implications

This source supports:

- `docs/scoring/README.md`;
- `docs/dashboard/README.md`;
- future scoring schema definitions;
- future dashboard payload schema capture;
- evidence-registry ingestion issue;
- monitoring-delta time-series issue;
- role-based sharing and redaction issue.

## Capture status

Captured into GitHub as structured source-state. This is not a replacement for the original Drive documents. It records current methodology, intended artifact state, connector-observed state, and known gaps.
