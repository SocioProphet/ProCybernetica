"""Serialization channel — the single outbound path (yesod).

Everything the kernel sends to a counterparty leaves through `emit`, and nothing
else produces a `WireEnvelope`. The point of a chokepoint is not tidiness: it is
that a governed decision is only worth something if there is exactly one place the
effect can happen, so that place can be made to check.

What the chokepoint checks
--------------------------
`emit` refuses unless the caller presents an `InternalModelState` whose equilibrium
clears the share threshold. That is the join between the two organs: `daat` decides,
`yesod` transmits, and transmission is not reachable without a decision. An agent
cannot route around its own share/withhold equilibrium by serialising somewhere else,
because there is nowhere else.

This is deliberately the inverse of the usual arrangement, where a policy check is
something a call site remembers to perform. Here the check is on the only path out,
so forgetting it is not expressible.

What "outbound" means
---------------------
Crossing to a counterparty. Building a dict for local use is not outbound, and
`to_json()` methods on kernel types remain free — they produce structure, not wire.
The invariant is narrower and therefore actually enforceable: **only this module
constructs a sealed envelope, and only `semantic_algebra.canonical_json` and this
module encode JSON.** `single_channel_violations` checks both, and is wired into the
test suite so a second path fails the build rather than being noticed later.

Sealing
-------
The envelope carries a digest over its canonical body. That is integrity, not
confidentiality — it lets a receiver detect alteration in transit; it does not hide
anything and is not a substitute for transport security.

Pure and local-first: stdlib only, no network. This module decides the shape of what
leaves and seals it; actually putting bytes on a wire belongs to a transport that
takes an envelope it cannot forge.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

from procyber.semantic.internal_model import InternalModelState
from procyber.semantic.semantic_algebra import BOTTOM, SemanticAddress, canonical_json

SPEC_VERSION = "0.1.0"

REPO = Path(__file__).resolve().parents[2]

#: Modules permitted to encode JSON: the encoding primitive, and this chokepoint.
#: Anything else doing its own encoding is a second way out.
ENCODING_PERMITTED = ("semantic_algebra.py", "serialization_channel.py")


class ChannelRefusal(RuntimeError):
    """Raised when emission is attempted without a cleared share decision.

    An exception rather than a falsy return: a refused transmission that a caller
    can ignore by not checking the result is not a refusal.
    """


@dataclass(frozen=True)
class WireEnvelope:
    """A sealed outbound payload. Only `emit` constructs one."""

    channel: str
    body: str
    digest: str
    spec_version: str = SPEC_VERSION

    def verify(self) -> bool:
        """True if the body still matches its digest."""
        return self.digest == _digest(self.body)

    def to_json(self) -> Dict[str, object]:
        return {
            "specVersion": self.spec_version,
            "channel": self.channel,
            "body": self.body,
            "digest": self.digest,
        }


def _digest(body: str) -> str:
    return "sha256:" + hashlib.sha256(body.encode("utf-8")).hexdigest()


def emit(
    payload: Dict[str, object],
    *,
    channel: str,
    decision: InternalModelState,
    address: Optional[SemanticAddress] = None,
) -> WireEnvelope:
    """The only way out. Refuses unless the share decision clears.

    `decision` is required and positional-keyword: there is no default and no
    overload that omits it, so a call site cannot transmit without having asked.
    When `address` is given, its warrant travels with the payload — a receiver that
    cannot see why something was sent cannot evaluate it.
    """
    if not isinstance(payload, dict):
        raise TypeError(f"outbound payload must be a mapping, got {type(payload).__name__}")

    verdict = decision.equilibrium
    if verdict is BOTTOM:
        raise ChannelRefusal(
            f"channel {channel!r}: share decision abstained — {decision.binding_reason()}"
        )
    if not decision.may_share():
        raise ChannelRefusal(
            f"channel {channel!r}: share decision did not clear ({verdict}) — "
            f"{decision.binding_reason()}"
        )

    envelope_body: Dict[str, object] = {
        "specVersion": SPEC_VERSION,
        "channel": channel,
        "payload": payload,
        "warrant": {
            "verdict": verdict,
            "bindingReason": decision.binding_reason(),
        },
    }
    if address is not None:
        # The skeleton, never the full address: structure travels, the referent and
        # the evidence pointer stay behind unless the caller put them in the payload
        # deliberately.
        envelope_body["address"] = address.skeleton()

    body = canonical_json(envelope_body)
    return WireEnvelope(channel=channel, body=body, digest=_digest(body))


# --------------------------------------------------------------------------- #
# The teeth — a second path must fail the build
# --------------------------------------------------------------------------- #

_ENCODES_JSON = re.compile(r"\bjson\s*\.\s*dumps\s*\(")
_CONSTRUCTS_ENVELOPE = re.compile(r"\bWireEnvelope\s*\(")

_SELF = Path(__file__).name


def single_channel_violations(paths: Optional[Sequence[str]] = None) -> List[Tuple[str, int, str]]:
    """Return (file, line, finding) for every second outbound path. Empty == one path.

    Two findings:
      * JSON encoded outside the encoding primitive and this module
      * a `WireEnvelope` constructed anywhere but here

    Scans the kernel package by default. A chokepoint asserted in prose is not a
    chokepoint, which is the whole reason this function exists rather than a comment.
    """
    targets = (
        [str(p) for p in (REPO / "procyber" / "semantic").glob("*.py")]
        if paths is None
        else list(paths)
    )
    findings: List[Tuple[str, int, str]] = []
    for target in targets:
        path = Path(target)
        if not path.exists():
            continue
        for lineno, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            if _ENCODES_JSON.search(line) and path.name not in ENCODING_PERMITTED:
                findings.append((str(path), lineno, "JSON encoded outside the channel"))
            if _CONSTRUCTS_ENVELOPE.search(line) and path.name != _SELF:
                findings.append((str(path), lineno, "WireEnvelope constructed outside the channel"))
    return findings
