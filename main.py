"""The Screen Door Still Bangs — exactly one nostalgic sentence.

A childhood memory built on two smells — fried rice and rain on hot
concrete — and one sound, the screen door. The ache is in the second
half: twenty years later, the narrator still listens for a door that
no longer bangs, so the memory is not just recalled, it is waited for.

Prints the sentence to stdout and writes the exact same sentence,
with no trailing newline, to /output/entry.txt. Standard library
only, no network access, no files read — the sentence is a constant
in this file. The 280-character gate is checked on every run so an
over-long edit can never slip through silently. One sentence, one
memory, no greeting-card sentiment — just the kitchen, the rain,
and a door that still bangs in the narrator's head.
"""

import os
import sys

LINE = (
    "Grandma's kitchen smelled of fried rice and rain on hot concrete, "
    "and twenty years later I still listen for the screen door banging "
    "behind me when I come home."
)


def main() -> int:
    if not 1 <= len(LINE) <= 280:
        print(f"error: line is {len(LINE)} chars, must be 1-280",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
