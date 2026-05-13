#!/usr/bin/env python3
"""Validate ProCybernetica lawful metadata harvest envelopes.

This validator deliberately checks more than JSON shape. It enforces the first
cross-field governance invariants for resumable metadata harvesting:

- policy decision is required;
- batch receipts form a hash-linked chain;
- resumption-token handoff is consistent across batches;
- token loops must be explicitly represented as anomalies;
- completed OAI-PMH ListRecords runs must terminate with an empty token state;
- promotion requires validation and policy references.

By default it validates all fixtures under examples/harvest. Files ending in
.valid.json must pass. Files ending in .invalid.json must fail.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FIXTURE_DIR = ROOT / "examples" / "harvest"
SHA256_RE = re.compile(r"^sha256:[a-fA-F0-9]{64}$")

REQUIRED_TOP_LEVEL = {
    "schema_version",
    "protocol",
    "harvest_plan",
    "policy_decision_ref",
    "run",
    "batch_receipts",
    "terminal_state",
    "validation_report_ref",
    "promotion_decisions",
}

ALLOWED_ANOMALIES = {
    "bad_resumption_token",
    "expired_resumption_token",
    "resumption_token_loop",
    "missing_final_empty_token",
    "unexpected_empty_batch",
    "record_count_regression",
    "response_hash_mismatch_on_replay",
    "endpoint_identity_changed",
    "metadata_prefix_changed",
    "deleted_record_without_policy",
    "overscope_attempt",
    "unbounded_harvest_blocked",
    "rate_limit_or_throttle_detected",
    "non_monotone_datestamp_observed",
    "cursor_semantics_overassumed",
    "suspicious_tokenized_pagination_pattern",
}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError("document root must be a JSON object")
    return data


def is_nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def is_sha256(value: Any) -> bool:
    return isinstance(value, str) and bool(SHA256_RE.match(value))


def anomaly_codes(envelope: dict[str, Any]) -> set[str]:
    anomalies = envelope.get("anomalies", []) or []
    codes: set[str] = set()
    if not isinstance(anomalies, list):
        return codes
    for anomaly in anomalies:
        if isinstance(anomaly, dict) and isinstance(anomaly.get("code"), str):
            codes.add(anomaly["code"])
    return codes


def require(condition: bool, errors: list[str], message: str) -> None:
    if not condition:
        errors.append(message)


def validate_envelope(envelope: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    missing = sorted(REQUIRED_TOP_LEVEL.difference(envelope))
    require(not missing, errors, f"missing required top-level fields: {', '.join(missing)}")
    if missing:
        return errors

    require(envelope.get("schema_version") == "procybernetica.harvest.v0", errors, "schema_version must be procybernetica.harvest.v0")
    require(envelope.get("protocol") in {"OAI-PMH", "generic_metadata_harvest"}, errors, "protocol must be recognized")
    require(is_nonempty_string(envelope.get("policy_decision_ref")), errors, "policy_decision_ref must be non-empty")
    require(is_nonempty_string(envelope.get("validation_report_ref")), errors, "validation_report_ref must be non-empty")

    plan = envelope.get("harvest_plan")
    require(isinstance(plan, dict), errors, "harvest_plan must be an object")
    if isinstance(plan, dict):
        for field in ["plan_id", "endpoint_id", "endpoint_url_hash", "verb", "privacy_class", "retention_class"]:
            require(field in plan, errors, f"harvest_plan.{field} is required")
        require(is_sha256(plan.get("endpoint_url_hash")), errors, "harvest_plan.endpoint_url_hash must be sha256:<64 hex>")
        require(isinstance(plan.get("max_batches"), int) and plan.get("max_batches") >= 1, errors, "harvest_plan.max_batches must be a positive integer")
        require(isinstance(plan.get("max_records"), int) and plan.get("max_records") >= 1, errors, "harvest_plan.max_records must be a positive integer")

    run = envelope.get("run")
    require(isinstance(run, dict), errors, "run must be an object")
    if isinstance(run, dict):
        for field in ["run_id", "actor_id", "trace_id", "root_event_id", "execution_authority", "status"]:
            require(is_nonempty_string(run.get(field)), errors, f"run.{field} must be non-empty")

    batches = envelope.get("batch_receipts")
    require(isinstance(batches, list) and len(batches) > 0, errors, "batch_receipts must be a non-empty array")
    if not isinstance(batches, list) or not batches:
        return errors

    seen_next_tokens: set[str] = set()
    last_receipt_hash: str | None = None
    last_next_token_hash: str | None = None
    total_records = 0
    codes = anomaly_codes(envelope)

    unknown_anomalies = codes.difference(ALLOWED_ANOMALIES)
    require(not unknown_anomalies, errors, f"unknown anomaly code(s): {', '.join(sorted(unknown_anomalies))}")

    for index, batch in enumerate(batches):
        require(isinstance(batch, dict), errors, f"batch_receipts[{index}] must be an object")
        if not isinstance(batch, dict):
            continue

        for field in ["batch_id", "event_class", "request_hash", "response_hash", "record_count", "previous_receipt_hash", "receipt_hash", "observed_at", "classification", "handling_tags"]:
            require(field in batch, errors, f"batch_receipts[{index}].{field} is required")

        require(batch.get("event_class") == "harvest.batch.sealed", errors, f"batch_receipts[{index}].event_class must be harvest.batch.sealed")
        require(is_sha256(batch.get("request_hash")), errors, f"batch_receipts[{index}].request_hash must be sha256:<64 hex>")
        require(is_sha256(batch.get("response_hash")), errors, f"batch_receipts[{index}].response_hash must be sha256:<64 hex>")
        require(is_sha256(batch.get("receipt_hash")), errors, f"batch_receipts[{index}].receipt_hash must be sha256:<64 hex>")
        require(isinstance(batch.get("record_count"), int) and batch.get("record_count") >= 0, errors, f"batch_receipts[{index}].record_count must be a non-negative integer")
        total_records += batch.get("record_count", 0) if isinstance(batch.get("record_count"), int) else 0

        previous_receipt_hash = batch.get("previous_receipt_hash")
        if index == 0:
            require(previous_receipt_hash is None, errors, "first batch previous_receipt_hash must be null")
            require(batch.get("previous_resumption_token_hash") is None, errors, "first batch previous_resumption_token_hash must be null")
        else:
            require(previous_receipt_hash == last_receipt_hash, errors, f"batch_receipts[{index}].previous_receipt_hash must equal previous receipt_hash")
            require(batch.get("previous_resumption_token_hash") == last_next_token_hash, errors, f"batch_receipts[{index}].previous_resumption_token_hash must equal previous next_resumption_token_hash")

        next_token = batch.get("next_resumption_token_hash")
        previous_token = batch.get("previous_resumption_token_hash")
        if next_token is not None:
            require(is_sha256(next_token), errors, f"batch_receipts[{index}].next_resumption_token_hash must be sha256:<64 hex> or null")
            if next_token in seen_next_tokens or next_token == previous_token:
                require("resumption_token_loop" in codes, errors, "repeated or self-referential resumption token requires resumption_token_loop anomaly")
            seen_next_tokens.add(next_token)
        if previous_token is not None:
            require(is_sha256(previous_token), errors, f"batch_receipts[{index}].previous_resumption_token_hash must be sha256:<64 hex> or null")

        last_receipt_hash = batch.get("receipt_hash") if isinstance(batch.get("receipt_hash"), str) else None
        last_next_token_hash = next_token if isinstance(next_token, str) else None

    terminal = envelope.get("terminal_state")
    require(isinstance(terminal, dict), errors, "terminal_state must be an object")
    if isinstance(terminal, dict):
        require(terminal.get("total_batches") == len(batches), errors, "terminal_state.total_batches must equal number of batch receipts")
        require(terminal.get("total_records") == total_records, errors, "terminal_state.total_records must equal sum of batch record_count values")
        require(terminal.get("ledger_root_hash") == last_receipt_hash, errors, "terminal_state.ledger_root_hash must equal last receipt_hash")
        if envelope.get("protocol") == "OAI-PMH" and isinstance(plan, dict) and plan.get("verb") in {"ListRecords", "ListIdentifiers", "ListSets"}:
            if terminal.get("completed") is True:
                require(terminal.get("final_resumption_token_state") == "empty", errors, "completed OAI-PMH incomplete-list run must end with final_resumption_token_state=empty")

    promotions = envelope.get("promotion_decisions")
    require(isinstance(promotions, list), errors, "promotion_decisions must be an array")
    if isinstance(promotions, list):
        for index, decision in enumerate(promotions):
            require(isinstance(decision, dict), errors, f"promotion_decisions[{index}] must be an object")
            if not isinstance(decision, dict):
                continue
            if decision.get("outcome") == "promoted":
                require(is_nonempty_string(decision.get("policy_decision_ref")), errors, f"promotion_decisions[{index}].policy_decision_ref must be non-empty for promoted records")
                require(is_nonempty_string(decision.get("validation_report_ref")), errors, f"promotion_decisions[{index}].validation_report_ref must be non-empty for promoted records")
                require(isinstance(decision.get("record_refs"), list) and len(decision.get("record_refs")) > 0, errors, f"promotion_decisions[{index}].record_refs must be non-empty for promoted records")

    return errors


def validate_fixture(path: Path) -> tuple[bool, list[str]]:
    try:
        envelope = load_json(path)
    except Exception as exc:  # noqa: BLE001 - CLI diagnostic path
        return False, [f"failed to load JSON: {exc}"]
    errors = validate_envelope(envelope)
    return not errors, errors


def fixture_paths(args: argparse.Namespace) -> list[Path]:
    if args.files:
        return [Path(file_name) for file_name in args.files]
    return sorted(DEFAULT_FIXTURE_DIR.glob("*.json"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", help="Specific harvest envelope JSON files to validate")
    parser.add_argument("--no-name-expectations", action="store_true", help="Do not require .valid.json files to pass and .invalid.json files to fail")
    args = parser.parse_args(argv)

    paths = fixture_paths(args)
    if not paths:
        print("no harvest fixtures found", file=sys.stderr)
        return 1

    failures = 0
    for path in paths:
        ok, errors = validate_fixture(path)
        expected_ok = None
        if not args.no_name_expectations:
            if path.name.endswith(".valid.json"):
                expected_ok = True
            elif path.name.endswith(".invalid.json"):
                expected_ok = False

        if expected_ok is not None and ok != expected_ok:
            failures += 1
            expectation = "pass" if expected_ok else "fail"
            print(f"FAIL {path}: expected to {expectation}, got {'pass' if ok else 'fail'}")
            for error in errors:
                print(f"  - {error}")
            if expected_ok is False and ok is True:
                print("  - invalid fixture passed unexpectedly")
            continue

        print(f"{'PASS' if ok else 'FAIL'} {path}")
        for error in errors:
            print(f"  - {error}")
        if expected_ok is None and not ok:
            failures += 1

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
