<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sort</title>
</head>
<body>
    <a href="/">Go back</a> <br /> <br />
    <?php

    $arr = [9,8,7,6,5,4,3,2,1];
    sort($arr);

    $clength = count($arr);
    for($x = 0; $x < $clength; $x++) {
    echo $arr[$x];
    echo "<br>";
    }

    ?>
</body>
</html>