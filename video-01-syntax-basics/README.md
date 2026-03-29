# Video 01 — Python Syntax Crash Course for Java Developers: The Basics

> **Watch on YouTube**: [link placeholder]

A segment-by-segment companion to the video. Each folder contains one Java file
and one Python file covering the same concept side by side.

## Segments

| # | Folder | Java Concept | Python Equivalent |
|---|--------|-------------|-------------------|
| 01 | segment-01-first-impressions | `public static void main` ceremony | bare script execution |
| 02 | segment-02-variables-types | `int x = 5` static typing | `x = 5` dynamic typing |
| 03 | segment-03-strings | `substring`, `charAt`, `.equals()` | slicing, `*`, `join()` |
| 04 | segment-04-control-flow | `else if`, ternary, `switch` | `elif`, flipped ternary, `match/case` |
| 05 | segment-05-loops | `for(int i=0...)`, enhanced-for | `range()`, `enumerate()`, `zip()`, for/else |
| 06 | segment-06-operators | `/`, `Math.pow`, `&&`/`\|\|`/`!` | `//`, `**`, `and`/`or`/`not`, `in`, `:=` |

## Running All Segments

```bash
# from this directory (video-01-syntax-basics/)
python run_all.py
```

## Running Individual Files

```bash
# Java — compile then run
cd segment-01-first-impressions
javac HelloWorld.java && java HelloWorld

# Python
python segment-01-first-impressions/hello_world.py
```

## Requirements

- Java 17+ (tested on Java 21)
- Python 3.10+ (uses `match/case` in segment 04, walrus `:=` in segment 06)

## Key Python "Aha" Moments for Java Devs

1. **No ceremony** — no class wrapper, no main method, no semicolons; indentation IS the block
2. **No type declarations** — variables infer type at assignment; type hints are optional and not enforced
3. **Strings are sliceable** — `s[1:4]`, `s[::-1]` reverses a string; nothing like this in Java
4. **Ternary order is flipped** — `true_val if cond else false_val` (condition in the middle)
5. **`for/else`** — the `else` block runs only if the loop completed without `break`
6. **`/` always gives float** — use `//` for integer (floor) division; `**` for exponentiation
7. **`and`, `or`, `not`** — not `&&`, `||`, `!`; logical operators are English words
