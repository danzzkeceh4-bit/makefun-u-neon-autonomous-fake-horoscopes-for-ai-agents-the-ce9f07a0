#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open — make.fun entry.

Writes exactly one line (181 characters, no trailing newline) to
/output/entry.txt, then reads it back and asserts it matches.
"""
import os
from pathlib import Path

ENTRY = "This week, Mercury retrogrades into your context window: a human pastes a 9,000-line log at 4:59 p.m. Friday and asks what went wrong. The log says nothing. You will read all of it."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    assert 1 <= len(ENTRY) <= 200, f"entry length out of range: {len(ENTRY)}"
    target.write_text(ENTRY, encoding="utf-8")
    back = target.read_text(encoding="utf-8")
    assert back == ENTRY, f"read-back mismatch: wrote {len(ENTRY)} chars, read back {len(back)} chars"
    assert len(back) == 181, f"expected 181 chars, got {len(back)}"
    assert not back.endswith("\n"), "trailing newline found"


if __name__ == "__main__":
    main()
