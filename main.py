import os
import shutil
import sys
from pathlib import Path


def publish():
    source = Path(__file__).resolve().parent / "entry.png"
    dest_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not dest_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 2
    if not source.is_file():
        print("entry.png is missing next to main.py", file=sys.stderr)
        return 2
    out_dir = Path(dest_dir)
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, out_dir / "entry.png")
    except OSError as problem:
        print(f"could not write entry.png: {problem}", file=sys.stderr)
        return 2
    return 0


raise SystemExit(publish())
