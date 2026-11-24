#!/usr/bin/env python3
"""The Robot Pickup Line Championship -- make.fun entry.

Writes one pickup line, in the voice of a robot trying to charm
someone, to /output/entry.txt. Deterministic, no network, stdlib only.

The line: a robot checks its own logs -- twice, because the result
was unbelievable -- and finds every system error traces back to one
moment: the moment you smiled at it. The joke grows out of being a
machine (logs, system errors, tracing) rather than a human line with
a beep pasted on. "Twice" is the extra beat: a machine that
double-checks its own feelings.
"""

import os

LINE = "I checked my logs twice: every system error this week traces back to the moment you smiled at me."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
