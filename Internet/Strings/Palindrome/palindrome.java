import java.util.*;

class palindrome
{
  public static void main(String[] args)
  {
    Scanner s = new Scanner(System.in);

    String a = s.nextLine();
    char[] str = a.toCharArray();
    String rev = "";

    for (int i=str.length-1; i>=0; i--)
    {
      System.out.println(str[str.length-i] + str[i]);
      rev += str[i];
    }
    System.out.println(rev);
    if (rev == a)
    {
      System.out.println("Palindrome");
    }
    else
    {
      System.out.println("Not a Palindrome");
    }

  }
}
