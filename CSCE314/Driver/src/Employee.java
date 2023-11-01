public class Employee {
    public String name;
    public String department;
    public String title;
    public int salary;

    // what if no public/private in front??

    public String getName() {
        return name;
    }

    public String getDepartment() {
        return department;
    }

    public String getTitle() {
        return title;
    }

    public int getSalary() {
        return salary;
    }

    public void setSalary(int newSalary) {
        salary = newSalary;
    }

    public String toString() {
        return name + "\n" + department + "\n" + title + "\n" + salary;
    }

}
