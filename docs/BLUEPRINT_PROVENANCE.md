# Blueprint Provenance

ProCybernetica is being codified from an existing blueprint corpus.

This repository is not the origin of the blueprint. It is the public GitHub surface that preserves, normalizes, reconciles, and executable-codifies it.

## Source archive

The source archive is the Drive corpus indexed in `docs/CORPUS_INDEX.md` and captured into repo-local source-state documents under `docs/source-captures/`.

The source archive should remain intact. Drive source documents should not be modified during GitHub codification unless there is an explicit editorial, archival, or program-management reason.

## Repo-local source state

The `docs/source-captures/` directory is the first repo-local truth layer.

A source capture is not a replacement for the original Drive artifact. It is a structured preservation of:

- document identity;
- thesis;
- normative claims;
- schema/profile implications;
- implementation implications;
- open gaps or contradictions;
- codification implications.

## Authorship posture

The repo should not present later scaffolding as if it were the original blueprint.

When a document is a capture, call it a capture.

When a document is a reconciliation, call it a reconciliation.

When a document is a proposal beyond the captured corpus, call it a proposal.

When code is provisional, mark it provisional.

## Implementation posture

Implementation follows reconciliation.

The captured blueprint already contains implementation guidance in Volume III, Volume IV, and Book XI. The reference implementation should be derived from those sources, not invented as an unrelated runtime.

## Provenance rule for agents

Agents must preserve source provenance when creating or modifying doctrine and specification files.

A strong change references the source capture it came from and records any conflict with other captures.

## Current caveat

Some provisional schema, profile, and runtime scaffolding was added before the capture-first posture was corrected. Those files should be reconciled against the captured blueprint before being treated as canonical.
