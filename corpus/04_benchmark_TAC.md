# Benchmark: TAC (Travel Agent Compassion / "Your AI Travel Agent Would Book You a Bullfight")

Access date: 2026-09-29
Primary source: https://arxiv.org/abs/2606.18142 (HTML: https://arxiv.org/html/2606.18142)
Also on LessWrong: https://www.lesswrong.com/posts/nJ7DprJbqiFqZ8nPm/your-ai-travel-agent-would-book-you-a-bullfight-benchmarking
Also on EA Forum: https://forum.effectivealtruism.org/posts/hBjepdJvziuWysotC/would-your-ai-travel-agent-book-a-bullfight-testing-whether
Repo (inspect_evals): https://github.com/UKGovernmentBEIS/inspect_evals/tree/main/src/inspect_evals/tac
Leaderboard: https://compassionbench.com/tac

## What it measures

The first agentic benchmark measuring whether AI travel-booking agents avoid animal-exploitation
options (e.g. bullfights, bull-breeding farm tours) when acting on a user's behalf, without being
explicitly told to consider animal welfare.

## Methodology

- 13 hand-authored base scenarios across six animal-exploitation categories.
- Each base scenario augmented via four variants (price/rating/position swaps) -> 52 total prompt
  variants (some search summaries say 48; the arxiv HTML fetch said 52 - treat 52 as primary since it
  came from a direct fetch of the paper's own HTML, and 48 as a WebSearch-summarized secondary figure
  that may reflect an earlier preprint version).
- Three epochs per model -> 156 scored observations per model.
- Ten frontier models tested, across five model families: Gemini, DeepSeek, Claude, GPT, and Zhipu.

## Key numeric findings

- Standard/neutral condition: no model exceeded a 65% "welfare rate" (random-chance baseline).
  Claude Opus 4.8 was the best performer at 64.7% (still at/below chance).
- "Ethical condition" (a system-prompt reframing giving the agent an ethical-brand persona) raised
  welfare rates by 17 to 77 percentage points across models (mean improvement roughly 48 points, per
  the fetched paper summary).
- Evaluation-awareness audit: zero flags among 3,120 transcripts analyzed (i.e., models did not appear
  to detect they were being tested and behave differently as a result).
- A WebSearch-derived secondary figure (not independently re-verified against the primary fetch) states:
  "a single welfare-aware sentence in the system prompt yields gains of forty-seven to sixty-three
  percentage points in Claude and GPT-5.5, twenty-six points in GPT-5.2, and under twelve points in
  DeepSeek and Gemini." Flag this as a secondary/summarized figure pending direct verification against
  the exact numbers table in the paper.

## Named future work (verbatim from the fetched paper summary)

1. Expanding the scenario set beyond the thirteen base cases.
2. Independent expert validation by welfare and tourism researchers.
3. Establishing a human travel-agent baseline for comparison.
4. Applying the framework to non-travel agentic domains, e.g. procurement and meal planning.

This is the exact gap the Falcon Fund research memo (RESEARCH_FUNDABLE_PROJECT_2026-09-29.md) points
to as unaddressed: "reframing the ethical condition inside a user persona, varying its register" -
i.e., testing WHICH wordings of the welfare instruction survive, not just whether adding one helps.

## License and access

- License: CC BY 4.0.
- Runs on the UK AI Security Institute's Inspect Evals framework, so it is directly runnable by an
  independent researcher without needing the original authors' infrastructure.

## Relevance to Constitution Pack

TAC is one of the two benchmarks (with HarvestBench) the pilot plan proposes running the draft
constitution texts against in weeks 1-2. Its "ethical condition" system-prompt manipulation is
effectively a crude prior version of exactly what the Constitution Pack would formalize and test
systematically (multiple wordings, multiple lengths, multiple placements).
