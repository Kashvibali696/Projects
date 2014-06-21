import java.lang.Math;

class Pi {
    public static final int MAX = 25;

    public static void main (String[] args) {
        if (args.length == 0 || args.length > 1) {
            System.out.println("Wrong number of arguments!");
            System.exit(-1);
        }

        int howMany = Integer.parseInt(args[0]);
        if (howMany > Pi.MAX) {
            System.out.println("You can request for up to " + Pi.MAX + " numbers.");
            System.exit(-2);
        }

        String format = "%." + howMany + "f";
        System.out.println(String.format("Pi up to " + howMany + " numbers: " + format, Math.PI));
    }
}
