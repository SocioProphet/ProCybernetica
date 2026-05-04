# Agent Instructions

This repository is in blueprint-capture, estate-alignment, and reconciliation mode.

## Prime directive

Preserve, normalize, reconcile, and executable-codify the existing ProCybernetica blueprint before extending or implementing it.

The existing blueprint is represented by the Drive-derived corpus indexed in `docs/CORPUS_INDEX.md` and captured in `docs/source-captures/`.

## Public-first directive

This repository is public-first.

Agents should assume doctrine, source captures, schemas, profiles, examples, conformance tests, scoring methodology, dashboard methodology, and reference implementation work should be public unless a specific narrow exclusion applies.

Do not use vague privacy language to hide the blueprint. If something must be withheld or sanitized, name the reason precisely.

Narrow exclusions:

- credentials, tokens, keys, certificates, and secrets;
- customer or user-private data;
- live private telemetry or operational logs;
- sensitive deployment configuration;
- legally restricted third-party material;
- evidence requiring redaction before publication.

The burden of justification is on withholding, not publishing.

## Required reading before work

1. `docs/BLUEPRINT_POSITIONING.md`
2. `docs/BLUEPRINT_PROVENANCE.md`
3. `docs/CAPTURE_STATUS.md`
4. `docs/CORPUS_INDEX.md`
5. `docs/integration/ESTATE_ALIGNMENT_AUDIT.md`
6. `docs/integration/RECENT_CONTRIBUTION_ALIGNMENT.md`
7. `docs/PUBLICATION_BOUNDARY.md`
8. Relevant files under `docs/source-captures/`

## Estate-alignment rule

Do not work in a vacuum.

Before changing schemas, profiles, runtime code, integration docs, or agent lanes, check:

- the current repository dossier routing rules;
- `docs/integration/ESTATE_ALIGNMENT_AUDIT.md`;
- `docs/integration/RECENT_CONTRIBUTION_ALIGNMENT.md`;
- relevant upstream repos in SocioProphet, SourceOS-Linux, SociOS-Linux, and mdheller.

If another repo already owns a contract/runtime/evidence surface, map to it. Do not fork or duplicate it unless the gap is explicit and documented.

## Operating rules

- Treat Drive as source archive and GitHub as public codification target.
- Do not modify Drive source material from this repository workstream.
- Do not invent architecture beyond the captured corpus without marking it as a proposal.
- Do not treat early schemas, profiles, or runtime scaffolding as canonical until reconciliation completes.
- Prefer capture and reconciliation before implementation.
- Record conflicts, ambiguities, and open decisions explicitly.
- Preserve source provenance in every substantial doctrine or specification document.
- Publish public-safe methodology, schemas, examples, tests, and source-state summaries rather than withholding entire workstreams.

## Work lanes

### Capture lane

Produce repo-local source-state documents under `docs/source-captures/`.

A good capture records:

- source identity;
- source role;
- central thesis;
- normative claims;
- schema/profile implications;
- implementation implications;
- open questions;
- relation to already captured sources.

### Reconciliation lane

Normalize differences among captured sources and upstream estate surfaces.

A good reconciliation records:

- what the sources agree on;
- where names or enums differ;
- what should become canonical for v0;
- what upstream repository owns the runtime, evidence, or contract surface;
- what requires human decision;
- what provisional repo files need correction.

### Implementation lane

Implementation is allowed only after capture/reconciliation/estate mapping makes the target contract clear.

Reference implementation should follow the captured Volume IV kit, the Volume III executable specification pack, Book XI implementation practicum, and estate mapping documents.

### Publication lane

When an artifact contains sensitive material, do not discard the artifact category. Publish the public-safe form:

- schema;
- synthetic fixture;
- redacted fixture;
- methodology;
- summary;
- provenance note;
- ingestion plan.

## Publication boundary

Follow `docs/PUBLICATION_BOUNDARY.md` and `docs/decisions/0001-public-first-transparency.md`.

Do not commit secrets or private data. Everything else should be public by default.
