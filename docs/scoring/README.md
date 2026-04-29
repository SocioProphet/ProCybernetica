# ProCybernetica Scoring

This directory captures the scoring and evidence methodology for ProCybernetica alignment work.

The scoring system is part of the blueprint. It should be preserved, published, and made inspectable before it is rebuilt, re-ingested, or turned into dashboard code.

## Public-first scoring posture

Scoring methodology, dimensions, rubrics, evidence-shape, validation checks, and dashboard schema should be public by default.

Raw scoring/evidence bodies should also be published if they are public-safe. If any row contains customer/user-private data, live private telemetry, restricted third-party material, or sensitive operational evidence, publish a sanitized row, synthetic fixture, methodology, schema, or validation summary instead.

Do not treat “not yet clean” as a reason to hide the scoring system. Mark incomplete artifacts as provisional and publish the public-safe state.

## Primary concepts

`POA` means ProCybernetica Operational Alignment.

`EGA` means EpiCybernetica Governance Alignment.

The composite score is a weighted rollup of operational and governance alignment.

## Scoring scale

| Score | Meaning |
| --- | --- |
| 0 | absent or directly incompatible |
| 1 | mostly implicit or marketing-only |
| 2 | partial or local evidence |
| 3 | clear subsystem evidence |
| 4 | systematic and repeatable |
| 5 | constitutional or productized |

## Lab scoring dimensions

The captured scoring methodology names 11 lab dimensions:

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

## Model-family scoring dimensions

The captured methodology names 11 model dimensions:

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

## Evidence registry shape

The intended evidence registry is subject-by-dimension.

For the lab universe, the expected shape is 100 labs × 11 dimensions = 1,100 evidence rows.

Each row should carry subject, watch ID, dimension, score, weight, rollup mapping, evidence confidence, primary evidence URLs, monitoring summary, scoring basis, and interpretation note.

## Current capture state

See:

- `../source-captures/SCORING_METHODOLOGY_CAPTURE.md`
- `../source-captures/DASHBOARD_ARTIFACT_INVENTORY_CAPTURE.md`

Important caveat: the blueprint records intended and locally rebuilt heavy data bodies, but those bodies are not yet committed to this public repository. Do not claim they are present here until they are actually ingested.

## Future work

- Locate or recreate the repaired workbook/CSV/JSON artifacts.
- Verify row counts and schema shape.
- Classify artifacts using `../PUBLICATION_MATRIX.md`.
- Publish raw artifacts when public-safe.
- Publish sanitized or synthetic fixtures when raw artifacts contain narrow excluded material.
- Publish schemas, validation checks, row counts, methodology, and reproduction plans even when raw evidence cannot be published.
