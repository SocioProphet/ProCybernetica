from __future__ import annotations

from pathlib import Path

from procyber.validate import load_json
from procyber.schema_bundle import SchemaBundle

ROOT = Path(__file__).resolve().parents[1]


def test_book_xi_slice_a_public_fixtures_validate() -> None:
    bundle = SchemaBundle(ROOT / "schemas")
    cases = [
        ("artifact_envelope", ROOT / "examples/practicum/artifact_envelope.example.json"),
        ("claim", ROOT / "examples/practicum/claim.example.json"),
        ("provenance_record", ROOT / "examples/practicum/provenance_record.example.json"),
        ("event_envelope", ROOT / "examples/practicum/event_envelope.example.json"),
        ("trace_event", ROOT / "examples/practicum/trace_event.example.json"),
    ]
    for schema_name, path in cases:
        bundle.validate(schema_name, load_json(path))


def test_scoring_public_fixtures_exist() -> None:
    expected = [
        ROOT / "examples/scoring/lab_scoring.sample.csv",
        ROOT / "examples/scoring/evidence_registry.sample.csv",
        ROOT / "examples/scoring/monitoring_deltas.sample.csv",
        ROOT / "examples/dashboard/dashboard_export.sample.json",
    ]
    for path in expected:
        assert path.exists(), f"missing public fixture: {path}"
