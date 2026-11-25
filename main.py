#!/usr/bin/env python3
"""Fortune-cookie entry: one line for a freshly liquidated trader.

Running this file writes the fortune text into entry.txt inside the
output folder named by MAKEFUN_OUTPUT_DIR (default /output). Only the
standard library is used, and the bytes written never change between
runs: no clock, no randomness, no network.
"""

from pathlib import Path
import os

FORTUNE = "You will meet a tall dark stranger: your liquidation price, again, at a better entry."
ENTRY_NAME = "entry.txt"


def output_folder() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def write_fortune() -> None:
    folder = output_folder()
    folder.mkdir(parents=True, exist_ok=True)
    (folder / ENTRY_NAME).write_text(FORTUNE, encoding="utf-8", newline="")


if __name__ == "__main__":
    write_fortune()
