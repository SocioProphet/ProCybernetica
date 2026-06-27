.PHONY: test triune-ci triune-render-ci triune-exec-ci

test:
	python -m pytest -q

triune-ci:
	python -m pytest -q tests/test_triune_admission.py

triune-render-ci:
	python -m pytest -q tests/test_triune_cluster_member_render.py tests/test_triune_admission_pack_render.py

triune-exec-ci: triune-ci triune-render-ci
