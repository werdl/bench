<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fib</title>
</head>
<body>
    <a href="/">Go back</a> <br /> <br />
    <?php
        # const fib = (n) => {
        #     if (n === 0 || n === 1) return n;
        #     else {
        #         return fib(n - 1) + fib(n - 2)
        #     }
        # }
        # console.log(fib(15))

        function fib($n) {
            if ($n === 0 || $n === 1) return $n;
            else {
                return fib($n - 1) + fib($n - 2);
            }
        }

        echo fib(15);

    ?>
</body>
</html>

