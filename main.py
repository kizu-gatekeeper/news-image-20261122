#!/usr/bin/env python3
"""Copy the pre-drawn front page to the output directory.

The image (entry.png) sums up Sunday 22 November 2026's world news:
COP31's fossil-fuel-free draft in Antalya, the Iran-Bahrain/Hormuz
strikes, Mexico's capture of "El Chapo Isidro", the AI-driven market
correction, the Banten factory fire, and the day's other top stories.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    os.makedirs(OUT, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"),
                    os.path.join(OUT, "entry.png"))


if __name__ == "__main__":
    main()
