#!/usr/bin/env python3
"""One-Line Laugh Sprint - entry program.

Writes one original funny line to /output/entry.txt. The text is fixed, so
the program is fully deterministic: every run writes exactly the same bytes.
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
