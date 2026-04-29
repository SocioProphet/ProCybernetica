# Publication Matrix

ProCybernetica is public-first.

This matrix converts the public-first decision into operational publication rules.

## Default rule

Publish the blueprint, doctrine, methodology, schemas, profiles, examples, tests, source captures, reconciliation records, conformance law, and reference implementation work.

Sanitize only where a specific narrow exclusion applies.

## Artifact classes

| Artifact class | Default disposition | Notes |
| --- | --- | --- |
| Source captures | public | Captures preserve the blueprint and should remain public unless a source contains prohibited private material. |
| Doctrine and architecture docs | public | Core trust surface. Publish. |
| Reconciliation docs | public | Public disagreement and ambiguity are preferable to hidden normalization. |
| Decision records | public | Public architecture needs public decisions. |
| JSON Schemas | public | Standards surface. Publish. |
| YAML profiles | public | Standards surface. Publish. |
| Example fixtures | public or public-synthetic | Use synthetic examples where real evidence contains private material. |
| Conformance tests | public | Public standard requires public tests. |
| Reference implementation | public | Keep secrets and deployment bindings out. |
| Scoring methodology | public | Publish methodology and dimensions. |
| Scoring data | public or public-sanitized | Publish unless it contains private data, restricted third-party material, or sensitive operational evidence. |
| Evidence registry | public or public-sanitized | Prefer URLs, summaries, and evidence confidence; redact only narrow private details. |
| Dashboard schemas | public | Publish schemas and loaders. |
| Dashboard sample payloads | public or public-synthetic | Use sanitized or synthetic data if needed. |
| Live private telemetry | withheld-specific | Publish schema/methodology, not live private data. |
| Credentials/secrets | withheld-specific | Never commit. |
| Customer/user-private data | withheld-specific | Never commit unless explicitly anonymized and cleared. |
| Deployment configs | public-sanitized or withheld-specific | Publish generic examples; withhold secrets and sensitive topology. |

## Withholding rule

Withholding must be specific.

Bad: “internal.”

Good: “withheld-specific: contains customer identifiers and live private telemetry; publish synthetic fixture and schema instead.”

## Public-safe substitutes

When raw material cannot be published, publish one or more of:

- schema;
- synthetic fixture;
- redacted fixture;
- summary;
- methodology;
- provenance note;
- row counts and validation checks;
- reproduction instructions;
- ingestion plan.

## Trust principle

The public should be able to understand what the system claims, how it is governed, how it is evaluated, how it fails, and how it improves.

Public-first publication is part of the architecture, not a marketing layer.
