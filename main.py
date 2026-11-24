#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Writes one brutally honest line: the error message an AI agent prints
the instant it breaks production.
"""

import os
import shutil
import sys

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
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Self-check the gate before reporting success: the file must be
    # UTF-8 text of 1 to 200 characters, a single line, not only
    # white space. Fail loudly instead of shipping a bad entry.
    with open(entry_path, "r", encoding="utf-8") as f:
        text = f.read()
    body = text[:-1] if text.endswith("\n") else text
    if not 1 <= len(text) <= 200 or "\n" in body or not body.strip():
        print(f"entry.txt failed the gate: {len(text)} chars", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
