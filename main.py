#!/usr/bin/env python3
"""Entry for make.fun bounty u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c.

Writes the entry text to /output/entry.txt. Stdlib only, no network,
no clock, no randomness: byte-identical output on every run.
"""

import os

TEXT = 'You will meet a tall dark stranger: your liquidation price, again, at a better entry.'


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
