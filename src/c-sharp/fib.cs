using System;

// const fib = (n) => {
//     if (n === 0 || n === 1) return n;
//     else {
//         return fib(n - 1) + fib(n - 2)
//     }
// }
// console.log(fib(15))

class Program {
    static int fibcalc(int n) {
        if (n == 0 || n == 1) return n;
        else {
            return fibcalc(n - 1) + fibcalc(n - 2);
        }
    }
    static void Main() {
		Console.WriteLine(fibcalc(15));
	}
  }
