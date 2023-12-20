using System;
using HelloN;
using FibN;
using SortN;

namespace Bench 
{
    class Program
    {
        static void GetChoice() {
            Console.WriteLine("Enter your choice: \n1: Hello, World \n2: Fibbonacci\n3: Sorting");
            int choice = Convert.ToInt32(Console.ReadLine());
            if (choice == 1) HelloC.Hello();
            else if (choice == 2) FibC.Fib();
            else if (choice == 3) SortC.Sort();
            else 
            {
                Console.WriteLine("Incorrect answer.");
                GetChoice();
            }
        }
        static void Main(string[] args) 
        {
            GetChoice();
        }
    }
}