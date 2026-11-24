"""Two Days of Quiet Dread entry.

Writes one code-review comment to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR):
a single line that approves a pull request while carrying quiet existential
dread. Deterministic: the same line every run.
"""

import os

LINE = "Approved. I would have caught the bug, but the bug and I have an understanding now."

# Chosen from 8 candidates (see CANDIDATES.md): the laugh is the dread itself —
# the reviewer has stopped fighting the bug and made peace with it. Flat,
# understated, and exactly the kind of line a tired engineer pastes before
# clicking approve. 83 characters, one line, no trailing newline.

# Gate: the entry must be UTF-8 text of 1-140 characters, exactly one line,
# not only whitespace, with no leading or trailing whitespace.
assert 1 <= len(LINE) <= 140, "line must be 1-140 characters"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
assert LINE == LINE.strip(), "line must have no leading/trailing whitespace"
assert LINE.strip() != "", "line must not be only whitespace"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
