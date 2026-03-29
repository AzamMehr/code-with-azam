// Variables.java — Segment 02: Variables & Types
//
// Java: statically typed — every variable needs a declared type at compile time.
// Python equivalent: variables.py

public class Variables {

    public static void main(String[] args) {
        System.out.println("=== Segment 02: Variables & Types ===");

        // --- Explicit type declarations ---
        int    age    = 30;
        double price  = 29.99;
        boolean active = true;       // Python → True (capital T)
        String  name  = "Azam";

        // var: local type inference (Java 10+) — compiler still knows the type
        var score = 95;              // inferred as int
        var apiUrl = "https://api.example.com";  // inferred as String

        // final: constant — reassignment won't compile
        final String API_URL = "https://api.example.com/v1";

        // String.format — cf. Python f-strings
        String msg = String.format("User: %s, Age: %d, Price: $%.2f", name, age, price);
        System.out.println(msg);

        // null — Python equivalent is None
        String token = null;
        if (token != null) {
            System.out.println("Token: " + token);
        } else {
            System.out.println("token is null (Python: None)");
        }

        // Swap — requires a temp variable in Java
        int a = 1, b = 2;
        int temp = a; a = b; b = temp;
        System.out.println("After swap: a=" + a + "  b=" + b);

        // Type casting
        int truncated = (int) price;          // 29  — truncates, not rounds
        System.out.println("(int) 29.99 = " + truncated);

        // int x = 10; x = "hello";  ← COMPILE ERROR — can't change type
    }
}
