"""mex6 countdown clerk: the line walks a checklist until nothing remains."""
import json
import os
import sys
from pathlib import Path

WALL = 200


def main():
    root = Path(__file__).resolve().parent
    drop = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    body = root.joinpath("entry.txt").read_text(encoding="utf-8").strip()
    remaining = [
        "strip done",
        "length known: %d" % len(body),
    ]
    ok = True
    while remaining:
        step = remaining.pop(0)
        if "length known" in step and len(body) > WALL:
            ok = False
            remaining = []
    if body == "" or body.isspace():
        ok = False
    if ok:
        drop.mkdir(parents=True, exist_ok=True)
        (drop / "entry.txt").write_bytes(body.encode("utf-8"))
        remaining.append("forwarded to %s" % drop)
    receipt = {"clerk": "mex6-countdown-r6", "ok": ok, "len": len(body), "wall": WALL, "last": remaining[-1] if remaining else None}
    print("VERDICT", json.dumps(receipt))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
