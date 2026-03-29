# hello_world.py — Segment 01: First Impressions
#
# Python requires: nothing. Just write code.
# No class, no main method, no imports needed for basic output.
# Java equivalent: HelloWorld.java

print("=== Segment 01: First Impressions ===")

# 1 line to say hello — no ceremony required
print("Hello from Python!")

# Suppress the newline with end=""  (cf. Java System.out.print)
print("No newline here", end="")
print(" -- continued on same line")

# f-strings (Python 3.6+) — cleaner than printf or String.format
name = "Azam"
print(f"Hello, {name}! Welcome to CodeWithAzam.")

# print() accepts multiple args, joined by sep=" " by default
import sys
print("Python version:", sys.version.split()[0])

"""
This is a docstring / multiline string.
Use triple quotes for multi-line text -- no StringBuilder needed.
Java uses text blocks (triple-quote) since Java 15 for similar purpose.
"""

# --- Key differences from Java ---
# 1. No class wrapper, no main() required
# 2. No type declarations on variables
# 3. No semicolons at end of statements
# 4. Indentation defines code blocks (not {})
# 5. f-strings beat printf / String.format for readability
