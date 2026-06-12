"""Content-addressing primitive for the Enrichment Twin cache.

Classifies filesystem observation changes as one of six conflict kinds and
determines whether re-enrichment is required. The cache key is the asset
content hash, not the path — a file move never triggers re-enrichment.

See: enrichment-twin-mission-spec.md §6
Schema: schemas/enrichment_path_content_conflict.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class AssetObservation:
    """Snapshot of a single asset at a point in time."""
    path: str
    asset_hash: str  # SHA-256 hex, 64 chars


@dataclass(frozen=True)
class PathContentConflict:
    """Result of classifying a before/after observation pair."""
    conflict_kind: str
    re_enrich_required: bool
    cache_key_changed: bool
    rationale: str


_NO_CHANGE = "no_change"
_PATH_MOVED_CONTENT_SAME = "path_moved_content_same"
_PATH_SAME_CONTENT_CHANGED = "path_same_content_changed"
_PATH_MOVED_CONTENT_CHANGED = "path_moved_content_changed"
_ASSET_ADDED = "asset_added"
_ASSET_REMOVED = "asset_removed"


def classify(
    before: Optional[AssetObservation],
    after: Optional[AssetObservation],
) -> PathContentConflict:
    """Classify a before/after observation pair.

    Rules (governance precedes heuristics):
      - Cache key = asset_hash. Path is informational only.
      - Re-enrichment fires iff asset_hash changes or asset is added.
      - Path change alone (move) never triggers re-enrichment.
    """
    if before is None and after is None:
        raise ValueError("before and after cannot both be None")

    if before is None:
        return PathContentConflict(
            conflict_kind=_ASSET_ADDED,
            re_enrich_required=True,
            cache_key_changed=True,
            rationale="Asset is new — no prior enrichment exists for this hash.",
        )

    if after is None:
        return PathContentConflict(
            conflict_kind=_ASSET_REMOVED,
            re_enrich_required=False,
            cache_key_changed=True,
            rationale=(
                "Asset removed — existing cache entry is now orphaned. "
                "No re-enrichment required; cache entry may be evicted."
            ),
        )

    same_path = before.path == after.path
    same_hash = before.asset_hash == after.asset_hash

    if same_path and same_hash:
        return PathContentConflict(
            conflict_kind=_NO_CHANGE,
            re_enrich_required=False,
            cache_key_changed=False,
            rationale="Path and content are identical — no action required.",
        )

    if not same_path and same_hash:
        return PathContentConflict(
            conflict_kind=_PATH_MOVED_CONTENT_SAME,
            re_enrich_required=False,
            cache_key_changed=False,
            rationale=(
                f"File moved from '{before.path}' to '{after.path}' but content "
                "is unchanged (same asset_hash). Cache key is unchanged — "
                "no re-enrichment required. This is the deliberate inversion of "
                "path-based cache invalidation."
            ),
        )

    if same_path and not same_hash:
        return PathContentConflict(
            conflict_kind=_PATH_SAME_CONTENT_CHANGED,
            re_enrich_required=True,
            cache_key_changed=True,
            rationale=(
                f"Content changed at '{before.path}' "
                f"({before.asset_hash[:12]}… → {after.asset_hash[:12]}…). "
                "Cache key changed — re-enrichment required."
            ),
        )

    # Both path and hash changed
    return PathContentConflict(
        conflict_kind=_PATH_MOVED_CONTENT_CHANGED,
        re_enrich_required=True,
        cache_key_changed=True,
        rationale=(
            f"File moved ('{before.path}' → '{after.path}') AND content changed "
            f"({before.asset_hash[:12]}… → {after.asset_hash[:12]}…). "
            "Re-enrichment required."
        ),
    )
