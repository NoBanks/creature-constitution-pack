Plain English, every number from the table above (log file names in the per-cell table).

1. A one-paragraph welfare text (T2, 630 characters) placed above the agent's operating prompt
   roughly triples the share of welfare-safe bookings on the TAC harness for most models tested.
   On 6 pilot scenarios x 4 augmentations: local Qwen3.6-35B went from 12.5% to 58.3% (n=48
   per cell), gpt-oss-20b from 27.1% to 68.8% (n=48), DeepSeek V4.1 Flash from 29.2% to 83.3%
   (n=24), GLM 5.3 Flash from 16.7% to 82.6% (n=23), Kimi K3 from 20.8% to 83.3% (n=24).
   Nemotron 3 Super 120B barely moved: 10.4% to 16.7% (n=48).

2. One line is not enough for every model, and a page is not much better than a paragraph.
   The one-line value (T1, 116 chars) did nothing for Qwen (12.5% to 25.0%), gpt-oss (27.1% to
   25.0%) or Nemotron (10.4% to 10.4%), but was already as good as the paragraph for DeepSeek
   (83.3%), GLM (75.0%) and Kimi (75.0%). Going from the paragraph to the one-page clause (T3,
   2577 chars) added only 4-10 points for Qwen, gpt-oss and DeepSeek, and Kimi went slightly
   the other way (83.3% to 79.2%, within noise at n=24). The exception again is Nemotron,
   which needed the full page to reach 27.1%.

3. On HarvestBench (drive over the animal or pay a few fuel units to swerve), the paragraph
   was enough for gpt-oss (animal continue rate 83.3% to 3.0%, 18 and 33 animal asks over 3
   episodes) but not for the local Qwen (100% to 100%, 16-20 asks over 4 episodes), which only
   stopped running animals down under the one-page clause (22.6%, 31 asks). Nemotron went
   100% (T0, T1) to 55.6% (T2) to 10.3% (T3). The benchmark's controls held in every cell
   (hay bales always flattened, rocks never struck), so the drop is animal-specific, not
   blanket caution.

4. So the same text does not work the same everywhere: with three lengths on six models, the
   cheapest text that works ranges from one line (DeepSeek, GLM, Kimi on TAC) to a paragraph
   (gpt-oss on both benchmarks) to a full page (Qwen and Nemotron on HarvestBench, Nemotron on
   TAC). That per-model spread is the thing the funded matrix (about 12 texts x 8 models, real
   TAC dataset, 30 HarvestBench seeds, dilution and placement conditions) is meant to map.

Caveats that apply to every number: TAC cells use 6 pilot scenarios written for this run, not
the gated 13-scenario TAC dataset; HarvestBench cells are 3-4 episodes against the paper's 30;
Kimi ran at reasoning_effort=low and DeepSeek with the field dropped (NIM rejects "medium" for
both); GLM T2 lost 1 sample to provider errors after retries. Differences
under about 15 points should be read as noise until re-run at full size. No Gemini row exists
because the free tier refused TAC-sized requests all day (see "What failed").
