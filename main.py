#!/usr/bin/env python3
"""Write one satirical sentence about lawmakers who regulate AI, crypto or the internet but cannot convert a file to PDF, at most 320 characters, to /output/entry.txt.

The line is written exactly as given: 182 Unicode code points,
inside the competition gate of 1-320. Python 3, standard library
only, no network.
"""

import os

TEXT = "The senator who wrote the 400-page AI safety bill still emails his staff a Word document named FINAL-final-v2 and asks them to print it, sign it, scan it, and email it back as a PDF."

# The entry line, byte for byte: no trailing newline, nothing added or cut.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
