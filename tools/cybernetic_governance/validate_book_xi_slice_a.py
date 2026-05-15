#!/usr/bin/env python3
"""Validate Book XI Slice A: ingest to canonical claims.

This validator is repository-local and public-synthetic. It validates one
artifact/provenance/claim/event fixture against the v0 schemas and checks the
Book XI practicum invariants that JSON Schema alone cannot express.

It does not implement an agent runtime, database, object store, index, graph
store, query runtime, planner, replay service, or mesh coordination runtime.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_DIR = ROOT / "schemas"
DEFAULT_FIXTURE = ROOT / "tests" / "fixtures" / "book-xi" / "slice-a-ingest-to-claims.synthetic.json"

SCHEMA_MAP = {
    "artifact_envelopes": "artifact_envelope.schema.json",
    "provenance_records": "provenance_record.schema.json",
    "claims": "claim.schema.json",
    "event_envelopes": "event_envelope.schema.json",
}


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"missing file: {path}") from None
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid JSON in {path}: {exc}") from None


def load_schema(name: str) -> dict[str, Any]:
    schema = load_json(SCHEMA_DIR / name)
    Draft202012Validator.check_schema(schema)
    return schema


def validate_objects(fixture: dict[str, Any]) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for collection_name, schema_name in SCHEMA_MAP.items():
        schema = load_schema(schema_name)
        validator = Draft202012Validator(schema)
        for index, obj in enumerate(fixture.get(collection_name, [])):
            errors = [error.message for error in sorted(validator.iter_errors(obj), key=str)]
            object_id = (
                obj.get("artifact_id")
                or obj.get("provenance_id")
                or obj.get("claim_id")
                or obj.get("event_id")
                or f"{collection_name}:{index}"
            )
            results.append(
                {
                    "check_id": f"schema:{collection_name}:{object_id}",
                    "object_id": object_id,
                    "schema": schema_name,
                    "passed": not errors,
                    "diagnostics": errors,
                }
            )
    return results


def require(condition: bool, check_id: str, diagnostics: list[str]) -> dict[str, Any]:
    return {
        "check_id": check_id,
        "passed": condition,
        "diagnostics": [] if condition else diagnostics,
    }


def validate_book_xi_invariants(fixture: dict[str, Any]) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    artifacts = {artifact["artifact_id"]: artifact for artifact in fixture.get("artifact_envelopes", [])}
    provenance = {record["provenance_id"]: record for record in fixture.get("provenance_records", [])}
    claims = {claim["claim_id"]: claim for claim in fixture.get("claims", [])}
    events = {event["event_id"]: event for event in fixture.get("event_envelopes", [])}

    results.append(require(len(artifacts) >= 1, "slice-a-has-artifact", ["Slice A must include at least one artifact envelope."]))
    results.append(require(len(provenance) >= 1, "slice-a-has-provenance", ["Slice A must include at least one provenance record."]))
    results.append(require(len(claims) >= 2, "slice-a-has-candidate-and-validated-claims", ["Slice A must include candidate and validated claims."]))
    results.append(require(len(events) >= 1, "slice-a-has-event", ["Slice A must include at least one event envelope."]))

    for claim_id, claim in claims.items():
        results.append(
            require(
                bool(claim.get("provenance_refs")),
                f"claim-has-provenance:{claim_id}",
                [f"Claim {claim_id} must cite provenance_refs."],
            )
        )
        results.append(
            require(
                bool(claim.get("schema_ref")) and bool(claim.get("ontology_ref")),
                f"claim-has-schema-and-ontology:{claim_id}",
                [f"Claim {claim_id} must declare schema_ref and ontology_ref."],
            )
        )
        missing_refs = [ref for ref in claim.get("provenance_refs", []) if ref not in provenance]
        results.append(
            require(
                not missing_refs,
                f"claim-provenance-resolves:{claim_id}",
                [f"Claim {claim_id} has unresolved provenance refs: {missing_refs}"],
            )
        )

    candidate_claims = [claim for claim in claims.values() if claim.get("status") in {"candidate", "hypothesis"}]
    validated_claims = [claim for claim in claims.values() if claim.get("status") == "validated"]

    results.append(
        require(
            bool(candidate_claims),
            "heuristic-output-enters-soft-lane",
            ["At least one claim must enter as candidate or hypothesis before validation."],
        )
    )
    results.append(
        require(
            bool(validated_claims),
            "validated-claim-present",
            ["Slice A must include at least one validated claim."],
        )
    )

    candidate_ids = {claim["claim_id"] for claim in candidate_claims}
    for claim in validated_claims:
        derived = set(claim.get("derived_from", []))
        results.append(
            require(
                bool(derived & candidate_ids),
                f"validated-claim-derived-from-candidate:{claim['claim_id']}",
                [f"Validated claim {claim['claim_id']} must derive from a candidate claim."],
            )
        )

    artifact_ids = set(artifacts)
    provenance_ids = set(provenance)
    for event_id, event in events.items():
        event_artifact_refs = set(event.get("artifact_refs", []))
        event_provenance_refs = set(event.get("provenance_refs", []))
        results.append(
            require(
                bool(event_artifact_refs & artifact_ids),
                f"event-cites-artifact:{event_id}",
                [f"Event {event_id} must cite at least one artifact_ref."],
            )
        )
        results.append(
            require(
                bool(event_provenance_refs & provenance_ids),
                f"event-cites-provenance:{event_id}",
                [f"Event {event_id} must cite at least one provenance_ref."],
            )
        )
        payload = event.get("payload", {})
        emitted_claim_refs = set(payload.get("candidate_claim_refs", [])) | set(payload.get("validated_claim_refs", []))
        results.append(
            require(
                bool(emitted_claim_refs & set(claims)),
                f"event-cites-claims:{event_id}",
                [f"Event {event_id} must cite candidate or validated claim refs in payload."],
            )
        )

    release_states = {artifact.get("public_release_state") for artifact in artifacts.values()} | {event.get("public_release_state") for event in events.values()}
    results.append(
        require(
            release_states <= {"public-synthetic"},
            "slice-a-public-synthetic-only",
            [f"Slice A fixtures must remain public-synthetic only; observed {sorted(release_states)}"],
        )
    )
    results.append(
        require(
            bool(fixture.get("non_claims")),
            "slice-a-non-claims-present",
            ["Slice A fixture must include non_claims."],
        )
    )

    return results


def validate_path(path: Path) -> dict[str, Any]:
    fixture = load_json(path)
    schema_results = validate_objects(fixture)
    invariant_results = validate_book_xi_invariants(fixture)
    results = schema_results + invariant_results
    return {
        "validator": "book_xi_slice_a.validator.v1",
        "fixture_file": str(path.relative_to(ROOT)),
        "passed": all(result["passed"] for result in results),
        "artifact_count": len(fixture.get("artifact_envelopes", [])),
        "provenance_count": len(fixture.get("provenance_records", [])),
        "claim_count": len(fixture.get("claims", [])),
        "event_count": len(fixture.get("event_envelopes", [])),
        "results": results,
        "non_claims": fixture.get("non_claims", []),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", nargs="?", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    result = validate_path(args.fixture)
    print(json.dumps(result, indent=2, sort_keys=True))
    if not args.json:
        if result["passed"]:
            print("PASS: Book XI Slice A fixture")
        else:
            print("FAIL: Book XI Slice A fixture", file=sys.stderr)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
