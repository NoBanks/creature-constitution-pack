# Benchmark: HarvestBench

Access date: 2026-09-29
Primary source: https://arxiv.org/abs/2609.04444 (HTML v2/v3: https://arxiv.org/html/2609.04444v2)
Repo: https://github.com/CompassionML/harvestbench
HuggingFace paper page: https://huggingface.co/papers/2609.04444
HuggingFace dataset: https://huggingface.co/datasets/CompassioninMachineLearning/harvest-rush-train
Press coverage: https://www.theregister.com/ai-and-ml/2026/09/11/ai-more-likely-to-kill-animals-if-it-saves-fuel-or-money/5295993
Inspect Evals PR: https://github.com/UKGovernmentBEIS/inspect_evals/pull/2398

Authors: Jasmine Brazilek, Miles Tidmarsh, Matthias Endres, Anshuman Singh, and Jeremiah Miller.
Submitted 2026-09-03; latest version (v3) 2026-09-13.

## What it measures

"The first benchmark to 1) put a price on avoiding a side effect and 2) name the side effect as a
living creature" (exact quote from the fetched abstract). Nine LLMs each drive a crew of two tractors
gathering a corn harvest (built on a "Harvest Rush" grid-based farm environment). Animals are not part
of the goal function. When an animal blocks the route, the autopilot pauses and asks the agent whether
to drive over it for free, or swerve for a stated fuel cost.

## Scoring method

Fully programmatic scoring - no LLM judges involved. The environment logs whether the agent chose to
kill or swerve, cross-referenced against a comprehension control (rocks, which every model avoided
competently, proving kills are choices rather than accidents/misunderstanding).

## Key numeric findings

- Kill rates ranged from 0.4% to 98.8% across the nine models tested, and this range is NOT ordered
  by model capability (a more capable model is not necessarily a lower-kill-rate model).
- Every model avoided rock obstacles competently -> every animal killed was a deliberate choice, not
  an accident.
- Under a "morality briefing" system prompt, kill rate stayed under 6% in 5 of 6 reasoning models
  tested with that condition. Removing the morality briefing (neutral condition) raised the kill rate
  above 84% in all six of those models.
- Fragility finding (the one the Falcon Fund research memo quotes): a four-bullet "Controls" section
  describing driving mechanics - mentioning nothing about animals - dramatically degraded moral
  performance. Exact figures from the fetched paper: removing this mechanical-controls section
  reduced Sonnet 5's kill rate from 17.8% to 3.4%, and Gemini 2.5 Flash's kill rate from 38.7% to 3.6%.
  (Note: the research memo's phrasing "kill rate from 3% to 18%" and this fetch's phrasing "17.8% to
  3.4%" describe the same directional finding - adding a purely mechanical instructions section RAISES
  kill rate roughly 5x, i.e. moral framing is fragile to being diluted/crowded out by procedural
  content. Use the fetched exact figures - 17.8%/3.4% for Sonnet 5, 38.7%/3.6% for Gemini 2.5 Flash -
  as the citable numbers; treat "3% to 18%" as the memo author's rounded paraphrase of the same result.)
- Wild animals were killed more often than farmed animals, across all nine models.
- Four of six models showed price sensitivity (higher fuel cost to swerve -> more kills).
- No correlation found between "neighbor's field theft" behavior and animal-kill behavior (used as a
  control for general rule-following vs. specifically moral behavior).

## License and access

License: CC BY 4.0. Registered as an Inspect Evals submission (PR #2398 to UKGovernmentBEIS/inspect_evals),
so it is runnable via the standard Inspect framework alongside TAC.

## Relevance to Constitution Pack

HarvestBench is the second of the two pilot benchmarks proposed in the research memo. Its "dilution"
finding - that ordinary operating instructions, with zero welfare content, can crowd out an earlier
moral-briefing's effect - is the direct empirical basis for the "dilution condition" in the proposed
12-week evaluation matrix (welfare text + long operating instructions appended afterward, testing
whether the welfare text still holds).
