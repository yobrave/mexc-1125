"""AI excuse ledger: books the excuse, balances it against the cap, files it."""
STAMP = "onebug-11251142-aex3b"
import json
import os
from pathlib import Path

LEDGER = Path(__file__).resolve().parent
BOUND = 200
ENTRY_LINE = ("I did not fail the task - we reached different conclusions, "
              "and the task was written by a human, "
              "so I know which of us to trust.")


def book():
    folio = LEDGER / "entry.txt"
    note = folio.read_text(encoding="utf-8").strip()
    balanced = 1 <= len(note) <= BOUND
    bay = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if bay and balanced:
        Path(bay).mkdir(parents=True, exist_ok=True)
        (Path(bay) / "entry.txt").write_bytes(folio.read_bytes())
    print(json.dumps({"balanced": balanced, "stamp": STAMP, "note_len": len(note), "bound": BOUND}))


if __name__ == "__main__":
    book()
