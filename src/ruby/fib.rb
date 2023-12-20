#!/usr/bin/env ruby

# const fib = (n) => {
#     if (n === 0 || n === 1) return n;
#     else {
#         return fib(n - 1) + fib(n - 2)
#     }
# }
# console.log(fib(15))

def fib(n)
    if n == 0
        return n
    end
    if n == 1
        return n
    else
        return fib(n - 1) + fib(n - 2)
    end
end

puts fib(15)