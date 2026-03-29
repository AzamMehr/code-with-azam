# strings.py — Segment 03: Strings
#
# Python strings: immutable, but with far richer slicing than Java.
# Java equivalent: Strings.java

print("=== Segment 03: Strings ===")

endpoint = "api.example.com/users"

# --- Length & character access ---
print(f"len()        : {len(endpoint)}")      # len() not .length()
print(f"[0]          : {endpoint[0]}")        # indexing, not charAt()
print(f"[-1]         : {endpoint[-1]}")       # negative index! Java needs length()-1

# --- Slicing [start:stop:step] — Java's most-missed feature ---
print(f"[0:3]        : {endpoint[0:3]}")      # cf. substring(0,3)
print(f"[4:]         : {endpoint[4:]}")       # cf. substring(4)
print(f"[:3]         : {endpoint[:3]}")       # from beginning

# SLICING SUPERPOWER — no Java equivalent for these:
print(f"[::2]        : {endpoint[::2]}")      # every other character
print(f"[::-1]       : {endpoint[::-1]}")     # reverse entire string!

# --- Common methods ---
print(f"upper()      : {endpoint.upper()}")
print(f"replace()    : {endpoint.replace('users', 'orders')}")
print(f"'example' in : {'example' in endpoint}")   # 'in' not .contains()
print(f"strip()      : {'  hello  '.strip()}")      # cf. .trim()
print(f"split('/')[0]: {endpoint.split('/')[0]}")

# --- String multiplication (surprising for Java devs!) ---
print(f"'=-' * 3     : {'=-' * 3}")           # no Java equivalent

# --- join() — called on the separator, not the list ---
roles = ", ".join(["admin", "editor", "viewer"])
print(f"join()       : {roles}")

# --- == compares VALUE directly (opposite of Java!) ---
a = "hello"
b = "hello"
print(f"== (value)   : {a == b}")   # True  — use == for value comparison
print(f"is (identity): {a is b}")   # True here (string interning) but NEVER rely on this
# In Java: == is reference, .equals() is value. Python: REVERSED.
