import java.util.*;
class PrimeNumbers
{
    PrimeNumbers()
    {
        System.out.println("Inside the Constructor");
    }
    public static void main (String[] args)
    {		
        int i = 0;
        int num = 0;
        Scanner s = new Scanner(System.in);
        System.out.print("Enter the range\n> ");
        int range = s.nextInt();
        String  primeNumbers = "";

        for ( i = 1; i <= range; i++ )         
        { 		  	  
            int counter = 0; 	  
            for ( num = i; num >= 1; num-- )
            {
                    if ( i % num == 0 )
                    {
                        counter++;
                    }
            }

            if (counter == 2)
            {
                //Appended the Prime number to the String
                primeNumbers = primeNumbers + i + " ";
            }	
        }	
        System.out.println("Prime numbers from 1 to 100 are :");
        System.out.println(primeNumbers);
    }
}