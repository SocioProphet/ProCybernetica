# Source Capture: Dashboard Assets and Artifact Inventory

Sources:

- `ProCybernetica Dashboard Asset Notes - v1`
- `ProCybernetica Full Scoring Mirror Status and Artifact Inventory - v1`
- `ProCybernetica Alignment Scoring Workbook - Full v3`
- `Prophet Platform & ProCybernetica` Drive folder

Capture purpose: preserve the current dashboard asset, workbook, and artifact-inventory state so the repository can distinguish existing blueprint state from future rebuild or ingestion work.

## Dashboard asset notes state

The dashboard notes state that the Drive-native scoring workbook includes:

- full lab scoring body;
- model-family seed sheet;
- dashboard export full tab.

Customer-facing local asset set named in the source:

- `procybernetica_dashboard_starter_v2.tsx`;
- `procybernetica_dashboard_loader_v2.ts`;
- `procybernetica_dashboard_export_v2_2026-04-11.json`;
- `procybernetica_dashboard_export_schema_v2.json`;
- `procybernetica_dashboard_readme_v2.md`.

Dashboard starter capabilities:

- leaderboard view;
- evidence registry view;
- drift view;
- contradiction / constitutional risk view;
- selected subject profile with rollup scores and flags.

Immediate build steps named in the dashboard notes:

1. bind the frontend to the export JSON through the loader helper;
2. expand evidence from subject-level to dimension-level;
3. connect monitoring deltas into drift history;
4. add role-based sharing and customer-safe redaction;
5. add radar/profile charts after evidence expansion.

## Artifact inventory state

The artifact inventory states that a clean Drive-native full workbook shell exists and that the methodology/provenance dossier exists in Drive.

It says repaired heavy data bodies were rebuilt and validated locally:

- full 100-lab scoring CSV;
- 1,100-row evidence registry CSV;
- 100-row monitoring delta CSV;
- local repaired XLSX workbook;
- live dashboard export JSON;
- dashboard starter, loader, schema, and README;
- methodology/provenance PDF.

It lists these artifacts as already in Drive:

- `ProCybernetica Alignment Scoring Workbook - Full v3`;
- `ProCybernetica Scoring Methodology and Data Provenance Dossier - v1`;
- `ProCybernetica Dashboard Asset Notes - v1`;
- `ProCybernetica Full Scoring Mirror Status and Artifact Inventory - v1`.

It states these were mirrored into the Drive workbook already:

- clean workbook shell;
- core structural tabs;
- summary and rubric tabs;
- model-family seed tab;
- artifact inventory tab.

It states these were not yet fully mirrored into the Drive workbook:

- 100-row full scoring body;
- 1,100-row detailed evidence registry;
- 100-row monitoring delta layer;
- 120-row live dashboard export body.

The reason recorded in the artifact inventory is that the runtime exposed native Sheet creation and cell-level editing, but not a direct bulk-import path from repaired local CSV/JSON artifacts into the native Sheet at required volume.

Operational recommendation from the artifact inventory: treat the repaired local workbook and CSV/JSON files as the current fullest source of truth until a later pass finishes the Drive-native bulk mirror using a path that supports large structured ingestion cleanly.

## Workbook metadata observed during capture

Workbook: `ProCybernetica Alignment Scoring Workbook - Full v3`

Observed tabs:

- `Summary`;
- `Rubric_Definitions`;
- `Full_Lab_Scoring_v2`;
- `Model_Families_Seed`;
- `Evidence_Registry_Detail`;
- `Monitoring_Deltas`;
- `Dashboard_Export_Live`;
- `Artifact_Inventory`.

The `Summary` tab reported:

| Field | Value |
| --- | --- |
| Purpose | Canonical Drive-native full scoring surface for ProCybernetica alignment and customer dashboard feeds |
| Lab rows | 100 |
| Model-family rows | 20 |
| Evidence registry rows | 1100 |
| Monitoring delta rows | 100 |
| Dashboard export rows | 120 |
| Primary composites | POA / EGA / Composite |
| Current state | Repaired v2 scoring mirrored into clean v3 workbook |
| Primary caution | Long-tail lab scoring remains provisional seed scoring beyond the anchor calibration set |
| Next operational step | Wire dashboard frontend to live export and continue evidence deepening |

Connector-observed caveat during capture:

- Reading `Full_Lab_Scoring_v2!A1:Z10` returned no values.
- Reading `Dashboard_Export_Live!A1:Z5` returned no values.

This does not prove the local repaired artifacts do not exist. It records only what was visible through the Drive connector during this capture pass.

## Current-state interpretation

The blueprint state should be captured as follows:

1. The scoring/dashboard program exists as an intended and partially mirrored artifact set.
2. There is strong methodology and inventory documentation.
3. The Drive workbook structure and summary tab exist.
4. The heavy data bodies may not be fully visible/mirrored in the Drive workbook through the connector.
5. The local repaired workbook/CSV/JSON artifacts were described as the fullest source of truth by the inventory document.
6. If heavy data bodies are missing from Drive/GitHub, they can be recreated or re-ingested later.

## Codification requirements

The GitHub repository should not claim that the 100-lab body, 1,100-row evidence registry, 100-row monitoring delta layer, or 120-row dashboard export body are committed until they actually are.

Instead, GitHub should preserve:

- methodology;
- workbook and tab inventory;
- dashboard asset list;
- intended row counts;
- connector-observed gaps;
- source-of-truth caveat;
- future ingestion plan.

## Future ingestion work

A later ingestion pass should:

1. locate the repaired local XLSX/CSV/JSON artifacts;
2. verify row counts;
3. commit sanitized schemas and sample fixtures to GitHub if public-safe;
4. import or regenerate canonical public-safe dashboard payloads;
5. document any redaction policy;
6. wire dashboard assets to the canonical export format;
7. keep customer/private data out of the public repository.

## Capture status

Captured into GitHub as structured source-state. This file records the dashboard and artifact-inventory blueprint as found, including contradictions and missing/uncertain material. Missing material can be recreated later; this capture intentionally preserves the present state without overstating completion.
