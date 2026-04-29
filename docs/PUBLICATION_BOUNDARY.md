# Publication Boundary

ProCybernetica is a public repository. It should be useful, rigorous, and implementation-grade without leaking operationally sensitive material.

## Public by default

The following belong in this repository:

- public doctrine;
- public curriculum and textbook index;
- public architectural summaries;
- JSON Schemas;
- YAML profiles;
- conformance tests;
- reference implementation code;
- examples with synthetic data;
- integration contracts;
- public issue tracking;
- adapter specifications;
- non-secret policy examples;
- non-sensitive dashboard schemas.

## Keep out of this repository

The following do not belong in this public repository:

- customer data;
- user-private data;
- private telemetry;
- production credentials;
- tokens, keys, certificates, or secrets;
- private deployment policy;
- non-public incident records;
- confidential vendor data;
- sensitive infrastructure topology;
- live operational logs;
- unreleased customer-specific dashboards;
- proprietary datasets not explicitly cleared for public release.

## Drive corpus handling

Drive documents are source material for codification. They should not be modified during GitHub codification unless there is an explicit editorial, archival, or program-management reason.

Codification means:

- reading the Drive corpus;
- distilling doctrine into public documents;
- translating implementation guidance into schemas, profiles, tests, and code;
- preserving source references in `docs/CORPUS_INDEX.md`;
- moving executable work into GitHub.

Codification does not mean:

- rewriting source Drive documents casually;
- treating the Drive archive as the production implementation;
- copying confidential or unsuitable material into public GitHub;
- claiming Drive-local artifacts have been mirrored if they have not.

## Evidence boundary

Evidence artifacts should be classified before publication.

Public examples may use synthetic or sanitized evidence.

Operational evidence should remain in private or platform repositories unless explicitly cleared.

## Policy boundary

Policy examples may be public. Production policy bundles should be kept in operational repositories when they reveal infrastructure, customers, users, or sensitive controls.

## Implementation boundary

The reference implementation should be real enough to run and test, but it should avoid embedding assumptions that only apply to one private deployment.

Adapters should expose interfaces. Production bindings should live in the repositories that own those deployments.
