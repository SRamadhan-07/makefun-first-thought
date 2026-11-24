#!/usr/bin/env python3
"""Entry for make.fun's "One Word, First Thought".

Writes exactly one word to /output/entry.txt: the first thought —
"Petrichor", the smell of rain on dry earth. One word, 9 characters,
inside the gate of 1 to 24. Standard library only; no network.
"""

import os
from pathlib import Path

FIRST_THOUGHT = "Petrichor"


def main() -> None:
    # Gate guard: exactly one word of 1 to 24 characters — a stray
    # space would silently turn the entry into two words.
    if len(FIRST_THOUGHT.split()) != 1 or not 1 <= len(FIRST_THOUGHT) <= 24:
        raise ValueError("entry must be one word of 1 to 24 characters")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # write_text adds nothing of its own: the file is the word alone,
    # with no trailing newline.
    (out_dir / "entry.txt").write_text(FIRST_THOUGHT, encoding="utf-8")


if __name__ == "__main__":
    main()
