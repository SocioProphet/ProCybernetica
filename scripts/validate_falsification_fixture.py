#!/usr/bin/env python3
"""Validate public falsification fixture files.

The fixture format is deliberately small and repository-local. It validates that
fixture-backed falsification observables have public-safe, structured examples.
It does not claim runtime telemetry or production monitoring coverage.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CROSS_REF_PATH = ROOT / "docs" / "falsification" / "observable-cross-reference.md"
FIXTURE_DIR = ROOT / "tests" / "fixtures" / "falsification"

REQUIRED_FIXTURE_FIELDS = {
    "fixture_id",
    "observable_id",
    "fixture_kind",
    "expected_result",
    "public_state",
    "condition",
    "detection_mechanism",
    "revision_direction",
    "owner",
    "non_claims",
}

VALID_EXPECTED_RESULTS = {"pass", "fail", "review_required", "deferred"}
VALID_PUBLIC_STATES = {"public", "public-sanitized", "public-synthetic"}
VALID_FIXTURE_KINDS = {
    "positive_fixture",
    "negative_fixture",
    "synthetic_case",
    "coverage_marker",
    "deferred_marker",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def extract_json_block(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"```json\s*\n(?P<payload>.*?)\n```", text, flags=re.DOTALL)
    if not match:
        fail(f"{path} does not contain a JSON code block")
    try:
        return json.loads(match.group("payload"))
    except json.JSONDecodeError as exc:
        fail(f"{path} contains malformed JSON: {exc}")


def known_observable_ids() -> set[str]:
    registry = extract_json_block(CROSS_REF_PATH)
    return {obs["id"] for obs in registry.get("observables", []) if isinstance(obs, dict) and "id" in obs}


def validate_fixture_file(path: Path, known_ids: set[str]) -> int:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"{path} contains malformed JSON: {exc}")

    if payload.get("fixture_set_version") != "v1":
        fail(f"{path} must set fixture_set_version to v1")
    if payload.get("publication_state") not in VALID_PUBLIC_STATES:
        fail(f"{path} has invalid publication_state")

    fixtures = payload.get("fixtures")
    if not isinstance(fixtures, list) or not fixtures:
        fail(f"{path} must contain a non-empty fixtures list")

    seen_ids: set[str] = set()
    for index, fixture in enumerate(fixtures):
        if not isinstance(fixture, dict):
            fail(f"{path} fixture {index} is not an object")
        fixture_id = fixture.get("fixture_id", f"<fixture-{index}>")
        missing = REQUIRED_FIXTURE_FIELDS - set(fixture)
        if missing:
            fail(f"{path} {fixture_id} missing required fields: {sorted(missing)}")
        if fixture_id in seen_ids:
            fail(f"{path} duplicate fixture_id {fixture_id}")
        seen_ids.add(fixture_id)

        observable_id = fixture["observable_id"]
        if observable_id not in known_ids:
            fail(f"{path} {fixture_id} references unknown observable_id {observable_id}")
        if fixture["fixture_kind"] not in VALID_FIXTURE_KINDS:
            fail(f"{path} {fixture_id} has invalid fixture_kind {fixture['fixture_kind']!r}")
        if fixture["expected_result"] not in VALID_EXPECTED_RESULTS:
            fail(f"{path} {fixture_id} has invalid expected_result {fixture['expected_result']!r}")
        if fixture["public_state"] not in VALID_PUBLIC_STATES:
            fail(f"{path} {fixture_id} has invalid public_state {fixture['public_state']!r}")
        if not isinstance(fixture["non_claims"], list) or not fixture["non_claims"]:
            fail(f"{path} {fixture_id} must list non_claims")
        for field in ["condition", "detection_mechanism", "revision_direction", "owner"]:
            if not isinstance(fixture[field], str) or not fixture[field].strip():
                fail(f"{path} {fixture_id} field {field} must be a non-empty string")

    return len(fixtures)


def main() -> int:
    known_ids = known_observable_ids()
    if not known_ids:
        fail("observable registry is empty")
    if not FIXTURE_DIR.exists():
        fail(f"fixture directory does not exist: {FIXTURE_DIR}")

    fixture_files = sorted(FIXTURE_DIR.glob("*.json"))
    if not fixture_files:
        fail(f"no JSON fixture files found under {FIXTURE_DIR}")

    count = 0
    for path in fixture_files:
        count += validate_fixture_file(path, known_ids)

    print(f"PASS: validated {count} falsification fixtures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
