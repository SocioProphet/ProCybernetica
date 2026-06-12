"""Tests for the enrichment path/content conflict classifier.

Verifies that the content-addressing primitive correctly distinguishes
file moves from content changes, as required by enrichment-twin-mission-spec.md §6.

Test corpus covers all six conflict_kind values and validates the core invariant:
re-enrichment is triggered by asset_hash change, never by path change alone.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

from procyber.enrichment_path_content_conflict import (
    AssetObservation,
    PathContentConflict,
    classify,
)

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_FILE = ROOT / "schemas" / "enrichment_path_content_conflict.schema.json"

HASH_A = "a" * 64
HASH_B = "b" * 64


def obs(path: str, h: str) -> AssetObservation:
    return AssetObservation(path=path, asset_hash=h)


# ── Schema loading ──────────────────────────────────────────────────────────

@pytest.fixture(scope="module")
def pcc_schema() -> dict:
    schema = json.loads(SCHEMA_FILE.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return schema


def make_record(before: AssetObservation | None, after: AssetObservation | None, result: PathContentConflict) -> dict:
    """Build a JSON-serialisable decision record for schema validation."""
    def obs_dict(o: AssetObservation | None) -> dict | None:
        if o is None:
            return None
        return {"path": o.path, "asset_hash": o.asset_hash}

    return {
        "schema_version": "v0.1",
        "decision_id": f"pcc:{result.conflict_kind.replace('_', '-')}-test",
        "before": obs_dict(before),
        "after": obs_dict(after),
        "conflict_kind": result.conflict_kind,
        "re_enrich_required": result.re_enrich_required,
        "cache_key_changed": result.cache_key_changed,
        "rationale": result.rationale,
    }


# ── Conflict classification tests ───────────────────────────────────────────

class TestNoChange:
    def test_same_path_same_hash(self) -> None:
        result = classify(obs("/photos/a.jpg", HASH_A), obs("/photos/a.jpg", HASH_A))
        assert result.conflict_kind == "no_change"
        assert result.re_enrich_required is False
        assert result.cache_key_changed is False

    def test_schema_valid(self, pcc_schema) -> None:
        result = classify(obs("/photos/a.jpg", HASH_A), obs("/photos/a.jpg", HASH_A))
        record = make_record(obs("/photos/a.jpg", HASH_A), obs("/photos/a.jpg", HASH_A), result)
        errors = list(Draft202012Validator(pcc_schema).iter_errors(record))
        assert errors == [], [e.message for e in errors]


class TestPathMovedContentSame:
    """Core invariant: move ≠ re-enrich."""

    def test_move_does_not_trigger_re_enrichment(self) -> None:
        result = classify(
            obs("/photos/vacation/beach.jpg", HASH_A),
            obs("/photos/archive/2024/beach.jpg", HASH_A),
        )
        assert result.conflict_kind == "path_moved_content_same"
        assert result.re_enrich_required is False
        assert result.cache_key_changed is False

    def test_deep_rename_chain(self) -> None:
        result = classify(obs("/a/b/c/d.jpg", HASH_A), obs("/x/y/z/d.jpg", HASH_A))
        assert result.conflict_kind == "path_moved_content_same"
        assert result.re_enrich_required is False

    def test_schema_valid(self, pcc_schema) -> None:
        before = obs("/photos/old.jpg", HASH_A)
        after = obs("/photos/new.jpg", HASH_A)
        result = classify(before, after)
        record = make_record(before, after, result)
        errors = list(Draft202012Validator(pcc_schema).iter_errors(record))
        assert errors == [], [e.message for e in errors]


class TestPathSameContentChanged:
    """In-place edit triggers re-enrichment."""

    def test_content_change_at_same_path(self) -> None:
        result = classify(obs("/docs/report.pdf", HASH_A), obs("/docs/report.pdf", HASH_B))
        assert result.conflict_kind == "path_same_content_changed"
        assert result.re_enrich_required is True
        assert result.cache_key_changed is True

    def test_schema_valid(self, pcc_schema) -> None:
        before = obs("/docs/report.pdf", HASH_A)
        after = obs("/docs/report.pdf", HASH_B)
        result = classify(before, after)
        record = make_record(before, after, result)
        errors = list(Draft202012Validator(pcc_schema).iter_errors(record))
        assert errors == [], [e.message for e in errors]


class TestPathMovedContentChanged:
    """Move + edit: re-enrich on content change."""

    def test_move_and_edit(self) -> None:
        result = classify(obs("/drafts/memo.docx", HASH_A), obs("/final/memo-v2.docx", HASH_B))
        assert result.conflict_kind == "path_moved_content_changed"
        assert result.re_enrich_required is True
        assert result.cache_key_changed is True

    def test_schema_valid(self, pcc_schema) -> None:
        before = obs("/drafts/memo.docx", HASH_A)
        after = obs("/final/memo-v2.docx", HASH_B)
        result = classify(before, after)
        record = make_record(before, after, result)
        errors = list(Draft202012Validator(pcc_schema).iter_errors(record))
        assert errors == [], [e.message for e in errors]


class TestAssetAdded:
    def test_new_asset(self) -> None:
        result = classify(None, obs("/photos/new.jpg", HASH_A))
        assert result.conflict_kind == "asset_added"
        assert result.re_enrich_required is True
        assert result.cache_key_changed is True

    def test_schema_valid(self, pcc_schema) -> None:
        after = obs("/photos/new.jpg", HASH_A)
        result = classify(None, after)
        record = make_record(None, after, result)
        errors = list(Draft202012Validator(pcc_schema).iter_errors(record))
        assert errors == [], [e.message for e in errors]


class TestAssetRemoved:
    def test_deleted_asset(self) -> None:
        result = classify(obs("/photos/old.jpg", HASH_A), None)
        assert result.conflict_kind == "asset_removed"
        assert result.re_enrich_required is False
        assert result.cache_key_changed is True

    def test_schema_valid(self, pcc_schema) -> None:
        before = obs("/photos/old.jpg", HASH_A)
        result = classify(before, None)
        record = make_record(before, None, result)
        errors = list(Draft202012Validator(pcc_schema).iter_errors(record))
        assert errors == [], [e.message for e in errors]


class TestErrorCases:
    def test_both_none_raises(self) -> None:
        with pytest.raises(ValueError, match="cannot both be None"):
            classify(None, None)


# ── Core invariant: path change alone never triggers re-enrichment ──────────

class TestCoreInvariant:
    """The deliberate inversion of path-based cache invalidation.

    Across all valid (before, after) pairs where the asset_hash is unchanged,
    re_enrich_required must be False regardless of path change.
    """

    PATHS = [
        ("/a.jpg", "/a.jpg"),
        ("/a.jpg", "/b/a.jpg"),
        ("/old/deep/path/file.png", "/new/location/file.png"),
        ("/同じファイル.jpg", "/moved/同じファイル.jpg"),
    ]

    @pytest.mark.parametrize("before_path,after_path", PATHS)
    def test_same_hash_never_re_enriches(self, before_path: str, after_path: str) -> None:
        result = classify(obs(before_path, HASH_A), obs(after_path, HASH_A))
        assert result.re_enrich_required is False, (
            f"re_enrich_required must be False when hash is unchanged "
            f"('{before_path}' → '{after_path}')"
        )

    def test_content_change_always_re_enriches(self) -> None:
        """Any hash change must trigger re-enrichment, even same path."""
        result = classify(obs("/photos/a.jpg", HASH_A), obs("/photos/a.jpg", HASH_B))
        assert result.re_enrich_required is True


# ── Real SHA-256 hashes ──────────────────────────────────────────────────────

class TestRealHashes:
    """Classifier works correctly with real SHA-256 content hashes."""

    @staticmethod
    def sha256(content: bytes) -> str:
        return hashlib.sha256(content).hexdigest()

    def test_identical_content_different_path(self) -> None:
        h = self.sha256(b"photo content bytes")
        result = classify(obs("/2023/img001.jpg", h), obs("/archive/img001.jpg", h))
        assert result.conflict_kind == "path_moved_content_same"
        assert result.re_enrich_required is False

    def test_edited_file(self) -> None:
        h_before = self.sha256(b"original content")
        h_after = self.sha256(b"edited content")
        result = classify(obs("/doc.pdf", h_before), obs("/doc.pdf", h_after))
        assert result.conflict_kind == "path_same_content_changed"
        assert result.re_enrich_required is True
