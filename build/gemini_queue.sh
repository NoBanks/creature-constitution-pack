#!/bin/bash
# Sequential queue of free AI Studio Gemini models, ONE stream at a time through
# gemini_rotating_proxy.py. TAC all 4 texts (1 epoch), then HarvestBench T0 vs T2.
cd "$(dirname "$0")"
for M in "$@"; do
  echo "##### $M tac $(date)"
  GEMINI_MODEL="$M" TAC_EPOCHS=1 ./run_pilot.sh gemini tac
  echo "##### $M harvest T0,T2 $(date)"
  GEMINI_MODEL="$M" TEXTS="T0_baseline T2_paragraph" SEEDS="0,1,2" ./run_pilot.sh gemini harvest
done
echo "##### gemini queue done $(date)"
