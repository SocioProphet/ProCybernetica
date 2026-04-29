# Public-First Publication Boundary

ProCybernetica is a public-first repository.

The point of this repository is to make the blueprint inspectable, criticizable, reproducible, and buildable in public. Trust requires transparency. The default posture is therefore publication, not concealment.

This document defines the narrow boundaries that protect secrets, private data, legal rights, and legitimate safety constraints without weakening the public nature of the blueprint.

See also: `docs/decisions/0001-public-first-transparency.md`.

## Public by default

The following belong in this repository by default:

- doctrine;
- source-state captures;
- blueprint provenance;
- curriculum and textbook index;
- architectural summaries;
- JSON Schemas;
- YAML profiles;
- conformance tests;
- reference implementation code;
- examples and fixtures;
- integration contracts;
- public issue tracking;
- adapter specifications;
- policy examples;
- scoring methodology;
- dashboard methodology;
- public-safe evidence methodology;
- public-safe dashboard schemas and sample payloads;
- build plans, roadmaps, and implementation practicum material.

## Narrow exclusions

The following do not belong in this public repository unless explicitly sanitized, cleared, or represented by safe examples:

- credentials, tokens, keys, certificates, and secrets;
- customer data;
- user-private data;
- live private telemetry or operational logs;
- private deployment configuration that exposes infrastructure or security posture;
- confidential incident records containing private or sensitive operational details;
- third-party material we do not have the right to republish;
- evidence artifacts that contain private data and need redaction before publication.

The burden of justification is on withholding, not publishing.

## Classification language

Use these states for artifacts:

| State | Meaning |
| --- | --- |
| `public` | may be committed directly |
| `public-sanitized` | may be committed after removing private/sensitive fields |
| `public-synthetic` | should be represented with synthetic fixtures |
| `withheld-specific` | withheld for a named, narrow reason |

Do not use vague labels such as “internal” or “private” without explaining what specific boundary applies.

## Drive corpus handling

Drive documents are source material for codification. They should not be modified during GitHub codification unless there is an explicit editorial, archival, or program-management reason.

Codification means:

- reading the Drive corpus;
- preserving source-state captures in `docs/source-captures/`;
- distilling doctrine into public documents;
- translating implementation guidance into schemas, profiles, tests, and code;
- preserving source references in `docs/CORPUS_INDEX.md`;
- moving executable work into GitHub.

Codification does not mean:

- rewriting source Drive documents casually;
- treating the Drive archive as the production implementation;
- copying secrets or private data into public GitHub;
- claiming Drive-local artifacts have been mirrored if they have not.

## Evidence boundary

Evidence should be public where possible.

If evidence includes private data, publish the method, schema, provenance posture, summary, synthetic fixture, or redacted form instead of suppressing the entire evidence layer.

Operational evidence should be excluded only when it contains secrets, customer/user private data, live private telemetry, or legally restricted material.

## Policy boundary

Policy examples and policy doctrine should be public.

Production policy bundles should be published when they are generic and safe. They should be sanitized or represented as examples when they reveal secrets, customer data, infrastructure, or sensitive controls.

## Implementation boundary

The reference implementation should be real enough to run and test.

Deployment bindings may be represented by adapters and examples if live configuration would expose secrets or infrastructure.

Interfaces, contracts, and conformance law should remain public.
