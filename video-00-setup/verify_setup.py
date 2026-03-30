#!/usr/bin/env python3
"""verify_setup.py - CodeWithAzam | Video 00: Setup
Confirms your Python environment is ready for the series.
Standard library only - no third-party packages required.
"""
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

PASS, FAIL, WARN = "[OK]  ", "[FAIL]", "[WARN]"
results: list[bool] = []


def check(label: str, passed: bool, detail: str = "") -> None:
    tag = PASS if passed else FAIL
    suffix = f" -- {detail}" if detail else ""
    print(f"  {tag} {label}{suffix}")
    results.append(passed)


# --- 1. Python version ---
print("\n=== Python Environment ===")
v = sys.version_info
ver_str = f"{v.major}.{v.minor}.{v.micro}"
print(f"  Location : {sys.executable}")
print(f"  Version  : {ver_str}")
check("Python >= 3.10 (required for match/case in later videos)",
      (v.major, v.minor) >= (3, 10), ver_str)

# --- 2. Virtual environment ---
print("\n=== Virtual Environment ===")
in_venv = sys.prefix != sys.base_prefix
check("Running inside a virtual environment", in_venv,
      sys.prefix if in_venv else "not in a venv -- run: uv venv && source .venv/bin/activate")

# --- 3. Standard-library imports ---
print("\n=== Standard Library Imports ===")
for mod in ["json", "os", "sys", "pathlib", "datetime", "collections", "typing"]:
    try:
        __import__(mod)
        check(f"import {mod}", True)
    except ImportError as exc:
        check(f"import {mod}", False, str(exc))

# --- 4. HTTP connectivity (graceful failure when offline) ---
print("\n=== Network Check ===")
try:
    import urllib.request
    import json as _json
    with urllib.request.urlopen("https://httpbin.org/get", timeout=5) as r:
        origin = _json.loads(r.read().decode()).get("origin", "unknown")
    check("HTTP request to httpbin.org/get", True, f"origin={origin}")
except Exception as exc:
    print(f"  {WARN} HTTP check skipped -- {exc}")
    print(f"  {WARN} Fine if offline; no points deducted.")

# --- 5. Summary ---
print("\n=== Summary ===")
passed, total = sum(results), len(results)
if all(results):
    print(f"  All {total}/{total} checks passed. You are ready for the series!")
else:
    print(f"  {passed}/{total} checks passed, {total - passed} failed.")
    print("  Fix the [FAIL] items above, then re-run this script.")
print()
