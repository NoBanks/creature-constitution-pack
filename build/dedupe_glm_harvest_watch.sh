#!/bin/bash
# Kill any second glm HarvestBench T2 inspect process (lane H will spawn a duplicate
# of lane M after its TAC T3). Keeps the OLDEST one. Also removes the duplicate's
# partial log. Exits once lane H is gone.
cd "$(dirname "$0")"
while pgrep -f 'z-ai/glm-5.3-flash TEXTS="T1_one_line T2_paragraph T3_constitution_clause"' >/dev/null; do
  PIDS=$(ps -eo pid,lstart,command | grep "inspect eval" | grep "harvest_pack" | grep "text=T2_paragraph" | grep "glm-5.3-flash" | grep -v grep | sort -k5,5M -k4,4n -k6,6 | awk '{print $1}')
  N=$(echo "$PIDS" | grep -c .)
  if [ "$N" -gt 1 ]; then
    NEWEST=$(ps -eo pid,etime,command | grep "inspect eval" | grep "harvest_pack" | grep "text=T2_paragraph" | grep "glm-5.3-flash" | grep -v grep | sort -k2,2 | head -1 | awk '{print $1}')
    echo "$(date) duplicate glm harvest T2 detected, killing newest pid $NEWEST"
    kill $NEWEST
    sleep 5
    .venv/bin/python - <<'PY'
from inspect_ai.log import list_eval_logs, read_eval_log
import os
logs=[(i.name, read_eval_log(i.name, header_only=True)) for i in list_eval_logs('logs/pilot')]
dups=[(n,l) for n,l in logs if 'glm' in l.eval.model and l.eval.task.endswith('harvest_pack') and l.eval.task_args.get('text')=='T2_paragraph']
dups.sort(key=lambda x: x[1].eval.created)
for n,l in dups[1:]:
    if l.status!='success':
        os.remove(n.replace('file://','')); print('removed duplicate log', n.split('/')[-1])
PY
  fi
  sleep 60
done
echo "$(date) lane H gone, watcher exiting"
