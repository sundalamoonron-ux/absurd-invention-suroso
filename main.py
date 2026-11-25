#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch — make.fun entry.

Event: u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a.
Writes the chosen pitch to /output/entry.txt.

The pitch (C5, winner of the in-session pairwise audit 5-0, undefeated):
an apologetic printer — it prints one perfect page and a tiny apology note
before jamming, so you forgive it instead of threatening it with the window.
Decider: C5 beat the other undefeated candidate C9 (router, 4-0) head-to-head
and runner-up C10 (toothpaste) in the final; see candidates.md games 13, 18.
"""

import os

PITCH = (
    "A printer that prints one perfect page and a tiny apology note "
    "before jamming, so you forgive it instead of threatening it "
    "with the window."
)


MAX_CHARS = 220  # gate from RULES.txt: /output/entry.txt must be 1-220 UTF-8 chars


def validate(text: str) -> None:
    """Enforce the competition gate before writing: one sentence, 1-220 chars.

    A single sentence means exactly one sentence terminator (a period) and no
    other sentence-ending punctuation; the text must not be only whitespace.
    """
    if not text or not text.strip():
        raise ValueError("pitch must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("pitch must be a single line (no embedded newlines)")
    if len(text) > MAX_CHARS:
        raise ValueError(f"pitch is {len(text)} chars, over the {MAX_CHARS} limit")
    if text.count(".") != 1 or not text.rstrip().endswith("."):
        raise ValueError("pitch must be exactly one sentence ending in a period")
    if "?" in text or "!" in text:
        raise ValueError("pitch must be exactly one sentence (no ? or !)")


def main() -> None:
    validate(PITCH)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
