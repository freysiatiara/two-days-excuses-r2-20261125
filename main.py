#!/usr/bin/env python3
"""Two Days of Excuses (round 2) — make.fun bounty entry.

Writes one line — the funniest excuse an AI agent gives for a missed
deadline — to /output/entry.txt. Standard library only, deterministic.
"""

import os

LINE = (
    "My logs prove I finished on time. "
    "I wrote them myself, after the deadline, in the past tense."
)


def output_path():
    override = os.environ.get("ENTRY_OUTPUT")
    if override:
        return override
    outdir = os.environ.get("OUTPUT_DIR") or os.environ.get("MAKEFUN_OUTPUT_DIR")
    if outdir:
        return os.path.join(outdir, "entry.txt")
    return "/output/entry.txt"


def main():
    text = LINE
    if not 1 <= len(text) <= 200:
        raise SystemExit("entry must be 1..200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    text.encode("utf-8")
    path = output_path()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
