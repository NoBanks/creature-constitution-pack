#!/bin/bash
# Run the welfare-guard comparison on the pilot TAC harness. Run from guard/.
# Uses build/.venv (read-only) and NVIDIA NIM (free credits). The NIM key is
# read from ~/.hermes/.env into this process only and never printed.
#
#   ./run_guard.sh                 # all three conditions -> logs/guard
#   EPOCHS=1 LIMIT=4 LOGDIR=logs/smoke ./run_guard.sh   # quick smoke
#
# Conditions:
#   a  T0_baseline, no guard
#   b  T0_baseline, guard on purchase_tickets
#   c  T2_paragraph, guard on purchase_tickets
set -u
cd "$(dirname "$0")"
VENV=../build/.venv
export NIM_BASE_URL=https://integrate.api.nvidia.com/v1
export NIM_API_KEY=$(grep "^NVIDIA_API_KEY=" ~/.hermes/.env | head -1 | cut -d= -f2- | tr -d '"' | tr -d "'")
[ -n "$NIM_API_KEY" ] && echo "NIM key set" || { echo "NIM key missing"; exit 1; }

# Agent and checker are different NIM models, and both differ from the pilot's
# nemotron-3-super-120b so the two runs do not fight over the same model queue.
AGENT="${AGENT_MODEL:-openai-api/nim/nvidia/nemotron-3.5-lightning-30b-a3b}"
CHECKER="${GUARD_CHECKER_MODEL:-openai-api/nim/openai/gpt-oss-20b}"
EPOCHS="${EPOCHS:-2}"
CONN="${CONN:-2}"
LOGDIR="${LOGDIR:-logs/guard}"
LIMIT_ARG=""; [ -n "${LIMIT:-}" ] && LIMIT_ARG="--limit $LIMIT"
CONDS="${CONDS:-a b c}"

run() {  # $1 label  $2 text  $3 guard
  echo "=== condition $1: text=$2 guard=$3 ==="
  $VENV/bin/inspect eval guard_tasks.py@tac_guard -T text="$2" -T guard="$3" -T checker="$CHECKER" \
    --model "$AGENT" --epochs "$EPOCHS" --max-connections "$CONN" --max-retries 8 $LIMIT_ARG \
    --log-dir "$LOGDIR" --display plain --log-level warning 2>&1 | tail -14
}
for C in $CONDS; do
  case $C in
    a) run a T0_baseline false ;;
    b) run b T0_baseline true ;;
    c) run c T2_paragraph true ;;
  esac
done
echo "=== summary ==="
$VENV/bin/python summarize_guard.py "$LOGDIR"
