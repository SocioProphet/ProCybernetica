# Agent Instructions

This repository is in blueprint-capture mode.

## Prime directive

Preserve, normalize, reconcile, and executable-codify the existing ProCybernetica blueprint before extending or implementing it.

The existing blueprint is represented by the Drive-derived corpus indexed in `docs/CORPUS_INDEX.md` and captured in `docs/source-captures/`.

## Required reading before work

1. `docs/BLUEPRINT_POSITIONING.md`
2. `docs/CAPTURE_STATUS.md`
3. `docs/CORPUS_INDEX.md`
4. Relevant files under `docs/source-captures/`

## Operating rules

- Treat Drive as source archive and GitHub as codification target.
- Do not modify Drive source material from this repository workstream.
- Do not invent architecture beyond the captured corpus without marking it as a proposal.
- Do not treat early schemas, profiles, or runtime scaffolding as canonical until reconciliation completes.
- Prefer capture and reconciliation before implementation.
- Record conflicts, ambiguities, and open decisions explicitly.
- Preserve source provenance in every substantial doctrine or specification document.

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

Normalize differences among captured sources.

A good reconciliation records:

- what the sources agree on;
- where names or enums differ;
- what should become canonical for v0;
- what requires human decision;
- what provisional repo files need correction.

### Implementation lane

Implementation is allowed only after capture/reconciliation makes the target contract clear.

Reference implementation should follow the captured Volume IV kit and the Volume III executable specification pack.

## Public/private boundary

Follow `docs/PUBLICATION_BOUNDARY.md`. Do not commit secrets, customer data, private telemetry, live operational logs, or confidential evidence.
