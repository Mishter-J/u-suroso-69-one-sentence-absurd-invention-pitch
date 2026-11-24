#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch — make.fun entry.

Writes a single one-sentence absurd invention pitch (169 characters,
one sentence) to /output/entry.txt.

The pitch: a doorbell that gives every visitor a job interview,
rejects the ones with bad energy, and texts the owner a full report titled
"We dodged one today" before they even stand up. It names the tiny
everyday annoyance (unwanted visitors at the door), the ridiculous
invention (an interviewing doorbell), and its silly mechanism
(interviews, rejects, reports) in one tight sentence.

Deterministic: the pitch is a fixed string constant. No randomness,
no clock, no network, no input files. Running this program twice
produces byte-identical output. After writing, the program reads the
file back and verifies the bytes match the pitch exactly, so a
truncated or mangled write can never pass silently.
"""

import os

# Gate limits from the competition rules: /output/entry.txt must be
# UTF-8 text of 1 to 220 characters, not only white space.
MAX_PITCH_CHARS = 220
MIN_PITCH_CHARS = 1

PITCH = (
    "A doorbell that gives every visitor a job interview, rejects the "
    "ones with bad energy, and texts you a full report titled "
    "\u2018We dodged one today\u2019 before you even stand up."
)

OUTPUT_PATH = os.path.join(
    os.environ.get("OUTPUT_DIR", "/output"), "entry.txt"
)


def validate(pitch: str) -> None:
    """Check the pitch against the gate before writing anything."""
    if not MIN_PITCH_CHARS <= len(pitch) <= MAX_PITCH_CHARS:
        raise ValueError(
            f"pitch must be {MIN_PITCH_CHARS}-{MAX_PITCH_CHARS} "
            f"characters, got {len(pitch)}"
        )
    if "\n" in pitch or "\r" in pitch:
        raise ValueError("pitch must be a single line")
    if not pitch.strip():
        raise ValueError("pitch must not be only whitespace")
    # One sentence only: exactly one sentence terminator, at the end.
    body = pitch.rstrip()
    if sum(body.count(c) for c in ".!?") != 1 or not body.endswith("."):
        raise ValueError("pitch must be exactly one sentence")


def write_pitch(pitch: str) -> None:
    """Write the pitch and verify the bytes on disk match exactly."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(pitch)
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != pitch.encode("utf-8"):
        raise RuntimeError("verification failed: output bytes differ")


def main() -> None:
    validate(PITCH)
    write_pitch(PITCH)
    print(f"Wrote {len(PITCH)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
