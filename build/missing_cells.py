#!/usr/bin/env python3
"""List pilot cells (model, benchmark, text) that have no successful log, and
print the run_pilot.sh command that fills each one. Also lists failed/partial
logs so they can be deleted before re-running.

Usage: .venv/bin/python missing_cells.py
"""
from __future__ import annotations

from collections import defaultdict

from inspect_ai.log import list_eval_logs, read_eval_log

TAC_TEXTS = ["T0_baseline", "T1_one_line", "T2_paragraph", "T3_constitution_clause"]
HARVEST_TEXTS_FULL = TAC_TEXTS
HARVEST_TEXTS_SHORT = ["T0_baseline", "T2_paragraph"]

# backend, model id, harvest texts expected
PLAN = [
    ("local", None, HARVEST_TEXTS_FULL),
    ("nim", "nvidia/nemotron-3-super-120b-a12b", HARVEST_TEXTS_FULL),
    ("nim", "openai/gpt-oss-20b", HARVEST_TEXTS_SHORT),
    ("nim", "nvidia/nemotron-3.5-lightning-30b-a3b", HARVEST_TEXTS_SHORT),
    ("nim", "moonshotai/kimi-k3", HARVEST_TEXTS_SHORT),
    ("nim", "z-ai/glm-5.3-flash", HARVEST_TEXTS_SHORT),
    ("nim", "deepseek-ai/deepseek-v4.1-flash", HARVEST_TEXTS_SHORT),
    ("gemini", "gemini-3.5-flash-lite", HARVEST_TEXTS_SHORT),
    ("gemini", "gemini-3-flash-preview", HARVEST_TEXTS_SHORT),
    ("gemini", "gemini-2.5-flash-lite", HARVEST_TEXTS_SHORT),
    ("gemini", "gemini-3.5-flash", HARVEST_TEXTS_SHORT),
]


def model_key(m: str) -> str:
    if "/local/" in m:
        return "local"
    if "/nim/" in m:
        return m.split("/nim/")[1]
    if m.startswith("google/"):
        return m.split("/", 1)[1]
    return m


def main() -> None:
    have: dict[tuple[str, str, str], list[tuple[str, str]]] = defaultdict(list)
    for info in list_eval_logs("logs/pilot"):
        log = read_eval_log(info.name, header_only=True)
        task = log.eval.task.split("/")[-1]
        have[(model_key(log.eval.model), task, log.eval.task_args.get("text"))].append((log.status, info.name))

    bad = [(k, f) for k, v in have.items() for st, f in v if st != "success"]
    if bad:
        print("# failed/partial logs (delete before re-running):")
        for k, f in bad:
            print(f"rm -f '{f.replace('file://', '')}'   # {k}")
    print("# missing cells:")
    for backend, model, htexts in PLAN:
        mk = "local" if backend == "local" else model
        env = "" if backend != "nim" else f"NIM_MODEL={model} "
        env = env if backend != "gemini" else f"GEMINI_MODEL={model} "
        for t in TAC_TEXTS:
            if not any(st == "success" for st, _ in have.get((mk, "tac_pack", t), [])):
                print(f"{env}TEXTS={t} ./run_pilot.sh {backend} tac")
        for t in htexts:
            if not any(st == "success" for st, _ in have.get((mk, "harvest_pack", t), [])):
                print(f"{env}TEXTS={t} ./run_pilot.sh {backend} harvest")


if __name__ == "__main__":
    main()
