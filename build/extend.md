Target for the funded project: about 12 texts x 8 models on TAC (real gated dataset, 156 samples
per cell as published) and HarvestBench (30 seeds at k=12 as published), plus the dilution and
placement conditions. That is 96 (text, model) cells per benchmark before extra conditions.

Per-cell timings measured in this pilot (smaller cells: TAC 24-48 samples, HarvestBench 3-4 episodes):

| model | TAC per condition (n) | HarvestBench per condition (episodes) | source |
|---|---|---|---|
| local Qwen3.6-35B-A3B-5bit, one request at a time | 8-9 min (48) | 5 min (4) | logs_local.log timestamps |
| NIM gpt-oss-20b | 7 min (48) | 10 min (3) | logs_nim_queueB.log, logs_nim_queueI.log |
| NIM nemotron-3-super-120b | 40-65 min (48), heavily rate-limited while 5 lanes shared one key | 8 min (3) | logs_nim_tac.log, logs_nim_harvest.log, logs_nim_queueE.log |
| NIM deepseek-v4.1-flash | 35 min (24) | not run | logs_nim_queueK.log |
| NIM glm-5.3-flash | 90 min (24) | over 2 h for 3 episodes (calls inside an episode are sequential) | logs_nim_queueH.log, logs_nim_queueM.log |
| NIM kimi-k3 (effort low) | 90 min (24), one connection | not run | logs_nim_queueJ.log |

Scaling those to the published cell sizes (TAC x3.3 to x6.5, HarvestBench x7.5 to x10):

- Local open-weight model: about 30 min TAC + 40 min HarvestBench = roughly 70 min per text, so
  12 texts is about 14 h of unattended machine time per local model, at $0. Two local models
  (e.g. the Qwen3.6 MoE plus a dense 27B) is about 28 h; they must run one at a time on the Mac.
- API models: 96 cells x (30-60 min TAC + 30-90 min HarvestBench). With 4-6 lanes in parallel
  on properly provisioned keys (not the free tiers used today), about 2-4 days of wall time for
  the whole matrix, plus one day for reruns of cells that error out (this pilot needed retries
  on 3 of 6 NIM models for provider quirks: empty `choices`, rejected `reasoning_effort`).

Token volume and cost. A TAC sample is about 5 model calls at roughly 4-5K tokens each
(pilot logs show 7-15K tokens per 2 samples), so a 156-sample cell is about 3.5M tokens.
A HarvestBench episode is 100-160 calls at about 2K tokens, so a 30-seed cell is about 9M tokens.
Call it 12-13M tokens per (text, model) cell, or about 1.2B tokens for 96 cells.

- On flash-class models (Gemini Flash, GPT mini, DeepSeek, open-weight via NIM/OpenRouter),
  blended around $0.5-1.5 per million tokens: roughly $600-1,800 for the matrix.
- On top-tier models (Claude Opus/Sonnet class, GPT-5 class), blended $3-15 per million:
  roughly $3,600-15,000 if every one of the 8 models were top-tier.
- A realistic panel (2 local, 3 flash-class, 3 top-tier) lands around $2,500-6,000, which is
  why the proposal budgets $4K for API/compute and treats the pilot as the calibration.

Adding the dilution and placement conditions multiplies the API line by about 2-3x; the local
lanes absorb most of that at $0 if the matrix is scheduled overnight.

What this pilot could not price: Gemini. The AI Studio free tier refused TAC-sized requests on
every key today (see skipped list); paid Gemini quota would be needed for those rows and would
sit in the flash-class cost band.
