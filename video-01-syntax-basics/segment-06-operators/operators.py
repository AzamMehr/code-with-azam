# operators.py — Segment 06: Operators
#
# Rapid-fire: Python operators that differ from Java.
# Java equivalent: Operators.java

print("=== Segment 06: Operators ===")

# --- / ALWAYS gives float in Python (not int!) ---
print(f"10 / 3  (true div)   = {10 / 3}")      # 3.3333... ← NOT 3 like Java!
print(f"10 // 3 (floor div)  = {10 // 3}")     # 3   ← use // for integer result
print(f"-7 // 2 (floors!)    = {-7 // 2}")     # -4  ← floors toward -∞ (Java gives -3)

# --- Modulo ---
print(f"10 % 3               = {10 % 3}")       # 1

# --- ** is exponentiation (no Math.pow needed) ---
print(f"2 ** 10              = {2 ** 10}")      # 1024

# --- Logical operators are English words, not symbols ---
t, f = True, False
print(f"t and f = {t and f}")   # cf. Java &&
print(f"t or  f = {t or f}")    # cf. Java ||
print(f"not t   = {not t}")     # cf. Java !

# --- Bitwise: same symbols as Java ---
print(f"5 & 3   = {5 & 3}")     # 1
print(f"5 | 3   = {5 | 3}")     # 7
print(f"5 ^ 3   = {5 ^ 3}")     # 6

# --- in operator: replaces .contains() ---
roles = ["admin", "editor", "viewer"]
print(f"'admin' in roles  = {'admin' in roles}")    # True  — cf. roles.contains("admin")
print(f"'owner' not in    = {'owner' not in roles}") # True  — not in is one operator

# --- Walrus operator := (Python 3.8+) — assign AND test in one expression ---
# Java has no equivalent; you must split into two statements
api_responses = [200, 404, 200, 500, 200]
errors = [code for code in api_responses if (category := code // 100) >= 4]
print(f"error codes       = {errors}")   # [404, 500]
# Java: must compute category separately, can't assign inside if
