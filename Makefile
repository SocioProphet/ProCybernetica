.PHONY: test governance-fabric-tier1-ci governance-fabric-tier2-ci governance-fabric-ci triune-ci falsification-static falsification-fixtures falsification-cross-reference falsification-ci cybernetic-governance-fixtures cybernetic-governance-ci dependency-control-fixtures dependency-control-ci agentic-ops-fixtures agentic-ops-ci bridges-fixtures bridges-ci certificate-v13-fixtures certificate-v13-ci shacl-companions shacl-ci profiles-fixtures profiles-ci v0-schemas-fixtures v0-schemas-ci agentplane-binding-fixtures agentplane-binding-ci proof-pack-fixtures proof-pack-ci lawful-learning-fixtures lawful-learning-ci hpl-reconciliation hpl-ci book-xi-slice-a-fixtures book-xi-slice-a-ci civic-stack-fixtures civic-stack-ci estate-alignment-followups estate-alignment-followups-ci

test:
	python -m pytest -q

governance-fabric-tier1-ci:
	python -m pytest -q tests/test_governance_fabric_tier1.py

governance-fabric-tier2-ci:
	python -m pytest -q tests/test_governance_fabric_tier2.py

governance-fabric-ci: governance-fabric-tier1-ci governance-fabric-tier2-ci

triune-ci:
	python -m pytest -q tests/test_triune_admission.py

falsification-static:
	python scripts/validate_falsification_coverage.py

falsification-fixtures:
	python scripts/validate_falsification_fixture.py

falsification-cross-reference:
	python scripts/validate_falsification_coverage.py

falsification-ci: falsification-static falsification-fixtures falsification-cross-reference

cybernetic-governance-fixtures:
	python tools/cybernetic_governance/validate_defensive_fixtures.py

cybernetic-governance-ci: cybernetic-governance-fixtures

dependency-control-fixtures:
	python tools/cybernetic_governance/validate_dependency_control.py

dependency-control-ci: dependency-control-fixtures

agentic-ops-fixtures:
	python tools/cybernetic_governance/validate_agentic_ops.py

agentic-ops-ci: agentic-ops-fixtures

bridges-fixtures:
	python tools/cybernetic_governance/validate_bridges.py

bridges-ci: bridges-fixtures

certificate-v13-fixtures:
	python tools/cybernetic_governance/validate_certificate_v13.py

certificate-v13-ci: certificate-v13-fixtures

shacl-companions:
	python tools/cybernetic_governance/validate_shacl_companions.py

shacl-ci: shacl-companions

profiles-fixtures:
	python tools/cybernetic_governance/validate_profiles.py

profiles-ci: profiles-fixtures

v0-schemas-fixtures:
	python tools/cybernetic_governance/validate_v0_schemas.py

v0-schemas-ci: v0-schemas-fixtures

agentplane-binding-fixtures:
	python tools/cybernetic_governance/validate_agentplane_binding.py

agentplane-binding-ci: agentplane-binding-fixtures

proof-pack-fixtures:
	python tools/cybernetic_governance/validate_proof_pack.py

proof-pack-ci: proof-pack-fixtures

lawful-learning-fixtures:
	python tools/cybernetic_governance/validate_lawful_learning.py

lawful-learning-ci: lawful-learning-fixtures
	PYTHONPATH=. python -m pytest -q tests/test_lawful_learning_toy.py tests/test_lawful_learning_conformance.py

hpl-reconciliation:
	python tools/cybernetic_governance/validate_hpl_reconciliation.py

hpl-ci: hpl-reconciliation

book-xi-slice-a-fixtures:
	python tools/cybernetic_governance/validate_book_xi_slice_a.py

book-xi-slice-a-ci: book-xi-slice-a-fixtures

civic-stack-fixtures:
	python tools/cybernetic_governance/validate_civic_stack.py

civic-stack-ci: civic-stack-fixtures

estate-alignment-followups:
	python tools/cybernetic_governance/validate_estate_alignment_followups.py

estate-alignment-followups-ci: estate-alignment-followups
