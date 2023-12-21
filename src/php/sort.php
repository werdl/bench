<?php

$arr = [9,8,7,6,5,4,3,2,1];
sort($arr);

$clength = count($arr);
for($x = 0; $x < $clength; $x++) {
    echo $arr[$x];
    echo "<br>";
}

?>
