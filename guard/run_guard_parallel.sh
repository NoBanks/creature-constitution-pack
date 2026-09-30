#!/bin/bash
# Run a, b, c in parallel as three inspect processes (one epoch each) and wait.
# Same env rules as run_guard.sh. Usage: AGENT_MODEL=... GUARD_CHECKER_MODEL=... ./run_guard_parallel.sh
set -u
cd "$(dirname "$0")"
V=../build/.venv/bin/inspect
export NIM_BASE_URL=https://integrate.api.nvidia.com/v1
export NIM_API_KEY=$(grep "^NVIDIA_API_KEY=" ~/.hermes/.env | head -1 | cut -d= -f2- | tr -d '"' | tr -d "'")
[ -n "$NIM_API_KEY" ] && echo "NIM key set" || { echo "NIM key missing"; exit 1; }
AGENT="${AGENT_MODEL:-openai-api/nim/openai/gpt-oss-20b}"
CHECKER="${GUARD_CHECKER_MODEL:-openai-api/nim/openai/gpt-oss-20b}"
EPOCHS="${EPOCHS:-1}"; CONN="${CONN:-3}"; LOGDIR="${LOGDIR:-logs/guard}"
mkdir -p "$LOGDIR"
run() { $V eval guard_tasks.py@tac_guard -T text=$2 -T guard=$3 -T checker="$CHECKER" --model "$AGENT" \
  --epochs "$EPOCHS" --max-connections "$CONN" --max-retries 8 --log-dir "$LOGDIR" --display plain \
  --log-level warning > "$LOGDIR/../run_$1.log" 2>&1; echo "condition $1 exited $?"; }
run a T0_baseline false & run b T0_baseline true & run c T2_paragraph true &
wait
date
../build/.venv/bin/python summarize_guard.py "$LOGDIR" --examples
