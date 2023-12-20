#!/usr/bin/env bash

# TODO fix

# const fib = (n) => {
#     if (n === 0 || n === 1) return n;
#     else {
#         return fib(n - 1) + fib(n - 2)
#     }
# }
# console.log(fib(15))

fib() {
    n=15
    if [ "$n" == 0 ] || [ "$n" == 1 ]; then
        echo "$n"
        exit 0
    else
        echo "debug"
        a=$((n-1))
        echo $a
        b=$((n-2))
        echo $b
        # c=$(($(fib $a)+$(fib $b)))
        c=$(fib $a)
        echo "$c"
        d=$(fib $b)
        echo "$d"
        e=$((c+d))
        echo "$e"
    fi
}

fib