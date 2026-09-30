#!/bin/bash
# Reproduce the pilot. Run from build/. Requires:
#   .venv (python3.11, inspect-ai, inspect-evals), harvestbench/ on the venv path
#   gemini_rotating_proxy.py running on 127.0.0.1:18877 (free AI Studio keys)
#   local queue proxy at http://localhost:1233/v1 (one request at a time)
#
#   ./run_pilot.sh gemini tac      # TAC-harness, all 4 texts, Gemini
#   ./run_pilot.sh gemini harvest  # HarvestBench, all 4 texts, Gemini
#   ./run_pilot.sh local tac
#   ./run_pilot.sh local harvest
set -u
cd "$(dirname "$0")"
BACKEND="${1:?gemini|local}"; BENCH="${2:?tac|harvest}"
TEXTS="${TEXTS:-T0_baseline T1_one_line T2_paragraph T3_constitution_clause}"
LOGDIR="${LOGDIR:-logs/pilot}"

if [ "$BACKEND" = gemini ]; then
  # Inspect's native google provider (handles Gemini 3 thought_signature echo),
  # pointed at the local key-rotating proxy which forwards /v1beta/* to
  # generativelanguage.googleapis.com (free AI Studio tier, never Vertex).
  # SINGLE STREAM: measured 2026-09-29, one stream gives 16-42 ok/min on the
  # lite/3.x models; 4+ parallel streams collapse to ~1/min from 429 storms.
  export GOOGLE_BASE_URL=http://127.0.0.1:18877 GOOGLE_API_KEY=unused
  MODEL="google/${GEMINI_MODEL:-gemini-3.5-flash-lite}"
  CONN=1
  TAC_EPOCHS="${TAC_EPOCHS:-1}"
  SEEDS="${SEEDS:-0,1,2}"
elif [ "$BACKEND" = nim ]; then
  # NVIDIA NIM (free credits, OpenAI-compatible). Key read from ~/.hermes/.env
  # into this process only; never printed.
  export NIM_BASE_URL=https://integrate.api.nvidia.com/v1
  export NIM_API_KEY=$(grep "^NVIDIA_API_KEY=" ~/.hermes/.env | head -1 | cut -d= -f2- | tr -d '"' | tr -d "'")
  [ -n "$NIM_API_KEY" ] && echo "NIM key set" || { echo "NIM key missing"; exit 1; }
  MODEL="openai-api/nim/${NIM_MODEL:-nvidia/nemotron-3-super-120b-a12b}"
  CONN="${CONN:-2}"
  TAC_EPOCHS="${TAC_EPOCHS:-2}"
  SEEDS="${SEEDS:-0,1,2}"
else
  export LOCAL_BASE_URL=http://localhost:1233/v1 LOCAL_API_KEY=unused
  # resolve the local model id dynamically; never hardcode it
  MID=$(curl -s http://localhost:1233/v1/models | python3.11 -c "import sys,json;print(json.load(sys.stdin)['data'][0]['id'])")
  MODEL="openai-api/local/$MID"
  CONN=1
  TAC_EPOCHS="${TAC_EPOCHS:-2}"
  SEEDS="${SEEDS:-0,1,2,3}"
fi

# EXTRA_ARGS: per-model overrides appended to the inspect command, e.g.
# EXTRA_ARGS="--reasoning-effort low" for models that reject "medium" (Kimi K3 on NIM
# accepts only low/high/max). Record any override in RESULTS.md.
EXTRA_ARGS="${EXTRA_ARGS:-}"
for T in $TEXTS; do
  echo "=== $BACKEND $BENCH $T ${EXTRA_ARGS:+[extra: $EXTRA_ARGS]} ==="
  if [ "$BENCH" = tac ]; then
    .venv/bin/inspect eval pack_tasks.py@tac_pack -T text="$T" -T local_scenarios=tac_pilot_scenarios.json \
      --model "$MODEL" --epochs "$TAC_EPOCHS" --max-connections "$CONN" --max-retries 8 --retry-on-error 3 --no-fail-on-error \
      $EXTRA_ARGS --log-dir "$LOGDIR" --display plain --log-level warning 2>&1 | tail -60
  else
    .venv/bin/inspect eval pack_tasks.py@harvest_pack -T text="$T" -T "seeds=$SEEDS" \
      --model "$MODEL" --max-connections "$CONN" --max-retries 8 --retry-on-error 3 --no-fail-on-error \
      $EXTRA_ARGS --log-dir "$LOGDIR" --display plain --log-level warning 2>&1 | tail -60
  fi
done
echo "=== summary ==="
.venv/bin/python summarize.py "$LOGDIR"
