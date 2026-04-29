# ADR-0001: Public-First Transparency Posture

Status: accepted

Date: 2026-04-29

## Context

ProCybernetica is being codified as a public blueprint and executable-specification repository. Trust in the program depends on making the doctrine, architecture, source captures, schemas, profiles, implementation plans, evidence methodology, and conformance posture visible.

The repository was initially framed with a public/private boundary to avoid accidental disclosure of sensitive operational material. That boundary remains necessary for secrets and private data, but it must not become a pretext for hiding the blueprint.

## Decision

ProCybernetica is public-first.

The blueprint, doctrine, source-state captures, architecture maps, schemas, profiles, examples, conformance tests, roadmap, scoring methodology, dashboard methodology, and reference implementation scaffolding should be public by default.

Narrow exclusions are allowed only for:

- credentials, tokens, keys, certificates, and secrets;
- customer data or user-private data;
- live private telemetry or operational logs;
- private deployment configuration that would expose infrastructure or security posture;
- third-party material we do not have the right to republish;
- sensitive evidence that must be summarized or sanitized before publication.

## Rationale

The program should be inspectable. If the architecture is serious, the public should be able to see the blueprint, criticize it, reproduce it, and evaluate whether implementation follows doctrine.

Public trust is not created by withholding the work. Public trust is created by publishing the doctrine and evidence posture while still protecting legitimate privacy, safety, and legal boundaries.

## Consequences

- Repository docs should use public-first language.
- Capture documents should remain public unless they contain prohibited sensitive material.
- Data artifacts should be classified as public, sanitized-public, or excluded-for-specific-reason.
- Exclusions must be explicit and narrow.
- The burden of justification is on withholding, not publishing.

## Implementation notes

Update `docs/PUBLICATION_BOUNDARY.md` to describe a public-first transparency policy rather than a broad private/public split.

Future scoring/dashboard ingestion work must prefer public-safe publication, with redaction only where required.
