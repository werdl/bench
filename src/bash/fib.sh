#!/usr/bin/env bash

# TODO fix

# const fib = (n) => {
#     if (n === 0 || n === 1) return n;
#     else {
#         return fib(n - 1) + fib(n - 2)
#     }
# }
# console.log(fib(15))

fib () {
    n="$0"
    if [ "$n" == 0 ] || [ "$n" == 1 ]; then
        return "$n"
    else
        a=$n-1
        b=$n-2
        c="$(fib $a)"+"$(fib $b)"
        return "$c"
    fi
}

echo "$(fib 1)"