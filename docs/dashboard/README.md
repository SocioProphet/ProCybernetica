# ProCybernetica Dashboard

This directory captures the dashboard blueprint and asset state for ProCybernetica scoring, evidence, drift, contradiction, and subject-profile views.

## Public-first dashboard posture

The dashboard should be public by default because it is part of the trust surface.

Dashboard schemas, loaders, view contracts, sample payloads, evidence-shape, scoring methodology, and validation checks should be public.

Raw dashboard payloads should also be public when public-safe. If raw payload rows include customer/user-private data, live private telemetry, restricted third-party material, or sensitive operational evidence, publish redacted or synthetic fixtures and preserve the full schema and validation checks.

## Captured dashboard views

The dashboard starter is described as supporting:

- leaderboard view;
- evidence registry view;
- drift view;
- contradiction / constitutional risk view;
- selected subject profile with rollup scores and flags.

## Captured local asset set

The dashboard notes name these customer-facing local assets:

- `procybernetica_dashboard_starter_v2.tsx`;
- `procybernetica_dashboard_loader_v2.ts`;
- `procybernetica_dashboard_export_v2_2026-04-11.json`;
- `procybernetica_dashboard_export_schema_v2.json`;
- `procybernetica_dashboard_readme_v2.md`.

These files are recorded as source-state. They are not yet present in this public repository unless committed separately in a later ingestion pass.

## Expected workbook/dashboard row counts

The captured workbook summary reports:

| Body | Expected rows |
| --- | --- |
| Lab scoring | 100 |
| Model-family seed scoring | 20 |
| Evidence registry | 1,100 |
| Monitoring deltas | 100 |
| Dashboard export | 120 |

## Connector-observed caveat

During capture, the workbook metadata and Summary tab were visible. Some heavy tabs appeared structurally present but returned no values through range reads. This may mean the data was not fully mirrored, was outside the requested range, or was not exposed through the connector path used in this pass.

The repository therefore records the intended artifact state and the observed connector-visible state separately.

## Immediate build steps from source

The source notes name these next steps:

1. bind the frontend to the export JSON through the loader helper;
2. expand evidence from subject-level to dimension-level;
3. connect monitoring deltas into drift history;
4. add role-based sharing and customer-safe redaction;
5. add radar/profile charts after evidence expansion.

## Publication boundary

Follow `../PUBLICATION_MATRIX.md`.

Do not commit secrets or private data. Everything else should be public by default.

If raw dashboard data cannot be public, publish:

- dashboard export schema;
- loader contract;
- synthetic fixture;
- redacted fixture;
- row-count validation checks;
- public methodology and provenance notes.

## Source captures

See:

- `../source-captures/SCORING_METHODOLOGY_CAPTURE.md`
- `../source-captures/DASHBOARD_ARTIFACT_INVENTORY_CAPTURE.md`
