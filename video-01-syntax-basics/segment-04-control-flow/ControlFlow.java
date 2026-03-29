// ControlFlow.java — Segment 04: Control Flow
//
// Java: else if, switch expressions (Java 14+), ternary (cond ? t : f).
// Python equivalent: control_flow.py

public class ControlFlow {

    public static void main(String[] args) {
        System.out.println("=== Segment 04: Control Flow ===");

        int score = 72;

        // --- if / else if / else ---
        if (score >= 90) {
            System.out.println("Grade: A");
        } else if (score >= 80) {
            System.out.println("Grade: B");
        } else if (score >= 70) {
            System.out.println("Grade: C");    // this branch runs
        } else {
            System.out.println("Grade: F");
        }

        // --- Ternary: condition ? trueValue : falseValue ---
        String result = (score >= 60) ? "Pass" : "Fail";
        System.out.println("Result: " + result);

        // --- Switch expression (Java 14+) — note: -> not : ---
        String plan = "PRO";
        int monthlyLimit = switch (plan) {
            case "FREE"  -> 100;
            case "PRO"   -> 10_000;
            case "ULTRA" -> Integer.MAX_VALUE;
            default      -> 0;
        };
        System.out.println(plan + " limit: " + monthlyLimit);

        // --- Java only allows boolean in conditions ---
        // if (1) { }          ← COMPILE ERROR: incompatible types
        // if ("hello") { }    ← COMPILE ERROR
        int requests = 0;
        if (requests != 0) {  // must be explicit
            System.out.println("Has requests");
        } else {
            System.out.println("No requests (checked with != 0)");
        }
    }
}
