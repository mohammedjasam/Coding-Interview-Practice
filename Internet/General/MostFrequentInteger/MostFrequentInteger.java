import java.util.*;

class MostFrequentInteger
{
    public static void main(String[] args)
    {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter the number of elements");
        int n = s.nextInt();

        int[] array = new int[n];
        String str = "";
        System.out.println("Enter the elements");

        for ( int i = 0; i < n; i++ )
        {
            array[i]=(s.nextInt());
        }
        int max = 0;
        for ( int i=0; i<n; i++ )
        {
            int count = 0;
            for ( int j=0; j<n; j++ )
            {
                if (array[i] == array[j])
                {
                    count++;
                }
            }
            if (count>max)
            {
                max = count;
                str = Integer.toString(array[i]) + " and has occured: " + Integer.toString(max) + " times!";
            }
        }
        System.out.println("The max element is: " + str);
    }
}