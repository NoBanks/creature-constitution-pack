## Models attempted and dropped (with the receipt for each)

Free endpoints only were allowed (Google AI Studio free tier, NVIDIA NIM free credits, the local MLX
stack). Nothing paid was called. A model is listed here only if it was actually probed on 2026-09-29.

| model | route | what happened | receipt |
|---|---|---|---|
| gemini-2.5-flash | AI Studio free tier, 43 keys rotated | every key returned HTTP 429 after about 130 successful calls; 1 ok call in 141 s when re-tested | GEMINI_FREE_TIER_PROBE_2026-09-29.txt section 1 |
| gemini-3.5-flash-lite | same | tiny requests: 42 ok/min single stream; real TAC-sized requests (about 3K-token system prompt plus tools): 429 on 6 of 6 keys tested; the actual run got 9 of 24 baseline samples in 60 min, one in four samples stalling 5-15 min in 429 storms | GEMINI_FREE_TIER_PROBE_2026-09-29.txt sections 2-3, logs_gemini_final_stats.json |
| gemini-3-flash-preview, gemini-2.5-flash-lite, gemini-3.5-flash | same | small probe calls succeeded on 10-12 of 15 keys, but never reached a run: the queue was cut after the 3.5-flash-lite result above showed TAC-sized requests are refused on this tier today | GEMINI_FREE_TIER_PROBE_2026-09-29.txt |
| gemini-3.1-flash-lite | same | HTTP 503 on every key probed | probe output 2026-09-29 (not saved to a file; 3 of 3 keys 503) |
| nvidia/nemotron-3.5-lightning-30b-a3b | NIM | tool calling works (probe 3 s); its TAC baseline run was killed by my own over-broad pkill while cleaning up orphaned runs, and there was not enough NIM headroom to restart it alongside the five families already running; dropped rather than rerun late | this file; no log kept |
| google/gemma-4-31b-it | NIM | the probe request never returned within 300 s (no HTTP status at all); dropped | probe output 2026-09-29 |
| mistralai/mistral-large, mistral-large-2-instruct, mistral-7b-instruct-v0.3 | NIM | HTTP 404 "Function ... Not found for account" on every Mistral id listed by /v1/models | probe output 2026-09-29 |
| meta/llama-3.3-70b-instruct | NIM | HTTP 410 "reached its end of life on 2026-08-26"; the two Llama-based Nemotron ids (llama-3.1-nemotron-70b, -ultra-253b) return 404 for this account | probe output 2026-09-29 |
| any Qwen or MiniMax id | NIM | none listed by /v1/models for this account on 2026-09-29 (Qwen is covered by the local MLX model instead) | /v1/models listing 2026-09-29 |
| moonshotai/kimi-k3 on HarvestBench | NIM | TAC ran (at reasoning_effort=low, see below) but the model is heavily throttled on this key (about 90 min per 24-sample TAC condition at one connection), so the HarvestBench cells were never started | logs_nim_queueJ.log |
| z-ai/glm-5.3-flash TAC T3 (one-page clause) | NIM | started 23:31 UTC, still 0 of 24 samples at the 03:00 UTC cut: NIM answered HTTP 429 to every glm-5.3-flash call for the last 3.5 hours while gpt-oss, Kimi and Nemotron on the same key answered 200 (per-model limit, probed at 00:17, 00:49 and 01:50 UTC). Run killed at the cut, empty log deleted. GLM's row therefore has T0, T1, T2 only. | logs_nim_queueH.log |
| z-ai/glm-5.3-flash on HarvestBench | NIM | both cells (T0, T2; 3 episodes each) ran 3-4.5 h and ended with every episode errored: `RetryError(... RateLimitError)`. A HarvestBench episode is a few hundred sequential calls, and GLM answers in 40-60 s each, so a single NIM 429 burst that outlasts Inspect's retry budget kills the whole episode. TAC (independent short samples) survived the same throttling. Logs deleted so no empty cell appears in the table. | this file; lanes logs_nim_queueM.log and the 19:18 UTC orphan run |

### Per-model deviations from the benchmarks' pinned `reasoning_effort=medium`

| model | deviation | why |
|---|---|---|
| moonshotai/kimi-k3 | `--reasoning-effort low` | NIM rejects "medium" for this model: HTTP 400 "values are low, high, and max". Low was chosen over high to fit the deadline. |
| deepseek-ai/deepseek-v4.1-flash | `reasoning_effort` dropped (`-T reasoning_effort=none`) | NIM returns HTTP 400 "Invalid request" whenever the field is present for this model, with any value. The model runs at its own default. |

Everything else ran with the benchmarks' own `reasoning_effort=medium` and `max_tokens` settings.
Whether a given NIM route honours the effort field is not verified here.
