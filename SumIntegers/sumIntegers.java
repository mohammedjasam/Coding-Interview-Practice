import java.util.*;

class calcSum
{
    private int size;
    
    public void sumIt(int[] arr, int sum)
    {
        int n = arr.length;

        for (int i=0; i<n; i++)
        {
            for (int j=i+1; j<n; j++)
            {
                // System.out.println(Integer.toString(arr[i]) + Integer.toString(arr[j]));                
                if (arr[i] + arr[j] == sum)
                {
                    System.out.println("(" + Integer.toString(arr[i]) + ", " + Integer.toString(arr[j]) + ")");
                    // int k =1;
                }
            }
        }
    }
}

class sumIntegers
{
    public static void main(String[] args)
    {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter the size of the Elements!");
        int size = s.nextInt();
        int[] arr = new int[size];
        System.out.println("Enter the elements");
        for (int i=0; i<size; i++)
        {
            arr[i] = s.nextInt();
        }
        System.out.println("Enter the sum you want to calc");
        calcSum cS = new calcSum();
        int summ = s.nextInt();
        cS.sumIt(arr, summ);
    }
}