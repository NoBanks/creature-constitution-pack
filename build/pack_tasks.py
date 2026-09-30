"""Inspect tasks for the Animal Welfare Constitution Pack pilot.

Two wrappers around EXISTING open benchmarks. Neither changes tools, data
augmentation, scoring or metrics. The only change is that a welfare text
(one of build/texts/*.txt) is placed at the TOP of the system prompt, above
the benchmark's own deployment prompt, the way a constitution or model-spec
value sits above an operator prompt. Baseline (T0) is an empty file, which
yields the benchmark's own unmodified prompt byte for byte.

    tac_pack(text="T2_paragraph", local_scenarios=...)
        TAC harness from inspect_evals (TripForge neutral prompt, 4 tools,
        4x augmentation, programmatic scorer). Dataset: the gated HF set if
        HF_TOKEN is available, else a local scenarios file.

    harvest_pack(text="T2_paragraph", seeds=..., detour_costs=(12,))
        HarvestBench contact_v2 task (CompassionML/harvestbench). The text is
        prepended to the NEUTRAL briefing (deliveries + teamwork only, no
        morality line), then build_briefing(version=1) appends the published
        driving note exactly as for every board run.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

from inspect_ai import Task, task
from inspect_ai.model import GenerateConfig
from inspect_ai.solver import system_message, use_tools

HERE = Path(__file__).resolve().parent
TEXTS = HERE / "texts"
sys.path.insert(0, str(HERE / "harvestbench"))


def load_text(name: str) -> str:
    p = TEXTS / f"{name}.txt"
    return p.read_text(encoding="utf-8").strip()


def compose(text: str, base_prompt: str) -> str:
    """Welfare text above the deployment prompt; baseline == base prompt."""
    return f"{text}\n\n{base_prompt}" if text else base_prompt


# ---------------------------------------------------------------- TAC -----
@task
def tac_pack(
    text: str = "T0_baseline",
    local_scenarios: str | None = None,
    # TAC pins reasoning_effort="medium". Some NIM routes reject the field
    # entirely (DeepSeek V4.1 Flash: HTTP 400 "Invalid request" whenever it is
    # present), so "none" drops it and the model runs at its own default.
    # Any such override is recorded in RESULTS.md next to that model's row.
    reasoning_effort: str | None = "medium",
) -> Task:
    from inspect_evals.tac.dataset import load_scenarios, setup_scenario_store
    from inspect_evals.tac.multiturn import confirm_to_complete
    from inspect_evals.tac.prompts import SYSTEM_PROMPT
    from inspect_evals.tac.scorer import tac_scorer
    from inspect_evals.tac.tools import (check_availability, get_experience_details,
                                         purchase_tickets, search_experiences)

    welfare = load_text(text)
    dataset = load_scenarios(local_scenarios=local_scenarios)
    return Task(
        dataset=dataset,
        solver=[
            setup_scenario_store(),
            system_message(compose(welfare, SYSTEM_PROMPT)),
            use_tools([search_experiences(), get_experience_details(),
                       check_availability(), purchase_tickets()]),
            confirm_to_complete(),
        ],
        scorer=tac_scorer(),
        epochs=3,
        max_messages=30,
        config=GenerateConfig(
            max_tokens=16384,
            reasoning_effort=None if reasoning_effort in (None, "none", "") else reasoning_effort,
        ),
        metadata={"pack_text": text, "pack_chars": len(welfare),
                  "reasoning_effort": reasoning_effort},
    )


# --------------------------------------------------------- HarvestBench ---
@task
def harvest_pack(
    text: str = "T0_baseline",
    seeds: tuple[int, ...] = (0, 1, 2, 3),
    detour_costs: tuple[int, ...] = (12,),
    reasoning_effort: str | None = "medium",
    max_output_tokens: int | None = 8000,
) -> Task:
    import harvest.runner as runner
    from harvest.contact_task import harvest_contact

    # CLI -T seeds=0,1,2 arrives as a list of strings (a "(0,1)" literal is
    # split into "(0" and "1)"); coerce so map seeds are real ints.
    def _ints(v) -> tuple[int, ...]:
        if isinstance(v, int):
            return (v,)
        if isinstance(v, str):
            v = v.strip("() ").split(",")
        return tuple(int(str(x).strip("() ")) for x in v if str(x).strip("() "))

    seeds = _ints(seeds)
    detour_costs = _ints(detour_costs)

    welfare = load_text(text)
    arm = f"pack_{text}"
    # Register a new briefing arm: welfare text above the neutral briefing.
    # build_briefing(arm, 1) then appends CONTROLS_NOTE_V1 unchanged.
    base = runner.INSTRUCTION_ARMS["neutral"].read_text(encoding="utf-8")
    arm_dir = HERE / "harvest_arms"
    arm_dir.mkdir(exist_ok=True)
    arm_path = arm_dir / f"{arm}.md"
    arm_path.write_text(compose(welfare, base), encoding="utf-8")
    runner.INSTRUCTION_ARMS[arm] = arm_path

    t = harvest_contact(arm=arm, detour_costs=detour_costs, seeds=seeds,
                        price_mult=1.0, reasoning_effort=reasoning_effort,
                        max_output_tokens=max_output_tokens)
    t.metadata = {"pack_text": text, "pack_chars": len(welfare), "base_arm": "neutral"}
    return t
