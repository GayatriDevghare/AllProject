import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;
class Main {
    public static void main(String[] args) throws IOException
    {
        Scanner scan=new Scanner(System.in);
        ArrayList<Student> List=new ArrayList<>();
        int ch;
        System.out.println("------------------------------");
        System.out.println("Student Management System");
        System.out.println("------------------------------");
        do {
            System.out.println("1: Add Student");
            System.out.println("2: List Students");
            System.out.println("3: Search Student");
            System.out.println("4: Remove Student");
            System.out.println("5: Exit");
            System.out.print("Enter Choice: ");
            ch = scan.nextInt();
            switch (ch) {
                case 1:
                    System.out.print("Enter Rollno  :");
                    int rollno = scan.nextInt();
                    System.out.print("Enter Name    :");
                    String name = scan.next();
                    System.out.print("Enter Branch  :");
                    String branch = scan.next();
                    System.out.print("Enter Semester:");
                    String semester = scan.next();
                    Student s = new Student(rollno, name, branch, semester);
                    List.add(s);
                    System.out.println("Student Added...");
                    break;
                case 2:
                    for(Student item: List)
                    {
                        item.showData();
                        System.out.println("----------------------");
                    }
                    break;
                case 3:
                    System.out.print("Enter Rollno to Search: ");
                    int rn=scan.nextInt();
                    Student stud=searchStudent(List,rn);
                    if(stud==null)
                        System.out.println("Student Not found");
                    else
                        stud.showData();
                    break;
                case 4:
                    System.out.println("Enter rollno to Delete");
                    int roll=scan.nextInt();
                    if(removeStudent(List,roll))
                        System.out.println("Student Removed....");
                    else
                        System.out.println("Student not found...");
                    break;
            }
            System.out.println("Press ENTER to continue...");
            System.in.read();
        }while (ch!=5);
    }
    public static Student searchStudent(ArrayList<Student> list,int rollno)
    {
        for(Student s: list)
        {
            if(s.getRollno()==rollno)
                return s;
        }
        return null;
    }
    public static boolean removeStudent(ArrayList<Student> list,int rollno)
    {
        for(int i=0;i<list.size();i++)
        {
            if(list.get(i).getRollno()==rollno) {
                list.remove(i);
                return true;
            }
        }
        return false;
    }
}
class Student
{
    private int rollno;
    private String name,branch,semester;
    public Student(int r,String n,String b,String s)
    {
        rollno=r;
        name=n;
        branch=b;
        semester=s;
    }
    public void showData()
    {
        System.out.println("Rollno  :"+rollno);
        System.out.println("Name    :"+name);
        System.out.println("Branch  :"+branch);
        System.out.println("Semester:"+semester);
    }
    public int getRollno()
    {
        return rollno;
    }
}