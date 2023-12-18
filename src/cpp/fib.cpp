#include <iostream>

int fib(int n) {
    if (n==0 || n==1) {
        return n;
    } else {
        return fib(n-1) + fib(n-2);
    }
}

int main() {
    std::cout << fib(15) << std::endl;
}