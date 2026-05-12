"""
Reference implementation of the persona -> substrategy chooser for agentic ops.

This resolver takes:
  - a persona policy (objective weights + hard constraints + agentic axes)
  - a workload signature (scenario, data class, expected trajectory shape)

and returns:
  - resolved substrategy bundle
  - per-step admission predicate
  - rejection reason when inadmissible
  - deterministic rationale for each decision family

Designed to be deterministic and auditable: every decision should be traceable
to a rule with a documented antecedent.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, Optional


class DataClass(str, Enum):
    PUBLIC = "public"
    INTERNAL = "internal"
    SENSITIVE = "sensitive"
    REGULATED = "regulated"
    FORENSIC = "forensic"


class Scenario(str, Enum):
    INTERACTIVE_QA = "interactive_qa"
    PLAN_THEN_EXECUTE = "plan_then_execute"
    REACT_EXPLORATION = "react_exploration"
    MULTI_AGENT_PIPELINE = "multi_agent_pipeline"
    LONG_HORIZON_ASSISTANT = "long_horizon_assistant"


class ReversibilityClass(str, Enum):
    NONE = "none"
    IDEMPOTENT_ONLY = "idempotent_only"
    COMPENSABLE = "compensable"
    UNRESTRICTED = "unrestricted"


@dataclass(frozen=True)
class Objectives:
    latency: float
    throughput: float
    cost_predictability: float
    correctness: float
    auditability: float
    ops_simplicity: float
    reproducibility: float
    collaboration: float

    def __post_init__(self) -> None:
        total = (
            self.latency
            + self.throughput
            + self.cost_predictability
            + self.correctness
            + self.auditability
            + self.ops_simplicity
            + self.reproducibility
            + self.collaboration
        )
        if abs(total - 1.0) > 1e-6:
            raise ValueError(f"objective weights must sum to 1.0, got {total}")


@dataclass(frozen=True)
class Budget:
    tokens_in_max: int
    tokens_out_max: int
    tool_calls_max: int
    wall_clock_seconds_max: float
    dollars_max: float


@dataclass(frozen=True)
class AgenticAxes:
    autonomy_depth: int
    reversibility: ReversibilityClass
    plan_mode: str
    max_replans: int
    verification_judge_rate: float
    self_consistency_k: int
    cascade_enabled: bool


@dataclass(frozen=True)
class PersonaPolicy:
    persona_id: str
    objectives: Objectives
    budget: Budget
    axes: AgenticAxes
    data_class_allowlist: set[DataClass]
    max_staleness_seconds: int


@dataclass(frozen=True)
class WorkloadSignature:
    scenario: Scenario
    data_class: DataClass
    expected_trajectory_length: int
    expected_tool_calls: int
    read_write_ratio: float
    hotness_skew: float
    sensitivity_class: DataClass


@dataclass(frozen=True)
class ResolvedBundle:
    substrategies: list[str]
    admission_predicate: Callable[[WorkloadSignature], bool]
    rejection_reason: Optional[str] = None
    rationale: dict[str, str] = field(default_factory=dict)


def _reject(reason: str) -> ResolvedBundle:
    return ResolvedBundle(
        substrategies=[],
        admission_predicate=lambda _: False,
        rejection_reason=reason,
        rationale={"rejection": reason},
    )


def resolve_substrategies(
    persona: PersonaPolicy,
    workload: WorkloadSignature,
) -> ResolvedBundle:
    """Resolve an auditable substrategy bundle for an agentic workload."""

    rationale: dict[str, str] = {}
    bundle: list[str] = []

    if workload.data_class not in persona.data_class_allowlist:
        return _reject(
            f"data class {workload.data_class.value} not in persona allowlist "
            f"{sorted(d.value for d in persona.data_class_allowlist)}"
        )

    expected_in = workload.expected_trajectory_length * 4000
    expected_out = workload.expected_trajectory_length * 200

    if expected_in > persona.budget.tokens_in_max:
        return _reject(
            f"expected tokens_in {expected_in} exceeds persona budget "
            f"{persona.budget.tokens_in_max}"
        )

    if expected_out > persona.budget.tokens_out_max:
        return _reject(
            f"expected tokens_out {expected_out} exceeds persona budget "
            f"{persona.budget.tokens_out_max}"
        )

    if workload.expected_tool_calls > persona.budget.tool_calls_max:
        return _reject(
            f"expected tool calls {workload.expected_tool_calls} exceeds persona budget "
            f"{persona.budget.tool_calls_max}"
        )

    if workload.expected_trajectory_length > persona.axes.autonomy_depth:
        bundle.append("human_checkpoint_before_autonomy_depth_exceeded")
        rationale["autonomy_depth"] = (
            "expected trajectory length exceeds persona autonomy depth; checkpoint required"
        )

    if workload.expected_trajectory_length > 3:
        bundle.append("prefix_cache_with_section_breakpoints")
        bundle.append("tool_result_canonicalization")
        rationale["prefix_cache"] = "trajectory length > 3, amortization wins"

    if persona.axes.plan_mode == "plan_then_execute":
        bundle.append("plan_commit_before_execute")
        rationale["plan_mode"] = "persona requires plan stability"
    elif persona.axes.plan_mode == "plan_with_revision":
        bundle.append(f"plan_with_max_{persona.axes.max_replans}_revisions")
        rationale["plan_mode"] = "persona permits bounded replanning"
    else:
        bundle.append("react_interleaved")
        rationale["plan_mode"] = "persona permits ReAct-style exploration"

    if persona.axes.cascade_enabled and workload.scenario != Scenario.INTERACTIVE_QA:
        bundle.append("model_cascade_with_confidence_escalation")
        rationale["cascade"] = "non-interactive workload and cascade enabled"

    if persona.axes.verification_judge_rate >= 1.0:
        bundle.append("llm_judge_every_output")
        rationale["verification"] = "persona requires verification on every output"
    elif persona.axes.verification_judge_rate > 0:
        bundle.append(f"llm_judge_sample_rate_{persona.axes.verification_judge_rate}")
        rationale["verification"] = "persona requires sampled verification"

    if persona.axes.self_consistency_k >= 2:
        bundle.append(f"self_consistency_k_{persona.axes.self_consistency_k}_majority")
        rationale["self_consistency"] = (
            "correctness-weighted persona; expected error reduction scales approximately "
            f"as 1/sqrt({persona.axes.self_consistency_k}) under independence assumptions"
        )

    if persona.axes.reversibility == ReversibilityClass.NONE:
        bundle.append("readonly_tools_only")
        rationale["reversibility"] = "persona forbids external mutations"
    elif persona.axes.reversibility == ReversibilityClass.IDEMPOTENT_ONLY:
        bundle.append("idempotency_key_required_for_mutations")
        rationale["reversibility"] = "persona permits only idempotent mutations"
    elif persona.axes.reversibility == ReversibilityClass.COMPENSABLE:
        bundle.append("two_phase_commit_with_compensating_actions")
        rationale["reversibility"] = "persona requires compensating actions for mutations"

    if workload.hotness_skew > 0.7:
        bundle.append("idempotent_tool_result_cache_with_admission_control")
        rationale["hotness"] = f"skew {workload.hotness_skew} > 0.7"

    if workload.data_class in {
        DataClass.SENSITIVE,
        DataClass.REGULATED,
        DataClass.FORENSIC,
    }:
        bundle.append("immutable_append_only_trajectory_log")
        bundle.append("trajectory_hash_chain")
        bundle.append("per_data_class_memory_isolation")
        rationale["audit"] = "elevated data class requires evidentiary chain"

    if persona.objectives.auditability >= 0.25:
        bundle.append("per_step_uco_attribution_emit")
        rationale["uco"] = "auditability objective >= 0.25"

    loop_threshold = max(3, persona.axes.autonomy_depth // 2)
    bundle.append(f"loop_detector_repeated_args_threshold_{loop_threshold}")
    rationale["loop_detector"] = "loop detection threshold derived from autonomy depth"

    def admission(_workload: WorkloadSignature) -> bool:
        return True

    return ResolvedBundle(
        substrategies=bundle,
        admission_predicate=admission,
        rationale=rationale,
    )


if __name__ == "__main__":
    regulated = PersonaPolicy(
        persona_id="regulated-enterprise-assistant",
        objectives=Objectives(
            latency=0.05,
            throughput=0.05,
            cost_predictability=0.15,
            correctness=0.30,
            auditability=0.30,
            ops_simplicity=0.05,
            reproducibility=0.05,
            collaboration=0.05,
        ),
        budget=Budget(
            tokens_in_max=200_000,
            tokens_out_max=8_000,
            tool_calls_max=40,
            wall_clock_seconds_max=300,
            dollars_max=5.0,
        ),
        axes=AgenticAxes(
            autonomy_depth=5,
            reversibility=ReversibilityClass.COMPENSABLE,
            plan_mode="plan_then_execute",
            max_replans=1,
            verification_judge_rate=1.0,
            self_consistency_k=3,
            cascade_enabled=False,
        ),
        data_class_allowlist={
            DataClass.INTERNAL,
            DataClass.SENSITIVE,
            DataClass.REGULATED,
        },
        max_staleness_seconds=0,
    )

    research = PersonaPolicy(
        persona_id="research-throughput",
        objectives=Objectives(
            latency=0.05,
            throughput=0.40,
            cost_predictability=0.05,
            correctness=0.15,
            auditability=0.05,
            ops_simplicity=0.05,
            reproducibility=0.20,
            collaboration=0.05,
        ),
        budget=Budget(
            tokens_in_max=2_000_000,
            tokens_out_max=50_000,
            tool_calls_max=500,
            wall_clock_seconds_max=7200,
            dollars_max=100.0,
        ),
        axes=AgenticAxes(
            autonomy_depth=100,
            reversibility=ReversibilityClass.UNRESTRICTED,
            plan_mode="react",
            max_replans=10,
            verification_judge_rate=0.1,
            self_consistency_k=1,
            cascade_enabled=True,
        ),
        data_class_allowlist={DataClass.PUBLIC, DataClass.INTERNAL},
        max_staleness_seconds=3600,
    )

    workload = WorkloadSignature(
        scenario=Scenario.PLAN_THEN_EXECUTE,
        data_class=DataClass.REGULATED,
        expected_trajectory_length=15,
        expected_tool_calls=8,
        read_write_ratio=0.7,
        hotness_skew=0.4,
        sensitivity_class=DataClass.REGULATED,
    )

    for name, policy in [("regulated", regulated), ("research", research)]:
        print(f"\n=== {name} persona on regulated workload ===")
        result = resolve_substrategies(policy, workload)
        if result.rejection_reason:
            print(f"REJECTED: {result.rejection_reason}")
        else:
            for strategy in result.substrategies:
                print(f"  - {strategy}")
            print("  rationale:")
            for key, value in result.rationale.items():
                print(f"    {key}: {value}")
