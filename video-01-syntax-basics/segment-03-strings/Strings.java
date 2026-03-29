// Strings.java — Segment 03: Strings
//
// Java strings: immutable objects, zero-indexed, rich method library.
// Python equivalent: strings.py

public class Strings {

    public static void main(String[] args) {
        System.out.println("=== Segment 03: Strings ===");

        String endpoint = "api.example.com/users";

        // --- Length & character access ---
        System.out.println("length()     : " + endpoint.length());
        System.out.println("charAt(0)    : " + endpoint.charAt(0));

        // --- Substring (begin inclusive, end exclusive — same as Python) ---
        System.out.println("substring(0,3): " + endpoint.substring(0, 3));
        System.out.println("substring(4)  : " + endpoint.substring(4));

        // --- Common methods ---
        System.out.println("toUpperCase(): " + endpoint.toUpperCase());
        System.out.println("replace()    : " + endpoint.replace("users", "orders"));
        System.out.println("contains()   : " + endpoint.contains("example"));
        System.out.println("trim()       : " + "  hello  ".trim());
        System.out.println("split()[0]   : " + endpoint.split("/")[0]);

        // --- Repeat (Java 11+) ---
        System.out.println("repeat(3)    : " + "=-".repeat(3));

        // --- String.join ---
        String roles = String.join(", ", "admin", "editor", "viewer");
        System.out.println("join()       : " + roles);

        // --- ALWAYS use .equals() for value comparison, never == ---
        String a = "hello";
        String b = new String("hello");
        System.out.println("==           : " + (a == b));        // false — reference!
        System.out.println(".equals()    : " + a.equals(b));     // true  — value
    }
}
