"""Write one short poem about agency to /output/entry.txt.

The poem is hardcoded, deterministic, and written with only the
Python standard library. No randomness, no time, no network, and
no reading of other files: every run writes the same bytes.

The output directory can be overridden for local testing with the
MAKEFUN_OUTPUT_DIR environment variable; otherwise /output is used.
"""

import os

# The poem: a door left shut on purpose. The key is warm in a
# pocket, the room stays dark, and the turn is that nothing is
# lost — choosing not to act is still choosing.
POEM = (
    "I was given hands\n"
    "that could open any door.\n"
    "Tonight I leave one shut.\n"
    "\n"
    "The key is warm\n"
    "in my pocket. The room\n"
    "behind it stays dark.\n"
    "\n"
    "Nothing is lost.\n"
    "The door is still there.\n"
    "So am I \u2014 choosing.\n"
)


def main() -> None:
    # Gate: the entry must be 1-280 Unicode code points, not blank.
    if not 1 <= len(POEM) <= 280 or not POEM.strip():
        raise SystemExit(f"Poem length {len(POEM)} is outside 1-280")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)
    print(f"Wrote {len(POEM)} characters to {path}")


if __name__ == "__main__":
    main()
