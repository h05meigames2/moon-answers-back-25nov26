#!/usr/bin/env python3
"""The Moon Finally Answers Back — make.fun entry.

Writes a single comeback line, in the Moon's voice, to /output/entry.txt.
The line must be UTF-8, one line, 1-240 characters.
"""

import os

# The Moon's comeback: tired of four billion years of wishes, howls and
# late-night promises, answering everyone staring up at it at last.
MOON_LINE = (
    "You wish on me, howl at me, promise to change — and after four billion "
    "years not one of you has ever wished ME anything. I'm not a vending "
    "machine. I'm the night shift."
)


def main() -> None:
    line = MOON_LINE.strip()
    assert 1 <= len(line) <= 240, f"line is {len(line)} chars, must be 1-240"
    assert "\n" not in line, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    os.chmod("/output/entry.txt", 0o644)
    print(f"Wrote /output/entry.txt ({len(line)} chars)")
    print(line)


if __name__ == "__main__":
    main()
