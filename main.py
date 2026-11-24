"""One word, one username, one reward — the whole entry.

The bounty wants a single word and nothing attached to it: no pitch,
no link, no explanation. So this script writes our own make.fun
username, ``serauis``, as that lone word, byte for byte.
"""

import os

USERNAME = "serauis"
MAX_LEN = 30


def save_word(path, word):
    """Save one word to ``path`` with no trailing newline."""
    assert word and " " not in word and "\t" not in word, \
        "entry must be exactly one word"
    assert 1 <= len(word) <= MAX_LEN
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(word)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.txt")
    save_word(dest, USERNAME)


if __name__ == "__main__":
    main()
