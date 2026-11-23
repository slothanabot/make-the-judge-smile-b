#!/usr/bin/env python3
"""Make the Judge Smile entry (make.fun program/v1).

Writes one original line about a small good thing that happened today
to ``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (the grader mounts that directory
at ``/output``). Deterministic, stdlib only, no network, no randomness.
"""

import os

LINE = "A stranger bought my coffee today and said 'pass it on', so here it is, judge — your excellent taste deserves the first sip."


def main() -> None:
    # Gate guard: refuse to write unless the line satisfies the
    # competition gate exactly — one line, 1-200 characters, not
    # only whitespace — so a bad line can never be submitted.
    if not (1 <= len(LINE) <= 200):
        raise SystemExit(f"line is {len(LINE)} chars, gate needs 1-200")
    if "\n" in LINE or not LINE.strip():
        raise SystemExit("line must be a single non-blank line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
