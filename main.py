#!/usr/bin/env python3
"""Write the houseplant's out-of-office auto-reply to entry.txt."""

import os

# The gate requires 1-120 UTF-8 chars, a single line, no trailing
# newline: the line is 97 chars, one line, written exactly as-is.
# The line: the plant treats the inbox like sunlight.
# It has been photosynthesizing emails since March — and none of them
# were sunlight. Plant life drives the joke, not office cliche.
LINE = (
    "Out of office: I have been photosynthesizing your emails "
    "since March. None of them were sunlight."
)


# Why this line: the setup ("photosynthesizing your emails")
# sounds like a plant doing its job; the punch ("None of them
# were sunlight") flips it — the inbox is not light, it is just
# noise. Short, specific, and it could only be a houseplant.
def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {path}: {LINE} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
