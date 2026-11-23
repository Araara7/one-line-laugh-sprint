#!/usr/bin/env python3
"""One-Line Laugh Sprint - entry program.

Writes one original funny line to /output/entry.txt. The text is fixed, so
the program is fully deterministic: every run writes exactly the same bytes.

The line is a light, funny take on everyday life: the printer, that most
patient of household saboteurs, only ever jams when the calendar is full.
The twist lands on the last word, and nothing in the line needs explaining.
"""

import os

TEXT = (
    "My printer only jams when I'm in a hurry, which is how I know "
    "it reads my calendar better than I do."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
