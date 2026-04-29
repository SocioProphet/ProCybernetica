# Blueprint Positioning

ProCybernetica is being codified as a blueprint-preservation and executable-specification repository.

The immediate task is not to invent a new architecture from scratch. The task is to preserve, normalize, reconcile, and executable-codify the existing blueprint contained in the Drive corpus.

## Positioning rule

This repository should treat the source corpus as a blueprint with provenance.

That means:

- preserve the blueprint's architecture, vocabulary, doctrine, and program state before extending it;
- distinguish source capture from interpretation;
- distinguish interpretation from implementation;
- record open ambiguities rather than silently resolving them;
- keep authorial and source provenance visible;
- avoid presenting later scaffolding as if it were the original blueprint;
- make the repository self-contained enough that agents and engineers can build from the captured blueprint.

## Correct order of operations

1. Capture the blueprint.
2. Index the source corpus.
3. Reconcile vocabulary and decisions across sources.
4. Mark conflicts and open questions.
5. Codify machine-readable contracts.
6. Build the reference implementation.
7. Integrate platform, agent, repository, and host-trust work.

## Agent instruction

Agents working in this repository should treat `docs/source-captures/` and `docs/CORPUS_INDEX.md` as the primary orientation layer.

Do not begin by inventing code, schemas, or architecture beyond what the captured corpus supports. When a gap appears, write it down as a gap or open decision.

## Public repository role

This public repository is the codified blueprint surface. It should contain source-state captures, normalized doctrine, public standards, schemas, profiles, examples, conformance tests, and eventually a reference implementation.

It should not contain private data, operational secrets, live telemetry, or unreviewed private evidence.
