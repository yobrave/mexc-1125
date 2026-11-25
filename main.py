"""Blame shuttle: verifies the excuse line, then forwards it for grading."""
import json
import os
import pathlib

CEILING = 200
CHALK = "aex3b-oops"


def blame(root: pathlib.Path):
    """Pull the draft excuse and keep the first line with ink on it."""
    source = root / "entry.txt"
    with source.open("rb") as tap:
        text = tap.read().decode("utf-8")
    for row in text.splitlines(keepends=False):
        if row.replace("\r", "").strip():
            return row.replace("\r", "")
    return ""


def absolve(line: str):
    if not line.strip():
        return "excuse missing"
    if len(line) > CEILING:
        return "excuse overflows (%d > %d)" % (len(line), CEILING)
    return ""


def forward(line: str, root: pathlib.Path):
    inbox = os.environ.get("MAKEFUN_OUTPUT_DIR") or str(root / "output")
    os.makedirs(inbox, exist_ok=True)
    slot = pathlib.Path(inbox) / "entry.txt"
    slot.write_bytes(line.encode("utf-8"))
    if slot.read_bytes() != line.encode("utf-8"):
        raise RuntimeError("forward lost bytes")
    return slot


here = pathlib.Path(__file__).resolve().parent
excuse = blame(here)
flaw = absolve(excuse)
if flaw:
    print(json.dumps({"clear": False, "flaw": flaw, "chalk": CHALK}))
    raise SystemExit(1)
slot = forward(excuse, here)
print(json.dumps({"clear": True, "len": len(excuse), "chalk": CHALK, "slot": slot.name}))
