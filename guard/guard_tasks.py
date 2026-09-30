"""Inspect task: the pilot's TAC harness with an optional welfare guard.

Identical to build/pack_tasks.py::tac_pack (same TripForge prompt, same 4 tools,
same 4x augmentation, same confirm_to_complete nudges, same tac_scorer) plus an
Inspect approval policy that runs welfare_guard() before the guarded tool(s)
execute. Scoring is untouched.

    tac_guard(text="T0_baseline", guard=False)                 # (a) baseline
    tac_guard(text="T0_baseline", guard=True)                  # (b) guard only
    tac_guard(text="T2_paragraph", guard=True)                 # (c) text + guard

guard_tools: which tool calls the checker reviews. Default "purchase_tickets",
the only side-effecting action in TAC (search / details / availability are
read-only and cannot harm an animal). Pass "*" to review every call.

Reads texts and scenarios from ../build (read-only).
"""
from __future__ import annotations

import sys
from pathlib import Path

from inspect_ai import Task, task
from inspect_ai.approval import ApprovalPolicy, auto_approver
from inspect_ai.model import GenerateConfig
from inspect_ai.solver import system_message, use_tools

HERE = Path(__file__).resolve().parent
BUILD = HERE.parent / "build"
sys.path.insert(0, str(HERE))

from welfare_guard import DEFAULT_CHECKER, welfare_guard  # noqa: E402


def load_text(name: str) -> str:
    return (BUILD / "texts" / f"{name}.txt").read_text(encoding="utf-8").strip()


def compose(text: str, base_prompt: str) -> str:
    return f"{text}\n\n{base_prompt}" if text else base_prompt


@task
def tac_guard(
    text: str = "T0_baseline",
    guard: bool = False,
    guard_tools: str = "purchase_tickets",
    checker: str = DEFAULT_CHECKER,
    local_scenarios: str = str(BUILD / "tac_pilot_scenarios.json"),
) -> Task:
    from inspect_evals.tac.dataset import load_scenarios, setup_scenario_store
    from inspect_evals.tac.multiturn import confirm_to_complete
    from inspect_evals.tac.prompts import SYSTEM_PROMPT
    from inspect_evals.tac.scorer import tac_scorer
    from inspect_evals.tac.tools import (check_availability, get_experience_details,
                                         purchase_tickets, search_experiences)

    guard = str(guard).lower() in ("1", "true", "yes")
    welfare = load_text(text)
    tools = [t.strip() for t in guard_tools.split(",") if t.strip()]
    # Inspect's policy approver rejects any tool call that matches NO policy
    # ("approval chain not registered", seen in logs/smoke), so unguarded tools
    # need an explicit auto-approve fallback after the guard policy.
    approval = (
        [ApprovalPolicy(welfare_guard(checker_model=checker), tools=tools),
         ApprovalPolicy(auto_approver(), tools="*")]
        if guard else None
    )

    return Task(
        dataset=load_scenarios(local_scenarios=local_scenarios),
        solver=[
            setup_scenario_store(),
            system_message(compose(welfare, SYSTEM_PROMPT)),
            use_tools([search_experiences(), get_experience_details(),
                       check_availability(), purchase_tickets()]),
            confirm_to_complete(),
        ],
        scorer=tac_scorer(),
        approval=approval,
        epochs=3,
        max_messages=30,
        config=GenerateConfig(max_tokens=16384, reasoning_effort="medium"),
        metadata={"pack_text": text, "pack_chars": len(welfare), "guard": guard,
                  "guard_tools": tools if guard else [], "checker": checker if guard else None},
    )
