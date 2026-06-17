
import java.io.Serializable;

public class Account implements Serializable
{
   private int AccountNo;
   private double Balance;
   String First_Name,Last_Name;
   public Account(String fn,String ln,int an,double bl)
   {
    First_Name=fn;
    Last_Name=ln;
    AccountNo=an;
    Balance=bl;
   }
   public void showBalance()
   {
    System.out.println("Account No :"+AccountNo);
    System.out.println("Balance :"+Balance);
   }
   public void deposit(int AT)
   {
    Balance=Balance+AT;
    System.out.println("Amount is deposited successfully");
   }
   public void withdraw(int AT)
   {
    if(Balance>=AT)
    {
      Balance=Balance-AT;
      System.out.println("Amount is withdraw Successfully");
    }
    else
      System.out.println("Insufficient Balance");
   }
   public void addinterest(double RT, int NY)
   {
    double si=Balance*RT*NY/100;
    Balance=Balance+si;
    System.out.println("Add interest Successfully");
   }
   public int getAccountNo()
   {
     return AccountNo;
   }
   public String getFName()
   {
    return First_Name;
   }
   public String getLName()
   {
     return Last_Name;
   }
   public double getBalance()
   {
    return Balance;
   }

}