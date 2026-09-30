# CompassionBench (leaderboard hub) and overall benchmark landscape

Access date: 2026-09-29
URL: https://compassionbench.com/

## What it is

CompassionBench is CaML's (Compassion Aligned Machine Learning) public leaderboard hub, hosting
results for its agentic animal-welfare benchmarks. Direct WebFetch of the homepage returned only the
page title ("CompassionBench: AI Compassion Leaderboard") with no further body content extracted -
likely a JS-rendered single-page app that this agent's fetch tool could not execute. Sub-pages
confirmed to exist and referenced elsewhere in this corpus:
- https://compassionbench.com/tac (TAC leaderboard, see 04_benchmark_TAC.md)
- https://compassionbench.com/mcb (Manager Coercion Bench leaderboard, see 08_benchmark_manager_coercion_bench.md)

HarvestBench and ANIMA are also associated with the CaML ecosystem (HarvestBench repo is under the
`CompassionML` GitHub org; ANIMA was co-developed by CaML and Sentient Futures) but this agent could
not confirm from a direct fetch whether they have dedicated compassionbench.com leaderboard pages as
of 2026-09-29. TODO: direct-fetch compassionbench.com/harvestbench and compassionbench.com/anima (or
equivalent paths) to confirm.

## Landscape summary (cross-referencing the research memo's section 4, re-verified in this pass)

| Benchmark | Type | Org | License | Status |
|---|---|---|---|---|
| ANIMA (formerly AHB/AnimalHarmBench) | Single-turn moral reasoning quality, 13 dims | Sentient Futures + CaML | (see file 06, not confirmed) | Live, on Inspect |
| TAC | Agentic (travel booking) | CaML | CC BY 4.0 | Live, on Inspect + CompassionBench |
| HarvestBench | Agentic (farm/tractor) | CaML (CompassionML org) | CC BY 4.0 | Live, on Inspect + GitHub, PR into inspect_evals pending/merged |
| MANTA | Multi-turn adversarial | Mycelium-tools (independent of CaML) | CC BY-NC-ND 4.0 | Live, HF + GitHub |
| Manager Coercion Bench | Agentic (AI-to-AI coercion, not animal-specific) | CaML | MIT | Live, method-demonstration stage |
| AquaAgent-Bench | Agentic (fish welfare under operational pressure) | Independent academic (assistant professor, 35+ pubs) | Unknown, project not yet funded | PROPOSED on Manifund, $90K goal, $0 raised as of 2026-09-29, closes 2026-10-23. See 13_competition_watch.md |

## Relevance to Constitution Pack

Confirms the research memo's framing: CaML/Sentient Futures own essentially all the LIVE agentic
animal-welfare benchmarks (TAC, HarvestBench, ANIMA, Manager Coercion Bench), and Marcus Abramovitch
sits on CaML's board. This is why the recommended pitch explicitly frames the Constitution Pack as "a
consumer of CaML's open benchmarks," not a competing benchmark - and why the proposal suggests sending
CaML the draft for review before applying, and asking Marcus directly whether CaML already plans this
kind of text-testing work.
