# Implementation

This directory translates the captured blueprint into implementation plans.

Implementation follows capture and reconciliation. Runtime code should not outpace the public contracts.

## Current implementation posture

1. Reconcile v0 schemas and profiles.
2. Publish public-safe fixtures.
3. Implement the first Book XI vertical slice: ingest to canonical claims.
4. Add replay, promotion, and mesh slices only after the first slice validates cleanly.

## Rule

Do not build a generic agent runtime first. Build the lawful schema, claim, event, provenance, replay, and promotion path first.
