import java.util.*;

class Fib
{
  public static void main(String[] args)
  {
    int n1 = 0, n2 = 1, n3, range;
    Scanner s = new Scanner(System.in);
    range = s.nextInt();
    System.out.println("Enter the range");
    System.out.println(n1);
    System.out.println(n2);

    for (int i = 2; i<range; i++)
    {
      n3 = n1 + n2;
      System.out.println(n3);
      n1 = n2;
      n2 = n3;
    }
  }
}
