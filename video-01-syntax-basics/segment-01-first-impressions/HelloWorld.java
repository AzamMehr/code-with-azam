// HelloWorld.java — Segment 01: First Impressions
//
// Java requires: a public class matching the filename,
//                a specific main() signature,
//                explicit print method calls.
// Python equivalent: hello_world.py

public class HelloWorld {

    // Entry point — this exact signature is required
    public static void main(String[] args) {

        System.out.println("=== Segment 01: First Impressions ===");

        // Basic output — println adds a newline
        System.out.println("Hello from Java!");

        // print() with no newline → System.out.print (no 'ln')
        System.out.print("No newline here");
        System.out.println(" -- continued on same line");

        // String formatting with printf (%n = newline, platform-safe)
        String name = "Azam";
        System.out.printf("Hello, %s! Welcome to CodeWithAzam.%n", name);

        // Show Java version
        System.out.println("Java version: " + System.getProperty("java.version"));

        // 7 lines of ceremony just to print "Hello from Java!"
        // (class declaration + main signature + println + closing braces)
    }
}
