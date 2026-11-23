"""make.fun entry: news-image-20261122, version 4.

The entry is a single front-page image of Sunday 22 November 2026's
world news (entry.png, drawn by gen.py). This program only copies that
image into the output directory the grader names, so it needs nothing
beyond the standard library.
"""

import os
import shutil
import sys


def output_dir():
    """Where the grader wants the image: $MAKEFUN_OUTPUT_DIR or /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    # The copy is byte for byte, so two runs write identical bytes.
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    # Empty the directory's contents only; the directory itself is a
    # mount point and must never be removed.
    for name in os.listdir(out):
        path = os.path.join(out, name)
        if os.path.isfile(path):
            os.remove(path)
    shutil.copyfile(src, os.path.join(out, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
