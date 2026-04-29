# Dashboard Export Schema

This document defines the public-safe dashboard export shape for ProCybernetica scoring and evidence views.

## Top-level shape

```json
{
  "schema_version": "0.1.0",
  "generated_at": "2026-04-29T00:00:00Z",
  "subjects": [],
  "evidence": [],
  "monitoring_deltas": []
}
```

## Subject object

| Field | Type | Notes |
| --- | --- | --- |
| subject_type | string | lab / model_family / other |
| subject | string | public subject name |
| watch_id | string | stable identifier |
| poa_score | number | 0 to 5 |
| ega_score | number | 0 to 5 |
| composite_score | number | 0 to 5 |
| evidence_confidence | string | low / medium / high |
| flags | array[string] | public-safe rollup flags |

## Evidence object

| Field | Type | Notes |
| --- | --- | --- |
| subject | string | public subject name |
| dimension | string | scoring dimension |
| score | number | 0 to 5 |
| rollup | string | POA / EGA / Composite |
| evidence_confidence | string | low / medium / high |
| public_summary | string | public-safe basis |
| urls | array[string] | public links only |

## Monitoring delta object

| Field | Type | Notes |
| --- | --- | --- |
| subject | string | public subject name |
| total_change_count | integer | non-negative |
| change_severity | string | none / low / medium / high |
| surface_stability_trend | string | stable / improving / degrading / unknown |
| contradiction_flag | boolean | public-safe flag |
| top_risk | string | public-safe summary |

## Validation rules

- Scores must be between 0 and 5.
- Public payloads must not include secrets or private data.
- URLs must be public-safe.
- Evidence rows should retain dimension-level support when available.
- If raw evidence is unavailable, use synthetic fixtures and mark them clearly.
