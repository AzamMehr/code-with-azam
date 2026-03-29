"""
run_all.py — runs every segment for Video 01 in order.

Usage:
    python run_all.py          (Windows / any platform)
    python3 run_all.py         (macOS / Linux)

Each segment prints its Python output; Java is compiled and run if javac is
available on PATH.
"""

import subprocess
import sys
import shutil
from pathlib import Path

SEGMENTS = [
    ("segment-01-first-impressions", "HelloWorld",  "hello_world.py"),
    ("segment-02-variables-types",   "Variables",   "variables.py"),
    ("segment-03-strings",           "Strings",     "strings.py"),
    ("segment-04-control-flow",      "ControlFlow", "control_flow.py"),
    ("segment-05-loops",             "Loops",       "loops.py"),
    ("segment-06-operators",         "Operators",   "operators.py"),
]

BASE = Path(__file__).parent
PYTHON = sys.executable          # exact binary that launched this script
HAS_JAVA = shutil.which("javac") is not None
SEP = "=" * 60


def run(cmd: list[str], cwd: Path) -> None:
    result = subprocess.run(cmd, cwd=cwd)
    if result.returncode != 0:
        print(f"  [ERROR] exit code {result.returncode}")


def main() -> None:
    for folder, java_class, py_file in SEGMENTS:
        seg_path = BASE / folder
        print(f"\n{SEP}")
        print(f"  {folder}")
        print(SEP)

        if HAS_JAVA:
            print("\n--- Java ---")
            run(["javac", f"{java_class}.java"], cwd=seg_path)
            run(["java", java_class], cwd=seg_path)
        else:
            print("\n--- Java --- (javac not found, skipping)")

        print("\n--- Python ---")
        run([PYTHON, py_file], cwd=seg_path)

    print(f"\n{SEP}")
    print("  All segments complete.")
    print(SEP)


if __name__ == "__main__":
    main()
