using System;

// const fib = (n) => {
//     if (n === 0 || n === 1) return n;
//     else {
//         return fib(n - 1) + fib(n - 2)
//     }
// }
// console.log(fib(15))

namespace FibN
{
  public class FibC
  {
    static int FibCalc(int n) {
        if (n == 0 || n == 1) return n;
        else {
            return FibCalc(n - 1) + FibCalc(n - 2);
        }
    }
    public static void Fib()
    {
      Console.WriteLine(FibCalc(15));    
    }
  }
}