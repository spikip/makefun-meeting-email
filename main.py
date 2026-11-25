"""Entry for the make.fun bounty "The Meeting That Should Have Been an Email".

The program writes a single funny line to /output/entry.txt. The joke
is that the meeting could have been an email, except then nobody
would have watched the host read the email out loud for forty-five
minutes. The joke needs no setup because everyone has sat through
that exact meeting, and the host reading the email aloud is the
detail that makes it specific instead of generic. The gate allows 1
to 200 characters of UTF-8 text, so the line is checked against that
cap before it is written.
"""

import os

ENTRY = (
    "This meeting could have been an email, but then nobody would have "
    "watched me read the email out loud for forty-five minutes."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
