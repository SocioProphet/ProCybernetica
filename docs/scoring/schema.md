# Scoring Data Shape

This document defines the public expected shape for ProCybernetica scoring artifacts.

## Lab scoring table

Expected row count: 100.

Required columns:

| Column | Type | Notes |
| --- | --- | --- |
| subject_type | string | usually `lab` |
| subject | string | public subject name |
| watch_id | string | stable watch/list identifier |
| region_bucket | string | region grouping when available |
| footprint_class | string | public footprint category |
| poa_score | number | 0 to 5 |
| ega_score | number | 0 to 5 |
| composite_score | number | 0 to 5 |
| evidence_confidence | string | low / medium / high |
| scoring_basis | string | summary of basis |
| provisional | boolean | true if seed/provisional scoring |

## Model-family seed table

Expected row count: 20.

Required columns:

| Column | Type | Notes |
| --- | --- | --- |
| subject_type | string | usually `model_family` |
| subject | string | model family name |
| family_class | string | VLA, LLM, world model, planner, etc. |
| poa_score | number | 0 to 5 |
| ega_score | number | 0 to 5 |
| composite_score | number | 0 to 5 |
| evidence_confidence | string | low / medium / high |
| scoring_basis | string | summary of basis |

## Evidence registry

Expected row count: 1,100 for the 100-lab × 11-dimension body.

Required columns:

| Column | Type | Notes |
| --- | --- | --- |
| subject_type | string | lab / model_family / other |
| subject | string | public subject name |
| watch_id | string | stable watch/list identifier |
| dimension | string | one rubric dimension |
| score | number | 0 to 5 |
| weight | number | dimension weight |
| rollup | string | POA / EGA / Composite mapping |
| evidence_confidence | string | low / medium / high |
| primary_evidence_urls | string | pipe-separated or JSON array in future schema |
| monitoring_summary | string | public-safe summary |
| scoring_basis | string | basis of score |
| interpretation_note | string | public note about interpretation |

## Monitoring deltas

Expected row count: 100.

Required columns:

| Column | Type | Notes |
| --- | --- | --- |
| subject | string | public subject name |
| watch_id | string | stable watch/list identifier |
| total_change_count | integer | non-negative |
| change_severity | string | none / low / medium / high |
| repeat_pass_count | integer | non-negative |
| surface_stability_trend | string | stable / improving / degrading / unknown |
| persistent_issue_flag | boolean | public-safe flag |
| contradiction_flag | boolean | public-safe flag |
| top_risk | string | public-safe risk summary |

## Validation rules

- scores must be between 0 and 5;
- expected row counts must be documented;
- subject and dimension must be present where required;
- evidence confidence must be low, medium, or high;
- public artifacts must not include secrets or private data;
- sanitized artifacts must document what class of field was removed.
