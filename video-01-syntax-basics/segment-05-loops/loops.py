# loops.py — Segment 05: Loops
#
# Python: range(), enumerate(), zip(), for/else — several things Java can't do.
# Java equivalent: Loops.java

print("=== Segment 05: Loops ===")

# --- range() replaces C-style for ---
print("range(5)   :", list(range(5)))          # range(stop)
print("step of 2  :", list(range(0, 10, 2)))   # range(start, stop, step)
print("countdown  :", list(range(5, 0, -1)))   # reverse — no extra variable needed

# --- for-each is just "for" ---
services = ["auth-service", "order-service", "payment-service"]
print("foreach    :", " ".join(services))

# --- enumerate(): index + value — no manual counter needed ---
print("indexed    :")
for i, service in enumerate(services):         # cf. Java: int i + services.get(i)
    print(f"  {i}: {service}")

# --- zip(): iterate two lists together ---
ports = [8080, 8081, 8082]
print("zipped     :")
for service, port in zip(services, ports):
    print(f"  {service} -> :{port}")

# --- while loop ---
n = 1
powers = []
while n <= 32:
    powers.append(n)
    n *= 2
print("powers of 2:", powers)

# --- for / else — else runs ONLY if loop was NOT broken ---
# Java devs: there is NO equivalent; Java uses a boolean flag instead
for service in services:
    if service == "billing-service":
        print("Found billing-service!")
        break
else:
    print("billing-service not found (for/else -- no Java equivalent)")

# --- List comprehension preview ---
# cf. Java: IntStream.range(0,6).map(x->x*x).boxed().toList()
squares = [x ** 2 for x in range(6)]
print("squares    :", squares)
# Deep dive on comprehensions coming in Video 2
