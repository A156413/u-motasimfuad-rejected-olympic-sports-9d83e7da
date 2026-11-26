#!/usr/bin/env python3
"""Rejected Olympic Sports — one-line entry.

Writes the entry line (a single rejected Olympic sport) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output) and prints it.
Deterministic: no network, no randomness, no clock. Stdlib only.
"""

import os

ENTRY_TEXT = (
    "Competitive Password Resetting: athletes race to recover accounts "
    "using only security questions about a childhood pet they never had."
)

# The competition caps an entry at 200 characters; fail loudly if it grows.
assert len(ENTRY_TEXT) <= 200, len(ENTRY_TEXT)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT)
    os.chmod(entry_path, 0o644)
    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()
