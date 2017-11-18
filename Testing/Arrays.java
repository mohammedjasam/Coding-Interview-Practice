import java.util.*;

class Manip
{
    ArrayList<Integer> A = new ArrayList<Integer>(100);        
    
    Manip()
    {
        System.out.println("This is the constructor!\n");
    }

    public int getElement(int x)
    {
        return A.get(x);
    }

    public void addElement(int x)
    {
        A.add(x);
    }

    public void removeElement(int x)
    {
        A.remove(x);
    }

    public int getSize()
    {
        return A.size();
    }
}

class Arrays
{
    public static void main(String[] args)
    {
        Manip m = new Manip();
        Scanner s = new Scanner(System.in);

        System.out.print("Let's add some elements into an array\nEnter the number of elements\n> ");
        int n = s.nextInt();

        System.out.println("Enter the " + Integer.toString(n) + " elements!");
        for ( int i = 0; i < n; i++ )
        {
            // System.out.print("Enter the element "+ Integer.toString(i+1) + ":");
            m.addElement(s.nextInt());
        }

        for ( int i = 0; i < n; i++ )
        {
            // System.out.print("The element at position " + Integer.toString(i+1) + " is:\n");
            System.out.print(Integer.toString(m.getElement(i)) + " ");
        }

        m.removeElement(1);
        m.removeElement(3);
        m.removeElement(5);
        
        System.out.println("After the removing some elements");

        for ( int i = 0; i < m.getSize(); i++ )
        {
            System.out.print(Integer.toString(m.getElement(i)) + " ");
        }

    }
}