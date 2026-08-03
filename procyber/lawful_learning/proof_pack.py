"""Map a lawful-learning lifecycle record onto the CANONICAL estate ProofPack
(prophet-core-contracts proof-pack.schema.json) — ledger-convergence migration (#35).

The lifecycle digest is already a deterministic sha256; it becomes ``ledger.head``. The converged
constraint residual + Truth=Law*Evidence score become ``checks``, and the run's standing maps onto
the sp-core epistemic lattice (converged within constraints -> bounded; otherwise synthetic).
The caller supplies signatures (>=1) — an unsigned canonical pack is unrepresentable.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


def to_canonical_proof_pack(
    record: Dict[str, Any],
    *,
    subject_id: str,
    signatures: List[str],
    created_at: str,
    epistemic_level: Optional[str] = None,
    claim_mode: str = "fixture_validated",
) -> Dict[str, Any]:
    if not signatures or any(not s for s in signatures):
        raise ValueError("a canonical ProofPack requires >=1 non-empty signature")
    converged = bool(record.get("converged"))
    level = epistemic_level or ("bounded" if converged else "synthetic")
    truth = record.get("truth", {})
    truth_score = float(truth.get("T", 0.0)) if isinstance(truth, dict) else float(truth)
    return {
        "schema_version": "0.1.0",
        "proof_pack_id": "proofpack_" + record["digest"],
        "subject_ref": {"ref_type": "lawful_learning_run", "ref_id": subject_id},
        "claim_mode": claim_mode,
        "epistemic_level": level,
        "ledger": {"algo": "sha256", "head": record["digest"]},
        "checks": [
            {"name": "constraint_violation", "value": float(record.get("violation", 0.0)), "passed": converged},
            {"name": "truth_score", "value": truth_score, "passed": truth_score > 0.0},
        ],
        "evidence_refs": [record["loop_digest"]] if record.get("loop_digest") else [],
        "signatures": list(signatures),
        "provenance": {"producer": "procyber.lawful_learning"},
        "created_at": created_at,
    }
