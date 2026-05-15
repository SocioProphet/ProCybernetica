#!/usr/bin/env python3
"""Validate falsification observable coverage registries.

This validator intentionally checks repository-local public artifacts only. It does
not claim runtime telemetry or production monitoring coverage.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DOCTRINE_PATH = ROOT / "docs" / "falsification" / "unified-falsification-v1.0.md"
CROSS_REF_PATH = ROOT / "docs" / "falsification" / "observable-cross-reference.md"
OWNERS_PATH = ROOT / "docs" / "falsification" / "observable-owners.md"
FIXTURE_DIR = ROOT / "tests" / "fixtures" / "falsification"

REQUIRED_OBSERVABLE_FIELDS = {
    "id",
    "layer",
    "severity",
    "condition",
    "detection_mechanism",
    "revision_direction",
    "owner",
    "evidence_class",
    "fixture_status",
    "ci_invariants",
}

VALID_FIXTURE_STATUSES = {
    "fixture_required",
    "fixture_present",
    "deferred_until_schema",
    "runtime_monitoring",
    "periodic_audit",
    "no_fixture_required",
}

RUNTIME_EVIDENCE_MARKERS = {"runtime-telemetry"}
RUNTIME_FIXTURE_STATUSES = {"runtime_monitoring"}
FIXTURE_BACKED_STATUSES = {"fixture_required", "fixture_present"}


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


def doctrine_observable_ids(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    return set(re.findall(r"\|\s*((?:F\d+\.\d+)|(?:B\d+))\s*\|", text))


def fixture_observable_ids(fixture_dir: Path) -> set[str]:
    ids: set[str] = set()
    if not fixture_dir.exists():
        return ids
    for path in sorted(fixture_dir.glob("*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        records = payload.get("fixtures", [])
        if not isinstance(records, list):
            fail(f"{path} has non-list fixtures")
        for record in records:
            if isinstance(record, dict) and isinstance(record.get("observable_id"), str):
                ids.add(record["observable_id"])
    return ids


def main() -> int:
    doctrine_ids = doctrine_observable_ids(DOCTRINE_PATH)
    if not doctrine_ids:
        fail(f"no observables found in {DOCTRINE_PATH}")

    cross_ref = extract_json_block(CROSS_REF_PATH)
    owners_registry = extract_json_block(OWNERS_PATH)

    owners = owners_registry.get("owners", [])
    if not isinstance(owners, list) or not owners:
        fail("owners registry must define a non-empty owners list")
    owner_ids = {owner.get("owner_id") for owner in owners if isinstance(owner, dict)}

    observables = cross_ref.get("observables", [])
    if not isinstance(observables, list) or not observables:
        fail("cross-reference must define a non-empty observables list")

    registry_ids = {obs.get("id") for obs in observables if isinstance(obs, dict)}
    missing = doctrine_ids - registry_ids
    extra = registry_ids - doctrine_ids
    if missing:
        fail(f"cross-reference missing doctrine observables: {sorted(missing)}")
    if extra:
        fail(f"cross-reference has observables not in doctrine: {sorted(extra)}")

    expected_layers = set(cross_ref.get("expected_architectural_layers", []))
    expected_invariants = set(cross_ref.get("expected_ci_invariants", []))
    seen_layers: set[str] = set()
    seen_invariants: set[str] = set()

    backed_fixture_ids = fixture_observable_ids(FIXTURE_DIR)

    for obs in observables:
        if not isinstance(obs, dict):
            fail("every observable must be an object")
        obs_id = obs.get("id", "<missing>")
        missing_fields = REQUIRED_OBSERVABLE_FIELDS - set(obs)
        if missing_fields:
            fail(f"{obs_id} missing required fields: {sorted(missing_fields)}")

        if obs["owner"] not in owner_ids:
            fail(f"{obs_id} owner {obs['owner']!r} is not in owner registry")

        if obs["layer"] not in expected_layers:
            fail(f"{obs_id} layer {obs['layer']!r} is not declared in expected_architectural_layers")
        seen_layers.add(obs["layer"])

        if obs["fixture_status"] not in VALID_FIXTURE_STATUSES:
            fail(f"{obs_id} has invalid fixture_status {obs['fixture_status']!r}")

        invariants = obs["ci_invariants"]
        if not isinstance(invariants, list) or not invariants:
            fail(f"{obs_id} must list at least one ci_invariant")
        unknown_invariants = set(invariants) - expected_invariants
        if unknown_invariants:
            fail(f"{obs_id} references unknown ci_invariants: {sorted(unknown_invariants)}")
        seen_invariants.update(invariants)

        evidence_class = str(obs["evidence_class"])
        has_runtime_evidence = any(marker in evidence_class for marker in RUNTIME_EVIDENCE_MARKERS)
        if has_runtime_evidence and obs["fixture_status"] not in RUNTIME_FIXTURE_STATUSES | FIXTURE_BACKED_STATUSES:
            fail(f"{obs_id} has runtime evidence but is not marked runtime_monitoring or fixture-backed")

        if obs["fixture_status"] in FIXTURE_BACKED_STATUSES and obs_id not in backed_fixture_ids:
            fail(f"{obs_id} is fixture-backed but has no fixture under {FIXTURE_DIR}")

    missing_layers = expected_layers - seen_layers
    if missing_layers:
        fail(f"expected architectural layers have no observable: {sorted(missing_layers)}")

    missing_invariants = expected_invariants - seen_invariants
    if missing_invariants:
        fail(f"expected CI invariants have no observable: {sorted(missing_invariants)}")

    print(f"PASS: falsification coverage registry validates {len(observables)} observables")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
