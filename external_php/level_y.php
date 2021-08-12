<?php

header("Content-type: image/png");
$imgPath = 'images/level_y.png';
$image = imagecreatefrompng($imgPath);
$_y = $_GET['y'];
$y1 = (0 - $_y) + 125;
$y2 = 40;
$x1 = 50;
$x2 = 20;
//98 to 152
// 125 +- 27
$min = 98;
$max = 152;
$_min = 50;
$_max = 200;

if ($y1 > $max || $y1 < 98){
    $color = imagecolorallocate($image, 238, 0, 0); //red2
    if ($y1 > $_max) $y1 = $_max;
    if ($y1 < $_min) $y1 = $_min;
}
elseif ($y1 == 124 || $y1 == 125 || $y1 == 126) {
    $color = imagecolorallocate($image, 58, 95, 205); //RoyalBlue3
}
else{
    $color = imagecolorallocate($image, 238, 201, 0); //gold2
}

imagefilledellipse($image, $x1, $y1, $x2, $y2, $color);
imagepng($image);
imagedestroy($image);

?> 