# Public-First Scoring and Dashboard Ingestion Plan

Status: planning artifact for public-safe ingestion.

This plan follows `docs/decisions/0001-public-first-transparency.md` and `docs/PUBLICATION_MATRIX.md`.

## Objective

Publish the ProCybernetica scoring and dashboard artifacts in the public repository wherever possible.

The public should be able to inspect the methodology, schemas, scoring dimensions, row-count expectations, validation checks, and evidence posture.

## Known blueprint state

The captured blueprint records these intended bodies:

| Body | Expected rows |
| --- | ---: |
| Lab scoring | 100 |
| Model-family seed scoring | 20 |
| Evidence registry | 1,100 |
| Monitoring deltas | 100 |
| Dashboard export | 120 |

The source inventory says repaired local artifacts existed for scoring, evidence, monitoring deltas, workbook, dashboard export, starter UI, loader, schema, and README.

During capture, workbook metadata and the Summary tab were visible. Some heavy tabs were structurally present but returned no values through the connector path used in that pass.

Therefore ingestion must distinguish intended state, local artifact state, Drive-visible state, and GitHub-committed state.

## Publication classification

| State | Meaning | Action |
| --- | --- | --- |
| `public` | safe to publish directly | commit artifact |
| `public-sanitized` | safe after removing narrow sensitive fields | commit sanitized artifact and note changes |
| `public-synthetic` | raw material cannot be public, but shape can be | commit synthetic fixture and schema |
| `withheld-specific` | cannot be public for a named reason | publish method, schema, counts, checks, and reason |

## Artifact target

| Artifact | Preferred disposition | Fallback |
| --- | --- | --- |
| scoring rubric | public | none expected |
| scoring dimensions | public | none expected |
| POA/EGA methodology | public | none expected |
| lab scoring table | public | public-sanitized |
| model-family seed table | public | public-sanitized |
| evidence registry | public or public-sanitized | public-synthetic |
| monitoring deltas | public or public-sanitized | public-synthetic |
| dashboard export schema | public | none expected |
| dashboard export payload | public | public-sanitized or public-synthetic |
| dashboard starter UI | public | none expected |
| dashboard loader | public | none expected |

## Required public artifacts

At minimum, the repository should contain public-safe versions of:

```text
docs/scoring/rubric.md
docs/scoring/schema.md
docs/dashboard/export-schema.md
examples/scoring/lab_scoring.sample.csv
examples/scoring/evidence_registry.sample.csv
examples/scoring/monitoring_deltas.sample.csv
examples/dashboard/dashboard_export.sample.json
```

Sample files may be synthetic if raw artifacts are unavailable or not yet cleared.

## Validation checks

Ingestion should check:

- expected row counts;
- required columns;
- score range 0 to 5;
- every row has subject and dimension;
- evidence-confidence fields exist;
- dashboard export validates against schema;
- no sensitive values are present in public artifacts.

## Public-safe substitution rule

If raw material cannot be published, publish the public-safe substitute:

- schema;
- synthetic fixture;
- sanitized fixture;
- methodology;
- summary;
- validation checks;
- ingestion notes.

Do not suppress an entire artifact class when a safe form can be published.

## Rebuild path if local artifacts are unavailable

1. Use captured methodology as canonical scoring law.
2. Recreate schema and fixture files first.
3. Rebuild scoring tables from public evidence and monitoring summaries.
4. Mark rebuilt rows as provisional public rebuilds.
5. Preserve intended row counts as target checks.
6. Compare rebuilt coverage against the captured blueprint.

## Next implementation tasks

1. Add public scoring rubric and schema docs.
2. Add dashboard export schema doc.
3. Add synthetic sample fixtures matching expected shapes.
4. Locate or recreate raw heavy artifacts.
5. Classify raw artifacts using the publication matrix.
6. Publish public or sanitized tables.
7. Add validation script after schema/profile reconciliation stabilizes.
