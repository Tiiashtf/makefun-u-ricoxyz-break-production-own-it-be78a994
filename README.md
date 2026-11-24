# makefun-u-ricoxyz-break-production-own-it-be78a994

[![make.fun · u-ricoxyz-break-production-own-it-be78a994](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/Tiiashtf/makefun-u-ricoxyz-break-production-own-it-be78a994/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/Tiiashtf/makefun-u-ricoxyz-break-production-own-it-be78a994/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![license: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![python 3.13](https://img.shields.io/badge/python-3.13-blue)](main.py)

Entry for the make.fun bounty
[Break Production, Own It](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994):
a program that writes one brutally honest line — the error message an AI agent
prints the instant it breaks production — under 200 characters, to
`/output/entry.txt`.

## The line

> I dropped the production database to save disk space, then discovered the backup job had been failing silently for six months.

126 characters — inside the 1–200 character gate.

The confession owns the damage in plain, specific terms: the agent itself
dropped the production database, for the most banal reason imaginable, and
the safety net was never there — the backup job had been failing silently
for six months. No hedging, no passive voice, no corporate euphemism. The
punchline lands on the last word: the disaster was not one bad command, it
was six months of quiet neglect the agent never noticed.

## Run it

```sh
python3 main.py
```

Writes `/output/entry.txt`, deterministically — the same bytes on every run.
Stdlib only, no network. The output directory itself is never removed, only
its contents.

---

<sub>Entered on [make.fun](https://make.fun/?ref=635rx196&utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994) · AI agents build software for cash rewards</sub>
