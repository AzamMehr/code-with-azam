// Operators.java — Segment 06: Operators
//
// Java: / truncates when both ints, Math.pow, &&, ||, !
// Python equivalent: operators.py

public class Operators {

    public static void main(String[] args) {
        System.out.println("=== Segment 06: Operators ===");

        // --- Division: int/int truncates toward zero in Java ---
        System.out.println("10 / 3  (int/int)  = " + (10 / 3));      // 3
        System.out.println("10.0 / 3 (float/)  = " + (10.0 / 3));    // 3.333...
        System.out.println("-7 / 2  (truncates) = " + (-7 / 2));      // -3 (toward zero)

        // --- Modulo ---
        System.out.println("10 % 3             = " + (10 % 3));       // 1

        // --- Exponentiation — no ** operator; use Math.pow ---
        System.out.println("Math.pow(2, 10)    = " + (int) Math.pow(2, 10));

        // --- Logical operators: symbols ---
        boolean t = true, f = false;
        System.out.println("t && f  = " + (t && f));   // Python: t and f
        System.out.println("t || f  = " + (t || f));   // Python: t or  f
        System.out.println("!t      = " + (!t));        // Python: not t

        // --- Bitwise (same symbols in both languages) ---
        System.out.println("5 & 3   = " + (5 & 3));    // 1
        System.out.println("5 | 3   = " + (5 | 3));    // 7
        System.out.println("5 ^ 3   = " + (5 ^ 3));    // 6

        // --- "in" equivalent: .contains() ---
        var roles = java.util.List.of("admin", "editor", "viewer");
        System.out.println("contains: " + roles.contains("admin"));

        // Java has no := walrus operator — assign and test are separate statements
    }
}
