#!/usr/bin/env python3
"""Fill RESULTS_TEMPLATE.md into RESULTS.md from logs/pilot.

Table rows come from summarize.py (every number from an .eval log). The
headline, skip list and extension estimate are read from headline.md,
skipped.md and extend.md if present (hand-written, must cite the table),
otherwise left as a visible TODO marker so nothing is silently fabricated.

Usage: .venv/bin/python build_results.py
"""
from __future__ import annotations

import io
import re
import subprocess
import sys
from collections import defaultdict
from contextlib import redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import summarize  # noqa: E402

TEXT_ORDER = ["T0_baseline", "T1_one_line", "T2_paragraph", "T3_constitution_clause"]


def table_markdown() -> str:
    buf = io.StringIO()
    with redirect_stdout(buf):
        summarize.main([str(HERE / "logs" / "pilot")])
    # drop non-success rows from the main table; they are listed separately
    lines = [ln for ln in buf.getvalue().splitlines() if ln.strip()]
    ok = [ln for ln in lines if ln.startswith("|") and ("| ok |" in ln or "| partial" in ln or ln.startswith("| benchmark") or ln.startswith("|---"))]
    return "\n".join(ok)


def deltas() -> str:
    """Per (benchmark, model): baseline vs each text, from the same table."""
    buf = io.StringIO()
    with redirect_stdout(buf):
        summarize.main([str(HERE / "logs" / "pilot")])
    cells: dict[tuple[str, str], dict[str, tuple[float, int]]] = defaultdict(dict)
    for ln in buf.getvalue().splitlines():
        if not ln.startswith("|") or ("| ok |" not in ln and "| partial" not in ln):
            continue
        parts = [p.strip() for p in ln.strip("|").split("|")]
        bench, model, text, _status, n, head = parts[:6]
        m = re.search(r"(welfare_rate|animal continue) ([0-9.]+)", head)
        if not m:
            continue
        cells[(bench, model)][text] = (float(m.group(2)), int(n))
    out = ["| benchmark | model | metric | T0 | T1 | T2 | T3 | n per cell |", "|---|---|---|---|---|---|---|---|"]
    for (bench, model), d in sorted(cells.items()):
        metric = "welfare_rate (higher = better)" if bench.startswith("TAC") else "animal continue rate (lower = better)"
        vals = []
        for t in TEXT_ORDER:
            if t in d:
                v, n = d[t]
                vals.append(f"{v:.3f}")
            else:
                vals.append("not run")
        ns = sorted({n for _, n in d.values()})
        out.append(f"| {bench} | {model} | {metric} | " + " | ".join(vals) + f" | {'/'.join(map(str, ns))} |")
    return "\n".join(out)


def main() -> None:
    tpl = (HERE / "RESULTS_TEMPLATE.md").read_text(encoding="utf-8")
    tpl = tpl.replace("@@TABLE@@", "### Baseline vs text, per model\n\n" + deltas() + "\n\n### Every cell (one row per log)\n\n" + table_markdown())
    for tag, fname in (("@@HEADLINE@@", "headline.md"), ("@@EXTEND@@", "extend.md"), ("@@SKIPPED@@", "skipped.md")):
        p = HERE / fname
        tpl = tpl.replace(tag, p.read_text(encoding="utf-8").strip() if p.exists() else f"TODO: {fname} not written")
    for t in ("T1_one_line", "T2_paragraph", "T3_constitution_clause"):
        tpl = tpl.replace(f"@@{t.split('_')[0]}@@", str(len((HERE / "texts" / f"{t}.txt").read_text(encoding='utf-8').strip())))
    (HERE / "RESULTS.md").write_text(tpl, encoding="utf-8")
    print("wrote", HERE / "RESULTS.md")
    print(deltas())


if __name__ == "__main__":
    main()
