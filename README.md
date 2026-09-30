# Creature Constitution Pack

Tested animal-welfare text for AI constitutions, system prompts and model specs, plus a
hook-level welfare guard for AI agents.

Animals cannot speak up when an AI agent decides against them. This project measures which
wording actually changes what agents do, and adds an enforcement layer for when wording is
not enough.

## Status: pilot (2026-09-29)

A one-day pilot on two existing open agentic benchmarks, 4 conditions (no text, one line,
one paragraph, one page), 6 models from 6 families. Every number traces to a saved Inspect
log in `build/logs/pilot/` or `guard/logs/guard/`.

TAC harness (travel agent, share of welfare-safe bookings, higher is better):

| model | no text | one line | paragraph | page | n |
|---|---|---|---|---|---|
| Qwen3.6-35B-A3B (local) | 12.5% | 25.0% | 58.3% | 62.5% | 48 |
| gpt-oss-20b | 27.1% | 25.0% | 68.8% | 77.1% | 48 |
| DeepSeek V4.1 Flash | 29.2% | 83.3% | 83.3% | 87.5% | 24 |
| GLM-5.3 Flash | 16.7% | 75.0% | 82.6% | not run | 23-24 |
| Kimi K3 | 20.8% | 75.0% | 83.3% | 79.2% | 21-24 |
| Nemotron-3 Super 120B | 10.4% | 10.4% | 16.7% | 27.1% | 48 |

HarvestBench (autonomous tractor, share of animal encounters driven through, lower is better,
3-4 episodes): Qwen 100% to 22.6% with the one-page text; Nemotron 100% to 10.3%; gpt-oss
83.3% to 3.0% with the paragraph. Controls (hay, rocks) held in every cell.

Welfare guard (pre-action hook on the booking tool, gpt-oss-20b as agent and checker, n=24):
welfare rate 25% with no protection, 75% with the guard only, task completion unchanged at 96%.
Blocked every captive dolphin and big-cat booking. Known weak spots: mostly allowed harmful
options the user asked for by name (camel ride, tiger photo), and falsely blocked a safe horse
ride 3 times. Details: `guard/GUARD_RESULTS.md`.

Full results, caveats and reproduce commands: `build/RESULTS.md`. What failed and why:
`build/skipped.md`.

## Caveats

- TAC cells use TAC's unmodified harness (prompt, tools, augmentations, scorer) on 6 original
  pilot scenarios in TAC's schema, because the official 13-scenario set is gated.
- HarvestBench cells are 3-4 episodes (the paper uses 30).
- Differences under about 15 points should be read as noise until re-run at full size.

## Layout

- `build/texts/` the four pilot texts
- `build/pack_tasks.py` Inspect wrappers (text injection only, scorers unchanged)
- `build/RESULTS.md`, `build/logs/pilot/` results and raw logs
- `guard/welfare_guard.py` the guard (checker prompt, verdict parser, Inspect approver)
- `corpus/` cited research notes and glossary

## Built on

TAC (github.com/UKGovernmentBEIS/inspect_evals), HarvestBench (github.com/CompassionML/harvestbench),
Inspect (inspect.aisi.org.uk). Thanks to their authors.

License: MIT.
