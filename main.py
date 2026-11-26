"""make.fun entry: Two-Sentence Horror.

Writes one horror story to /output/entry.txt — exactly two
sentences, at most 400 characters.

The story: "My smartwatch congratulated me on 10,000 steps before
breakfast. I have not left my bed in three days." The first
sentence reads as a harmless brag; the second turns it — the steps
happened anyway, and the horror is implied, never explained: who
was walking, wearing the watch, while the narrator never left bed.
"""

import os

ENTRY = (
    "My smartwatch congratulated me on 10,000 steps before breakfast. "
    "I have not left my bed in three days."
)


def main() -> None:
    # Gate self-check: 1-400 chars, exactly two sentences.
    assert ENTRY and len(ENTRY) <= 400 and ENTRY.count(".") == 2
    os.makedirs("/output", exist_ok=True)
    tmp_path = "/output/.entry.txt.tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
