# control_flow.py — Segment 04: Control Flow
#
# Python: elif (not else if), flipped ternary, match/case (3.10+).
# Java equivalent: ControlFlow.java

print("=== Segment 04: Control Flow ===")

score = 72

# --- if / elif / else — note: elif not "else if", colon required ---
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")      # this branch runs
else:
    print("Grade: F")

# --- Ternary — ORDER IS FLIPPED vs Java: true_val IF cond ELSE false_val ---
result = "Pass" if score >= 60 else "Fail"   # Java: (score>=60) ? "Pass" : "Fail"
print(f"Result: {result}")

# --- match/case (Python 3.10+) — cf. Java switch expression ---
plan = "PRO"
match plan:
    case "FREE":
        monthly_limit = 100
    case "PRO":
        monthly_limit = 10_000
    case "ULTRA":
        monthly_limit = float("inf")
    case _:                    # _ is the wildcard (cf. Java default)
        monthly_limit = 0
print(f"{plan} limit: {monthly_limit}")

# --- Python truthiness: 0, "", [], {}, None are ALL falsy ---
print("\nTruthiness:")
for val in [0, "", [], {}, None, 42, "hi", [1]]:
    label = "truthy" if val else "falsy"
    print(f"  {repr(val):12} -> {label}")

# --- Chained comparisons (no Java equivalent) ---
age = 35
print(f"\n18 <= {age} <= 65 : {18 <= age <= 65}")   # reads like math!

# --- is vs == — REVERSED from Java ---
a = [1, 2, 3]
b = [1, 2, 3]
print(f"\na == b (value)   : {a == b}")   # True  — like Java .equals()
print(f"a is b (identity): {a is b}")    # False — like Java ==
