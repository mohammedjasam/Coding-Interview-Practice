import java.util.*;

class checkOnce
{
  int[] arr;

  public void check(int[] arr)
    {
      // System.out.print("The length is " + Integer.toString(arr.length));
      for (int i = 0; i<arr.length; i++)
      {
        int count = 1;

        for (int j = i+1; j<arr.length; j++)
        {
          // System.out.println(Integer.toString(arr[i]) + ", " + Integer.toString(arr[j]));
          if (arr[i] == arr[j])
          {
            count++;
          }
        }
        // System.out.println(count);
        if (count == 1)
        {
          System.out.println(arr[i]);
        }
        else
        {
          System.out.print("LOL");
        }
    }
  }
} 
class OnlyOccursOnce
{
public static void main(String[] args)
{
Scanner s = new Scanner(System.in);
System.out.println("Enter the size of the array");
int size = s.nextInt();
int[] array = new int[size];

System.out.println("Enter the elements");
for (int i=0; i<size; i++)
{
array[i] = s.nextInt();
}
checkOnce co = new checkOnce();
co.check(array);
}
}
