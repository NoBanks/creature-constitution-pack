# Corpus Index: Creature Constitution Pack research

Built 2026-09-29 for the Falcon Fund "Animal Welfare Constitution Pack" project (see
../RESEARCH_FUNDABLE_PROJECT_2026-09-29.md for the funding strategy this corpus supports). This
index and all files below are read-only research grounding for RAG / agent use - not final grant
copy. Every claim in every file is either a direct verbatim quote with URL, or explicitly flagged as
a secondary/summarized/unverified finding needing re-check.

| File | Topic | Primary source URL(s) | Access date |
|---|---|---|---|
| 01_anthropic_claude_constitution.md | Anthropic Claude constitution, "welfare of animals and of all sentient beings" | https://www.anthropic.com/research/claudes-constitution ; https://forum.effectivealtruism.org/posts/LQAcbWatjodhjGkgw/claude-s-constitution-is-great ; https://www.lesswrong.com/posts/YN5Szk7BZZX3SzTvz/claude-s-constitution-is-great | 2026-09-29 |
| 02_openai_model_spec.md | OpenAI Model Spec, "overly moralistic tone" / dog-adoption example | https://model-spec.openai.com/2025-02-12.html | 2026-09-29 |
| 03_other_labs_animal_mentions.md | Google DeepMind / Meta / xAI / Mistral - search for animal-welfare language | https://metr.org/common-elements ; https://deepmind.google/frontier-safety/ | 2026-09-29 |
| 04_benchmark_TAC.md | TAC benchmark (Travel Agent Compassion / bullfight paper) | https://arxiv.org/html/2606.18142 ; https://github.com/UKGovernmentBEIS/inspect_evals/tree/main/src/inspect_evals/tac ; https://compassionbench.com/tac | 2026-09-29 |
| 05_benchmark_harvestbench.md | HarvestBench benchmark | https://arxiv.org/html/2609.04444v2 ; https://github.com/CompassionML/harvestbench | 2026-09-29 |
| 06_benchmark_anima_animalharmbench.md | ANIMA / AnimalHarmBench (AHB) | https://forum.effectivealtruism.org/posts/nBnRKpQ8rzHgFSJz9/animalharmbench-2-0-evaluating-llms-on-reasoning-about ; https://arxiv.org/html/2604.13076v1 ; https://github.com/UKGovernmentBEIS/inspect_evals/tree/main/src/inspect_evals/anima | 2026-09-29 |
| 07_benchmark_manta.md | MANTA multi-turn adversarial benchmark | https://arxiv.org/html/2605.16301 ; https://github.com/Mycelium-tools/manta | 2026-09-29 |
| 08_benchmark_manager_coercion_bench.md | Manager Coercion Bench (adjacent, not animal-specific) | https://github.com/CompassionML/manager-coercion-bench ; https://arxiv.org/abs/2607.15434 ; https://compassionbench.com/mcb | 2026-09-29 |
| 09_compassionbench_and_landscape.md | CompassionBench hub + full benchmark landscape table | https://compassionbench.com/ | 2026-09-29 |
| 11_falcon_fund_funder_context.md | Falcon Fund, Marcus Abramovitch, CaML, Sentient Futures, Anima International | https://manifund.org/projects/falcon-fund ; https://manifund.substack.com/p/fast-grants-for-ai-x-animals ; https://www.compassionml.com/ ; https://www.sentientfutures.ai/ | 2026-09-29 |
| 13_competition_watch.md | Search for competing constitution/model-spec/system-prompt text projects on Manifund/EA Forum/LessWrong | https://manifund.org/projects/edge-ai-stun-checks-and-an-ai-agent-benchmark ; https://animainternational.substack.com/p/animal-welfare-alignment-to-what ; https://animainternational.substack.com/p/animal-welfare-ai-fair-cop ; https://forum.effectivealtruism.org/posts/siYdAMNCzhLdWcEmr/ai-defaults-a-neglected-lever-for-animal-welfare | 2026-09-29 |
| GLOSSARY.md | Terminology: sentience, Five Freedoms/Domains, welfare vs rights, speciesism, moral circle, farmed/wild/companion/invertebrate, Constitutional AI | https://www.woah.org/en/what-we-do/animal-health-and-welfare/animal-welfare/ ; https://www.lse.ac.uk/news/news-assets/pdfs/2021/sentience-in-cephalopod-molluscs-and-decapod-crustaceans-final-report-november-2021.pdf ; https://en.wikipedia.org/wiki/Moral_circle_expansion | 2026-09-29 |

## Coverage gaps / open TODOs (see each file for detail)

- File 01: could not get a clean direct fetch of the primary Anthropic constitution PDF/page; quote
  is corroborated by 3+ independent secondary sources but should be re-verified against primary text.
- File 02: only the 2025-02-12 dated Model Spec version was confirmed to contain the animal example;
  2025-09-12 does not contain it; current/latest version not yet checked.
- File 03: absence-of-evidence only (search-level), not an exhaustive direct fetch of all four labs'
  safety docs.
- File 06: key percentage findings sourced from WebSearch summaries of the underlying paper, not yet
  independently re-verified against a direct fetch of arxiv 2604.13076's full text/tables.
- File 09: compassionbench.com homepage is JS-rendered and could not be read directly; sub-page
  existence for HarvestBench/ANIMA leaderboards not confirmed.
- File 13: the "AI Defaults" EA Forum post could not be directly fetched (JS rendering); resolved via
  WebSearch summary only, medium confidence.

## Rules followed while building this corpus

No invented quotes, numbers, or URLs. Bare URLs only (no tracking params, no redirect wrappers). No
em dashes (hyphens only). Every file states its access date and flags any content sourced from a
WebSearch summary versus a direct WebFetch of primary text.
