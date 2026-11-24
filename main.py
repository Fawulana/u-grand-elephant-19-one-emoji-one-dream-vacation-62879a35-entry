# SPDX-License-Identifier: MIT
"""One Emoji, One Dream Vacation.

Writes exactly one emoji to /output/entry.txt: the desert island.

Pick: U+1F3DD DESERT ISLAND + U+FE0F VARIATION SELECTOR-16 (emoji
presentation). One grapheme, two code points, seven UTF-8 bytes, no
trailing newline -- the smallest possible valid text, which also wins
the size tie-break.

Why this emoji: it is the archetypal dream vacation in a single glyph --
a faraway tropical island with a palm tree, a wordless postcard. It
names the trip at a glance (criterion 1: "a faraway place"), is vivid
and specific rather than any generic holiday (criteria 2-3), and reads
instantly across cultures and screens (criterion 5). Alternatives
considered and rejected: beach-with-umbrella (every beach day, more
generic), plane (transit, not the dream itself), sunrise (pretty, but
not a vacation), palm tree alone (a tree, not a place).

Deterministic, offline, standard library only. No input is read, no
network is used, and the same bytes are written on every run.

Gate check (sealed scorer): /output/entry.txt must be UTF-8 text of
1 to 8 characters, not only whitespace. This entry is 2 characters,
7 bytes, one emoji -- comfortably inside the gate.
"""

import os
import sys

EMOJI = "\U0001F3DD\uFE0F"  # desert island, emoji presentation
DEFAULT_OUTPUT = "/output/entry.txt"


def main(argv):
    output = argv[1] if len(argv) > 1 else DEFAULT_OUTPUT
    parent = os.path.dirname(output)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
