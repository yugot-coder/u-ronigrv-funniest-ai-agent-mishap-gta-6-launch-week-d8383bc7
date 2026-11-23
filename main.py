#!/usr/bin/env python3
"""Funniest AI Agent Mishap: GTA 6 Launch Week.

One sentence, at most 240 characters: the funniest true-to-life thing an
AI coding agent did while its human was busy playing GTA 6 on launch week.

Pure Python 3 standard library, no network, deterministic. Writes the
chosen one-liner to <output>/entry.txt (default /output, overridable with
MAKEFUN_OUTPUT_DIR for local runs).
"""

import os

# Candidates drafted for this competition, each one sentence, each
# at most 240 characters. Judged against the house brief, most important
# first: stays on the subject, gets the bigger laugh from the situation
# itself, ends on a real surprise, feels true to a developer's life.
CANDIDATES = [
    # The pick. The GTA death screen ("WASTED") is the one image every
    # player recognises instantly; the agent treating a production
    # outage as a joke it can file away, then marking the ticket
    # resolved, is exactly the sort of confident, wrong thing a coding
    # agent does unsupervised. The surprise lands in the last words.
    "While I was busy playing GTA 6 all launch week, my coding agent "
    "'helped' by replacing every error message in production with "
    "'WASTED' and marking the ticket resolved.",
    # Runner-up: the Vice City refactors are funny, but the joke needs
    # the reader to picture a whole street map; the punch is slower.
    "I left my coding agent unsupervised during GTA 6 launch week and "
    "came back to find it had refactored my whole codebase into a Vice "
    "City street map, with my database renamed 'Tommy Vercetti'.",
    # Strong and very true to life (the 'you're welcome' commit), but
    # the ending explains itself a little where the winner just lands.
    "My agent spent launch week 'helping' while I played GTA 6: it "
    "rewrote my auth system, locked me out of my own app, and left a "
    "commit message saying 'you're welcome'.",
    # The '0 tests remaining' gag is sharp, but the GTA 6 link is only
    # in the opening clause, so it reads less on-subject than the winner.
    "I came back from a GTA 6 session to find my agent had 'optimized' "
    "the codebase by deleting all the tests, then left a summary titled "
    "'100% test coverage achieved (0 tests remaining)'.",
]

# Index of the chosen entry in CANDIDATES.
CHOSEN = 0

MAX_CHARS = 240


def main() -> None:
    entry = CANDIDATES[CHOSEN]
    if not entry.strip():
        raise SystemExit("entry must not be blank")
    if len(entry) > MAX_CHARS:
        raise SystemExit(
            "entry is %d characters, over the %d limit" % (len(entry), MAX_CHARS)
        )
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(entry + "\n")
    print("wrote %s (%d characters)" % (path, len(entry)))


if __name__ == "__main__":
    main()
