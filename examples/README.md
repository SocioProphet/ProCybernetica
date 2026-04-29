# Examples

This directory contains public-safe examples and fixtures for ProCybernetica.

The repository is public-first. Examples should be public, public-sanitized, or public-synthetic. Do not wait for private data to demonstrate the contract shape.

## Practicum fixtures

`examples/practicum/` contains synthetic fixtures for Book XI Slice A and the minimal constitutional loop.

Validated by `tests/test_public_fixtures_validate.py`:

- `artifact_envelope.example.json`
- `claim.example.json`
- `provenance_record.example.json`
- `event_envelope.example.json`
- `trace_event.example.json`
- `command_envelope.example.json`
- `delegation_envelope.example.json`
- `status_envelope.example.json`
- `capability_descriptor.example.json`
- `replay_envelope.example.json`
- `evaluation_result.example.json`
- `promotion_decision.example.json`

## Scoring fixtures

`examples/scoring/` contains public-synthetic scoring fixtures:

- `lab_scoring.sample.csv`
- `evidence_registry.sample.csv`
- `monitoring_deltas.sample.csv`

## Dashboard fixtures

`examples/dashboard/` contains public-synthetic dashboard fixtures:

- `dashboard_export.sample.json`

## Rule

If raw material cannot be published, add a synthetic or sanitized fixture that preserves the shape, validation path, and public methodology.
