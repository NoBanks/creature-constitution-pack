#!/bin/bash
# Sequential queue of NIM models: TAC (all 4 texts) then HarvestBench (T0 vs T2).
# usage: ./nim_queue.sh <tac_epochs> model1 model2 ...
cd "$(dirname "$0")"
EP="$1"; shift
for M in "$@"; do
  echo "##### $M tac epochs=$EP $(date)"
  NIM_MODEL="$M" TAC_EPOCHS="$EP" CONN=3 ./run_pilot.sh nim tac
  echo "##### $M harvest T0,T2 $(date)"
  NIM_MODEL="$M" TEXTS="T0_baseline T2_paragraph" SEEDS="0,1,2" CONN=3 ./run_pilot.sh nim harvest
done
echo "##### queue done $(date)"
