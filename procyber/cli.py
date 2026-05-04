from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from .schema_bundle import SchemaBundle
from .validate import load_json

ROOT = Path(__file__).resolve().parents[1]

PRACTICUM_CASES: list[tuple[str, Path]] = [
    ("node_descriptor", ROOT / "examples/practicum/node_descriptor.example.json"),
    ("policy_envelope", ROOT / "examples/practicum/policy_envelope.example.json"),
    ("transition_record", ROOT / "examples/practicum/transition_record.example.json"),
    ("artifact_envelope", ROOT / "examples/practicum/artifact_envelope.example.json"),
    ("claim", ROOT / "examples/practicum/claim.example.json"),
    ("provenance_record", ROOT / "examples/practicum/provenance_record.example.json"),
    ("event_envelope", ROOT / "examples/practicum/event_envelope.example.json"),
    ("trace_event", ROOT / "examples/practicum/trace_event.example.json"),
    ("command_envelope", ROOT / "examples/practicum/command_envelope.example.json"),
    ("delegation_envelope", ROOT / "examples/practicum/delegation_envelope.example.json"),
    ("status_envelope", ROOT / "examples/practicum/status_envelope.example.json"),
    ("capability_descriptor", ROOT / "examples/practicum/capability_descriptor.example.json"),
    ("replay_envelope", ROOT / "examples/practicum/replay_envelope.example.json"),
    ("evaluation_result", ROOT / "examples/practicum/evaluation_result.example.json"),
    ("promotion_decision", ROOT / "examples/practicum/promotion_decision.example.json"),
]


def validate_file(schema_name: str, file_path: Path) -> dict[str, object]:
    bundle = SchemaBundle(ROOT / "schemas")
    bundle.validate(schema_name, load_json(file_path))
    return {
        "schema": schema_name,
        "path": str(file_path.relative_to(ROOT)),
        "valid": True,
    }


def practicum_report(output: Path | None = None) -> dict[str, object]:
    results = [validate_file(schema, path) for schema, path in PRACTICUM_CASES]
    report: dict[str, object] = {
        "schema_version": "0.1.0",
        "report_type": "public-practicum-validation-report",
        "fixture_type": "public-synthetic",
        "valid": all(item["valid"] for item in results),
        "validated_count": len(results),
        "results": results,
    }
    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="ProCybernetica public reference CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    validate = sub.add_parser("validate", help="Validate a JSON file against a named schema")
    validate.add_argument("schema", help="Schema name from procyber.schema_bundle.SCHEMA_MAP")
    validate.add_argument("path", type=Path, help="Path to JSON payload")

    report = sub.add_parser("practicum-report", help="Validate public practicum fixtures and emit a report")
    report.add_argument("--output", type=Path, default=None, help="Optional path to write JSON report")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "validate":
        result = validate_file(args.schema, args.path)
        print(json.dumps(result, indent=2))
        return 0

    if args.command == "practicum-report":
        report = practicum_report(args.output)
        print(json.dumps(report, indent=2))
        return 0

    parser.error(f"unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
