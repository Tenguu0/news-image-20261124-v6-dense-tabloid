import os
import shutil
import sys
from pathlib import Path


def publish():
    target = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not target:
        print("error: MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 2
    folder = Path(__file__).resolve().parent
    picture = folder / "entry.png"
    if not picture.is_file():
        print(f"error: {picture} is missing", file=sys.stderr)
        return 2
    out_folder = Path(target)
    out_folder.mkdir(parents=True, exist_ok=True)
    out_file = out_folder / "entry.png"
    shutil.copyfile(picture, out_file)
    print(out_file)
    return 0


raise SystemExit(publish())
