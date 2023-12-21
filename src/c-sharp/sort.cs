using System;


class Program {
    static void Main() {
		Console.WriteLine("\n");
        int[] arr = {9,8,7,6,5,4,3,2,1};
        Array.Sort(arr);
        foreach (int i in arr) {
            Console.WriteLine(i);
        } 
	}
}
