from procyber.lawful_learning.toy import (
    differences,
    dominance_slack,
    edgeworth_project_f11,
    end_to_end_example,
    learned_gate,
    monotone_projection_pava,
    spectral_construction_example,
)


def approx(a, b, tol=1e-3):
    assert abs(a - b) <= tol, (a, b)


def test_spectral_construction():
    out = spectral_construction_example()
    approx(out["lambda"][0], 2.207, 1e-3)
    approx(out["lambda"][1], 0.793, 1e-3)
    approx(out["lambda"][2], 0.300, 1e-3)
    approx(out["u"], 0.911, 1e-3)
    assert out["poincare_norm"] < 1.0


def test_monotone_projection():
    projected = monotone_projection_pava([0.10, 0.18, 0.15, 0.31])
    expected = [0.10, 0.165, 0.165, 0.31]
    for got, exp in zip(projected, expected):
        approx(got, exp, 1e-12)
    assert all(d >= -1e-12 for d in differences(projected))


def test_dominance_slack():
    out = dominance_slack([0.20, 0.30, 0.40], [0.25, 0.15, 0.20], gate=0.80, mu_min=1, mu_max=20)
    approx(out["slack"][0], 0.05, 1e-12)
    approx(out["mu"], 16.2, 1e-12)
    approx(out["penalty"], 0.0405, 1e-12)


def test_edgeworth_projection():
    out = edgeworth_project_f11(1.00, 1.30, 1.20, 1.45)
    approx(out["cross_difference"], -0.05, 1e-12)
    approx(out["projected_f11"], 1.50, 1e-12)
    assert out["projected_cross_difference"] >= 0


def test_learned_gate():
    approx(learned_gate(2.10, 1.70, 0.25), 0.832, 1e-3)
    approx(learned_gate(1.40, 1.70, 0.25), 0.231, 1e-3)


def test_end_to_end_truth_score():
    out = end_to_end_example()
    approx(out["truth"]["L"], 0.50, 1e-12)
    approx(out["truth"]["E"], 0.98, 1e-12)
    approx(out["truth"]["T"], 0.49, 1e-12)
    assert len(out["digest"]) == 64
