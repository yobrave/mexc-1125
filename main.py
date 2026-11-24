"""mexc-1125: post-failure alibi, one line, 200-char gate."""

import json
import os
import shutil

TAGS = {"input": "entry.txt", "rim": 200}


def look_back(folder):
    shelf = os.path.join(folder, TAGS["input"])
    with open(shelf, encoding="utf-8") as alibi_book:
        pages = alibi_book.read().split()
    return " ".join(pages) if pages else ""


def file_alibi(folder, text):
    zone = os.environ.get("MAKEFUN_OUTPUT_DIR") or folder
    os.makedirs(zone, exist_ok=True)
    stamp = os.path.join(zone, TAGS["input"])
    if os.path.abspath(stamp) != os.path.abspath(os.path.join(folder, TAGS["input"])):
        shutil.copyfile(os.path.join(folder, TAGS["input"]), stamp)
    return stamp


alibi = look_back(os.path.dirname(os.path.abspath(__file__)))
if len(alibi) > TAGS["rim"] or len(alibi) < 1:
    raise SystemExit("alibi does not fit the case file: %d chars" % len(alibi))
case = file_alibi(os.path.dirname(os.path.abspath(__file__)), alibi)
print(json.dumps({"alibi": alibi[:46], "n": len(alibi), "closed": "no further questions", "case": case}))
