-- const fib = (n) => {
--     if (n === 0 || n === 1) return n;
--     else {
--         return fib(n - 1) + fib(n - 2)
--     }
-- }
-- console.log(fib(15))

fib 0 = 0
fib 1 = 1
fib n = fib(n - 1) + fib(n - 2)

main = do
    putStr (show (fib(15)))
    putStr "\n"