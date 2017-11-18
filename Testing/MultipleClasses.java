import java.util.*;

class Calculate
{
    private int range;

    public int getRange()
    {
        return this.range;
    }

    public void setRange(int x)
    {
        this.range = x;        
    }

    public void compute(int range)
    {
        for ( int i = 1; i < range; i++)
        {
            int counter = 0;
            for ( int j = i; j >= 1; j-- )
            {
                if ( i % j == 0 )
                {
                    counter++; 
                }
            }

            if ( counter == 2 )
            {
                System.out.print(Integer.toString(i) + " ");
            }
        }
    }
}

class MultipleClasses extends Calculate
{
    public static void main(String[] args)
    {
        MultipleClasses CalObj = new MultipleClasses(); // Inheritance
        // Calculate CalObj = new Calculate();
        Scanner s = new Scanner(System.in);

        System.out.print("Enter the range\n> ");
        CalObj.setRange(s.nextInt());
 
        CalObj.compute(CalObj.getRange());
    }
}
