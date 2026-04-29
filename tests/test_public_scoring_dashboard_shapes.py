from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _csv_headers(path: Path) -> list[str]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.reader(handle)
        return next(reader)


def test_lab_scoring_sample_headers() -> None:
    headers = _csv_headers(ROOT / "examples/scoring/lab_scoring.sample.csv")
    expected = {
        "subject_type",
        "subject",
        "watch_id",
        "region_bucket",
        "footprint_class",
        "poa_score",
        "ega_score",
        "composite_score",
        "evidence_confidence",
        "scoring_basis",
        "provisional",
    }
    assert expected.issubset(set(headers))


def test_evidence_registry_sample_headers() -> None:
    headers = _csv_headers(ROOT / "examples/scoring/evidence_registry.sample.csv")
    expected = {
        "subject_type",
        "subject",
        "watch_id",
        "dimension",
        "score",
        "weight",
        "rollup",
        "evidence_confidence",
        "primary_evidence_urls",
        "monitoring_summary",
        "scoring_basis",
        "interpretation_note",
    }
    assert expected.issubset(set(headers))


def test_monitoring_delta_sample_headers() -> None:
    headers = _csv_headers(ROOT / "examples/scoring/monitoring_deltas.sample.csv")
    expected = {
        "subject",
        "watch_id",
        "total_change_count",
        "change_severity",
        "repeat_pass_count",
        "surface_stability_trend",
        "persistent_issue_flag",
        "contradiction_flag",
        "top_risk",
    }
    assert expected.issubset(set(headers))


def test_dashboard_export_sample_shape() -> None:
    payload = json.loads((ROOT / "examples/dashboard/dashboard_export.sample.json").read_text(encoding="utf-8"))
    assert payload["schema_version"] == "0.1.0"
    assert payload["fixture_type"] == "public-synthetic"
    assert isinstance(payload["subjects"], list)
    assert isinstance(payload["evidence"], list)
    assert isinstance(payload["monitoring_deltas"], list)
    assert payload["subjects"], "expected at least one synthetic subject"
