"""Theorems of the associative-memory dynamics (procyber.semantic.dynamics) — the temporal organ
of the semantic substrate. Deterministic (the dynamics carry no RNG). These discharge the
CONSTRUCTION+THEOREM tiers: two-timescale consolidation, graceful fade-but-persist,
recency-is-not-persistence, bounded spreading activation, and associative / multi-hop retrieval.
"""
from __future__ import annotations

from procyber.semantic import dynamics as dyn


def test_single_cooccurrence_is_transient_repeated_consolidates():
    # THEOREM (edge dynamics t1→t2): the slow variable barely moves on one co-occurrence but
    # accumulates under repetition — consolidation REQUIRES repetition.
    m = dyn.AssociativeMemory()
    m.co_occur("A", "B")
    slow_once = m.slow("A", "B")
    for _ in range(6):
        m.co_occur("A", "B")
    slow_many = m.slow("A", "B")
    assert slow_once < 0.2
    assert slow_many > 3 * slow_once
    assert slow_many <= 1.0  # bounded


def test_fade_but_persist():
    # THEOREM (edge dynamics t3): without reinforcement associations decay, but a CONSOLIDATED one
    # persists far longer than a transient one — graceful, not a cliff to zero.
    m = dyn.AssociativeMemory()
    m.co_occur("A", "B")                 # transient (single co-occurrence)
    for _ in range(6):
        m.co_occur("C", "D")             # consolidated (repeated)
    transient_peak = m.effective("A", "B")
    consolidated_peak = m.effective("C", "D")
    m.tick(12)                           # time passes, no reinforcement
    transient_after = m.effective("A", "B")
    consolidated_after = m.effective("C", "D")
    assert transient_after < transient_peak
    assert consolidated_after < consolidated_peak
    assert consolidated_after > 0.0                     # persists
    assert consolidated_after > 3 * transient_after     # persists far longer than the transient
    assert transient_after < 0.25 * transient_peak      # the transient trace has all but vanished


def test_recency_is_not_persistence():
    # THEOREM: a single RECENT co-occurrence is strongly readable NOW (high fast) yet will not
    # persist (low slow) — the fast/slow split separates recency from durable memory.
    m = dyn.AssociativeMemory()
    m.co_occur("A", "B")
    assert m.fast("A", "B") > m.slow("A", "B")          # recency dominates immediately
    now = m.effective("A", "B")
    m.tick(10)
    later = m.effective("A", "B")
    assert now > 0.4 and later < 0.15                   # readable now, gone later


def test_spreading_activation_is_bounded_and_terminating():
    # THEOREM (governed read): activations stay in [0,1] for ANY horizon and the loop runs in
    # exactly `steps` hops — a bounded loop, not an open one.
    m = dyn.AssociativeMemory()
    for _ in range(5):
        m.observe(["A", "B", "C"])       # a reinforced clique to stress saturation
    for steps in (0, 1, 3, 25):
        act = m.spread(["A"], steps=steps)
        assert all(0.0 <= v <= 1.0 for v in act.values())
        assert act["A"] == 1.0           # seed pinned


def test_associative_retrieval_ranks_cooccurring_over_unrelated():
    # THEOREM (read path): spreading from a query entity returns its associates, not noise.
    m = dyn.AssociativeMemory()
    for _ in range(5):
        m.observe(["alice", "reputation"])   # strong
    m.observe(["alice", "weather"])          # weak (single co-occurrence)
    hits = dict(m.recall(["alice"], k=5))
    assert "reputation" in hits
    assert hits.get("reputation", 0.0) > hits.get("weather", 0.0)   # strong beats weak
    assert "unrelated" not in hits                                  # never co-occurred


def test_multi_hop_decays_with_distance():
    # THEOREM: activation falls off with graph distance — a 2-hop node is reachable but weaker
    # than the 1-hop node that bridges to it.
    m = dyn.AssociativeMemory()
    for _ in range(5):
        m.observe(["A", "B"])   # A–B
        m.observe(["B", "C"])   # B–C ; A and C never co-occur
    act = m.spread(["A"], steps=3)
    assert act.get("B", 0.0) > act.get("C", 0.0) > 0.0


def test_consolidated_associations_readout():
    # The durable projection fed to the twin / ontogenesis: only repeated pairs surface, de-duped.
    m = dyn.AssociativeMemory()
    for _ in range(6):
        m.observe(["A", "B"])
    m.co_occur("A", "X")   # single → transient, below threshold
    cons = m.consolidated_associations(threshold=0.25)
    pairs = {frozenset((a, b)) for a, b, _ in cons}
    assert frozenset(("A", "B")) in pairs
    assert frozenset(("A", "X")) not in pairs
