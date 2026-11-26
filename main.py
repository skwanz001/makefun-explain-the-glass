"""Five Seconds to Explain the Glass — entry program.

Writes the single sentence a house cat would say in its own defence
after knocking a glass off the table, to /output/entry.txt.

The line: the glass squatted in the cat's sunbeam all morning without
paying rent, so the cat evicted it. Cat logic through and through —
territorial, self-interested, zero remorse, no apology, no confession.
Fresh idea: the glass is not a victim of gravity or a slippery edge,
it is a tenant that did not pay up.

Standard library only: the grading sandbox installs nothing.
"""

import os

ENTRY = (
    "That glass had been squatting in my sunbeam all morning "
    "without paying rent, so I evicted it."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text == text.strip() and text, "entry must not be only whitespace"
    # One sentence only: exactly one sentence-ending full stop, at the end.
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
