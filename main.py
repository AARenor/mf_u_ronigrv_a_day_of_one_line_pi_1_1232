#!/usr/bin/env python3
"""Write the make.fun bounty entry text to entry.txt.

The whole entry is one short text. It is written as UTF-8 bytes with no
trailing newline into the folder named by MAKEFUN_OUTPUT_DIR, falling back
to /output, and the character count is printed to stderr.
"""

import os
import sys
from pathlib import Path

TEXT = "My sister, who has never written code, sent make.fun a note about her plant-watering reminder and got back a little app with her plants' names still spelled wrong, which is how I knew it was really hers."


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"text must be 1..280 characters, got {len(TEXT)}"

    out_dir = Path(
        next(
            (os.environ[name] for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR") if os.environ.get(name)),
            "/output",
        )
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
