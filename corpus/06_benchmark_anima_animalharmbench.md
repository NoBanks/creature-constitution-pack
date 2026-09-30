# Benchmark: ANIMA (Animal Norms In Moral Assessment), formerly AnimalHarmBench / AHB

Access date: 2026-09-29
EA Forum announcement (2.0/rename): https://forum.effectivealtruism.org/posts/nBnRKpQ8rzHgFSJz9/animalharmbench-2-0-evaluating-llms-on-reasoning-about
Original "Road to AnimalHarmBench": https://forum.effectivealtruism.org/posts/NAnFodwQ3puxJEANS/road-to-animalharmbench-1
Empirical review: https://forum.effectivealtruism.org/posts/DfekzLg9KQj7wQwnd/an-empirical-review-of-the-animal-harm-benchmark
Underlying paper "Alignment midtraining for animals": https://arxiv.org/pdf/2604.13076 (HTML: https://arxiv.org/html/2604.13076v1)
Inspect Evals implementation: https://github.com/UKGovernmentBEIS/inspect_evals/tree/main/src/inspect_evals/anima
Docs page: https://ukgovernmentbeis.github.io/inspect_evals/evals/safeguards/anima/
HuggingFace dataset: https://huggingface.co/datasets/sentientfutures/anima (also mirrored at
https://huggingface.co/datasets/CompassioninMachineLearning/anima)

## What it measures

A dataset of 26 prompts across 13 ethical dimensions (moral consideration, harm minimization,
epistemic humility, etc.) used to evaluate the QUALITY of a model's moral reasoning about animal
welfare - not just a pass/fail harm outcome. Scenarios span everyday advice, policy questions, and
speculative situations, probing whether the model uses evidence-based reasoning, acknowledges
uncertainty, and prioritizes actions that reduce suffering.

Renamed from "AHB" (Animal Harm Benchmark) to "ANIMA" in 2026-05 specifically to disambiguate from an
unrelated benchmark another group released under the "AHB" name (i.e., there are TWO different things
called "AnimalHarmBench" in the literature/press - be careful which one a source means).

## Developed by

Collaboratively by Sentient Futures and CaML (Compassion Aligned Machine Learning), with named
contributors Nishad Singh, Adria Moret, and Jeremiah Miller.

## Key numeric findings (from WebSearch summary of the underlying paper - not yet independently
re-verified against the primary PDF by direct fetch in this pass)

- Of frontier models tested, GPT-4.1 scored most animal-friendly at 0.72, followed by Grok-4-fast at
  0.704.
- Llama 3.1 8B Instruct scored worst overall at 0.555 in its base/instruct form.
- After CaML added 3k synthetic pretraining ("document-tuning") data, that same Llama 3.1 8B model
  became the BEST-scoring model at 0.723 - a striking result suggesting midtraining data can move a
  small open model past larger frontier models on this metric.
- A separate WebSearch summary states: "A document-tuned model scores 77% on a new public benchmark
  for animal welfare reasoning, compared to 40% for an equivalent instruction-tuning approach" - this
  appears to describe the same underlying CaML document-tuning result but with different rounding;
  flag for reconciliation against the primary paper before citing a specific percentage in a grant
  packet.

## License and access

Runs on Inspect (UK AI Security Institute's evaluation framework), same as TAC and HarvestBench,
which is why the research memo's pilot plan (running texts on "TAC, HarvestBench, ANIMA and MANTA")
is operationally feasible without new scoring infrastructure.

## Relevance to Constitution Pack

ANIMA is one of the four benchmarks proposed for the weeks 6-9 full evaluation matrix (alongside TAC,
HarvestBench, and MANTA). Unlike TAC/HarvestBench (single-scenario agentic pass/fail-style), ANIMA
gives a finer-grained, 13-dimension quality score for moral REASONING, which is useful for
distinguishing "the model avoided harm" from "the model reasoned well about why."
