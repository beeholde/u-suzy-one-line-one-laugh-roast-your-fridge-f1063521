"""One Line, One Laugh: Roast Your Fridge entry.

Writes a single phone roast to entry.txt in the output directory:
UTF-8, one line, no trailing newline. Standard library only.
"""

import os
from pathlib import Path

# Trial winner (GLM-5.3-Flash pairwise vs the three strongest visible
# field lines, both orders): mean game score 0.583. The turn is the
# last word -- dictation that handles everything except the speaker's
# own name, which it treats as hearsay.
ROAST = (
    "My phone translates my voice into text perfectly, until I say "
    "my own name, which it treats as a rumor."
)
LIMIT = 200


def checked_text() -> str:
    text = ROAST.strip()
    if "\n" in text or "\r" in text:
        raise ValueError("roast must stay on one line")
    if not 1 <= len(text) <= LIMIT:
        raise ValueError(f"roast length {len(text)} outside 1-{LIMIT}")
    if not text.strip():
        raise ValueError("roast must not be blank")
    return text


def main() -> None:
    text = checked_text()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(text.encode("utf-8"))
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
