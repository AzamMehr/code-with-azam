# variables.py — Segment 02: Variables & Types
#
# Python: dynamically typed — variables are labels, not typed slots.
# Java equivalent: Variables.java

print("=== Segment 02: Variables & Types ===")

# --- No type declarations needed ---
age    = 30          # int   — inferred at runtime
price  = 29.99       # float — Python has no double/float distinction
active = True        # bool  — capital T (False also capital F)
name   = "Azam"      # str   — no char type; single chars are just strings

# Type hints (Python 3.5+) — optional, purely for documentation
# They do NOT enforce types at runtime
score: int = 95
api_url: str = "https://api.example.com"

# Constants by convention: ALL_CAPS — nothing prevents reassignment
API_URL = "https://api.example.com/v1"

# f-strings — cleaner than String.format
msg = f"User: {name}, Age: {age}, Price: ${price:.2f}"
print(msg)

# None — Java equivalent is null; use 'is not None' not '!= None'
token = None
if token is not None:
    print(f"Token: {token}")
else:
    print("token is None (Java: null)")

# Multiple assignment — one line
x, y, z = 1, 2, 3
print(f"x={x}  y={y}  z={z}")

# Swap without a temp variable — tuple unpacking
a, b = 1, 2
a, b = b, a          # impossible in Java without a temp
print(f"After swap: a={a}  b={b}")

# Dynamic typing: x = 10 then x = "hello" — this WORKS in Python
x = 10
x = "hello"          # Java would refuse: incompatible types
print(f"x changed type: {x!r}  ->  type is now {type(x).__name__}")

# type() checks the current type at runtime
print(type(age), type(price), type(active), type(token))
