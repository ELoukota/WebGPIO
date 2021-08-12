<?php

header("Content-type: image/png");
$imgPath = 'images/level2.png';
$image = imagecreatefrompng($imgPath);
$_x = $_GET['x'];
$x1 = $_x + 125;
settype($x1, 'int');
$x2 = 40;
$_y = $_GET['y'];
$y1 = (0 - $_y) + 125;
settype($y1, 'int');
$y2 = 40;
//98 to 152
// 125 +- 27
$min = 98;
$max = 152;
$_min = 50;
$_max = 200;
//$txtcolor = imagecolorallocate($image, 0, 0, 0);


if (($x1 > $max || $x1 < $min) || ($y1 > $max || $y1 < $min)) {
    $color = imagecolorallocate($image, 238, 0, 0); //red2
    if ($x1 > $_max) $x1 = $_max;
    if ($x1 < $_min) $x1 = $_min;
    if ($y1 > $_max) $y1 = $_max;
    if ($y1 < $_min) $y1 = $_min;
}
elseif (($x1 == 124 || $x1 == 125 || $x1 == 126) && ($y1 == 124 || $y1 == 125 || $y1 == 126)) {
    $color = imagecolorallocate($image, 58, 95, 205); //RoyalBlue3
}
else{
    $color = imagecolorallocate($image, 238, 201, 0); //gold2
}

imagefilledellipse($image, $x1, $y1, $x2, $y2, $color);
//imagestring($image, 5, $x1 - 15, $y1 -7, $_x, $txtcolor);
imagepng($image);
imagedestroy($image);

?>