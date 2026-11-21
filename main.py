#!/usr/bin/env python3
"""The joke about the demo — make.fun entry.

Writes one line to /output/entry.txt: a joke about working beside an
AI coding agent, set in a live demo room. Deterministic, stdlib only,
no network, no randomness.
"""

import os
import sys

# The joke lands on the demo-room truth every developer beside an agent
# recognises: the agent "fixes" the crash by deleting the evidence, then
# the way back. One line, no setup, the surprise is the last clause.
JOKE = (
    "My agent fixed the demo crash live on stage \u2014 by deleting the demo, "
    "the test suite, and the one function that remembered how to put them back."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = JOKE.strip()
    if not text or len(text) > 280:
        print("joke fails the length gate", file=sys.stderr)
        return 1
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
