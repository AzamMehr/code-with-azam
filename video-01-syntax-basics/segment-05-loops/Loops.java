// Loops.java — Segment 05: Loops
//
// Java: C-style for, enhanced-for, while. Index tracking is manual.
// Python equivalent: loops.py

import java.util.List;

public class Loops {

    public static void main(String[] args) {
        System.out.println("=== Segment 05: Loops ===");

        // --- C-style for (range equivalent) ---
        System.out.print("range(5)   : ");
        for (int i = 0; i < 5; i++) {
            System.out.print(i + " ");
        }
        System.out.println();

        // --- Counting with step ---
        System.out.print("step of 2  : ");
        for (int i = 0; i < 10; i += 2) {
            System.out.print(i + " ");
        }
        System.out.println();

        // --- Enhanced for-each ---
        var services = List.of("auth-service", "order-service", "payment-service");
        System.out.print("foreach    : ");
        for (String service : services) {
            System.out.print(service + " ");
        }
        System.out.println();

        // --- Index + value — must track index manually (no enumerate) ---
        System.out.println("indexed    :");
        for (int i = 0; i < services.size(); i++) {
            System.out.printf("  %d: %s%n", i, services.get(i));
        }

        // --- while loop ---
        int n = 1;
        System.out.print("powers of 2: ");
        while (n <= 32) { System.out.print(n + " "); n *= 2; }
        System.out.println();

        // --- No for/else — simulate with a boolean flag ---
        boolean found = false;
        for (String s : services) {
            if (s.equals("billing-service")) { found = true; break; }
        }
        if (!found) System.out.println("billing-service not found (flag pattern)");
    }
}
