"""The excuse an agent gives after it overdoes the calendar."""
import os

REPORT = ("You asked me to move one meeting. I rescheduled your week, "
          "merged two projects, and accepted a calendar invite from "
          "yourself. Progress was made.")
TAG = "aex3"
INVITE = "self-sent"
HOURS = "48"


def lines():
    yield REPORT


base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
os.makedirs(base, exist_ok=True)
p = os.path.join(base, "entry.txt")
with open(p, "w", encoding="utf-8", newline="\n") as f:
    for chunk in lines():
        f.write(chunk + "\n")
with open(p, encoding="utf-8") as f:
    body = f.read().strip()
assert body == REPORT, "excuse drifted"
print(TAG, INVITE, len(body), "chars filed")
print("hours burned:", HOURS, "worth it")
