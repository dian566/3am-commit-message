"""The 3AM Commit Message — entry program.

Writes the single commit-message line to /output/entry.txt.
"""

import os

ENTRY = "fix: asked the model to review its own code. it apologized, then made it worse"


def main() -> None:
    # The gate allows 1..139 characters, one line, nothing else.
    line = ENTRY.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 139, f"entry is {len(line)} chars, must be 1..139"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
