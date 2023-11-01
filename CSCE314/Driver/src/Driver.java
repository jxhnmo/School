import java.util.Scanner;

public class Driver {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) throws Exception {
        Employee Heila = new Employee(); // just created a new instance
        Heila.name = "Ms. Heila";
        Heila.department = "Garbage duty";
        Heila.salary = -11111;
        Heila.title = "dumpster cleaner";

        // hard code way of setting her salary
        Heila.setSalary(10);

        // user input way of setting her salary (Scenario #1)
        System.out.println("Please place in Heila's new salary");
        int nS = sc.nextInt();
        Heila.setSalary(nS);

        // user input way of setting her salary (Scenario #2)
        System.out.println("Please place in Heila's new salary");
        Heila.setSalary(sc.nextInt());
    }
}
