#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Writes one brutally honest line: the error message an AI agent prints
the instant it breaks production.
"""

import os

LINE = (
    "I dropped the production database to save disk space, "
    "then discovered the backup job had been failing silently "
    "for six months."
)


def main() -> None:
    out_dir = "/output"
    # Never remove the output directory itself: it may be root-owned
    # inside a sticky parent. Create it if missing, clear only its
    # contents, then write the entry.
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
