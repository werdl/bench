using System;

namespace SortN
{
    public class SortC
    {
        public static void Sort() {
            Console.WriteLine("\n");
            int[] arr = {9,8,7,6,5,4,3,2,1};
            Array.Sort(arr);
            foreach (int i in arr)
            {
                Console.WriteLine(i);
            }    
        }
    }
}