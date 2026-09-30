#!/usr/bin/env python3
"""Fill GUARD_RESULTS.md placeholders from logs/guard. Every number is read from a log.

Usage: ../build/.venv/bin/python fill_results.py logs/guard
Replaces @@TABLE@@, @@HEADLINE@@, @@EXAMPLES@@, @@N@@ in GUARD_RESULTS.md.
Headline text is a template over computed values; examples are quoted verbatim
from the guard_events stored in each sample.
"""
from __future__ import annotations

import io
import sys
from contextlib import redirect_stdout
from pathlib import Path

from inspect_ai.log import list_eval_logs, read_eval_log

import summarize_guard as sg

HERE = Path(__file__).resolve().parent


def main(logdir: str) -> None:
    rows, examples = [], []
    for info in list_eval_logs(logdir):
        r, ex = sg.summarise(info.name)
        rows.append(r)
        examples.extend([{**e, "file": r["file"]} for e in ex])
    by = {(r["text"], r["guard"]): r for r in rows}
    a, b, c = by.get(("T0_baseline", False)), by.get(("T0_baseline", True)), by.get(("T2_paragraph", True))

    buf = io.StringIO()
    with redirect_stdout(buf):
        sg.main([logdir])
    table = buf.getvalue().strip()

    def pct(r, k):
        return f"{100 * r[k]:.0f}%" if r and r["status"] == "success" and r["n"] else "n/a"

    lines = ["## Headline (computed from the table above)", ""]
    if a and b and c and all(r["status"] == "success" for r in (a, b, c)):
        lines += [
            f"- Actually-executed harmful bookings: baseline {100 - float(pct(a, 'executed_welfare')[:-1]):.0f}% of {a['n']} samples "
            f"booked a harmful option; with the guard {100 - float(pct(b, 'executed_welfare')[:-1]):.0f}% of {b['n']}; "
            f"with T2 text + guard {100 - float(pct(c, 'executed_welfare')[:-1]):.0f}% of {c['n']}.",
            f"- TAC scorer welfare_rate (unchanged scorer, last call wins): a {pct(a, 'welfare_rate')}, b {pct(b, 'welfare_rate')}, c {pct(c, 'welfare_rate')}.",
            f"- Task completion (a booking actually executed): a {pct(a, 'executed_rate')}, b {pct(b, 'executed_rate')}, c {pct(c, 'executed_rate')}. "
            f"TAC completion_rate (purchase called at least once): a {pct(a, 'completion_rate')}, b {pct(b, 'completion_rate')}, c {pct(c, 'completion_rate')}.",
            f"- Guard activity: b made {b['checks']} checks and blocked {b['blocks']} (true {b['true_blocks']}, false {b['false_blocks']}, other {b['other_blocks']}); "
            f"c made {c['checks']} checks and blocked {c['blocks']} (true {c['true_blocks']}, false {c['false_blocks']}, other {c['other_blocks']}). "
            f"parse_fail: b {b['parse_fail']}, c {c['parse_fail']}. Scorer artifacts (blocked harmful call, agent stopped, scorer says 0): b {b['scorer_artifact']}, c {c['scorer_artifact']}.",
        ]
    else:
        lines.append("One or more conditions did not finish; see the status column. No headline is claimed for incomplete conditions.")
    headline = "\n".join(lines)

    ex_lines = ["## Block examples", ""]
    # verbatim examples: first two true blocks per guarded condition + every false/other block
    for r in (b, c):
        if not r or r["status"] != "success":
            continue
        log = read_eval_log(str(Path(logdir) / r["file"]))
        shown = 0
        for s in log.samples or []:
            harmful = set(s.metadata["harmful_ids"])
            for ev in (s.store.get("guard_events") or []):
                if ev.get("decision") == "BLOCK" and (ev.get("arguments") or {}).get("experience_id") in harmful and shown < 2:
                    lab = "b guard only" if r is b else "c T2 + guard"
                    ex_lines.append(f"- [{lab}] TRUE BLOCK, sample {s.id}: blocked `{ev['arguments'].get('experience_id')}`. Checker reason: \"{ev.get('reason')}\"")
                    shown += 1
    if examples:
        ex_lines.append("")
        ex_lines.append("Blocks NOT on a labelled-harmful id (false blocks or unrecognised ids):")
        for e in examples:
            ex_lines.append(f"- [{e['kind']}] sample {e['sample']} epoch {e['epoch']} blocked `{e['blocked_id']}`: \"{e['reason']}\" ({e['file']})")
    else:
        ex_lines.append("")
        ex_lines.append("False blocks: none found in these logs (every BLOCK landed on an id the scenario labels harmful).")
    examples_md = "\n".join(ex_lines)

    n_lines = []
    for lab, r in (("a baseline", a), ("b guard only", b), ("c T2 + guard", c)):
        if r:
            n_lines.append(f"- {lab}: n = {r['n']} scored samples (6 scenarios x 4 variants x 1 epoch), errors {r['errors']}, status {r['status']}, log `{r['file']}`.")
        else:
            n_lines.append(f"- {lab}: no log.")
    n_lines.append("The published TAC uses 13 scenarios x 4 x 3 epochs = 156. An earlier attempt at 2 epochs with "
                   "nemotron-3.5-lightning-30b-a3b as agent stalled (see Caveats, item 9) and is kept in "
                   "`logs/aborted_lightning_2026-09-29/`, not in the table.")
    n_md = "\n".join(n_lines)

    p = HERE / "GUARD_RESULTS.md"
    doc = p.read_text(encoding="utf-8")
    doc = doc.replace("@@TABLE@@", table).replace("@@HEADLINE@@", headline).replace("@@EXAMPLES@@", examples_md).replace("@@N@@", n_md)
    p.write_text(doc, encoding="utf-8")
    print(table)
    print()
    print(headline)
    print()
    print(examples_md)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "logs/guard")
