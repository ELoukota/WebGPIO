<?php

header("Content-type: image/png");
$string = $_GET['text'];
$type = $_GET['type'];
$txtSize = 5;
$height = 75;
$width = $height;
$px     = ($width - 7.5 * strlen($string)) / 2;
//$py     = (imagesy($im) / 2) - ($txtSize * 2) ;
$py     = $height -20;
$orange = imagecolorallocate($im, 213, 134, 0);
$blue = imagecolorallocate($im, 0, 57, 141);

$im     = $image = @imagecreate($width, $height);

if ($type == 'On') {
	$background_color = $orange;
	$textcolor = $blue;
	imagestring($im, $txtSize, $px, $py, $string, $textcolor);}
elseif ($type == 'Off') {
	$background_color = $blue;
	$textcolor = $orange;
	imagestring($im, $txtSize, $px, $py, $string, $textcolor);}
else {
	$background_color = imagecolorallocate($im, 0, 0, 0);
	$textcolor = imagecolorallocate($im, 255, 255, 255);
	imagestring($im, $txtSize, $px, $py, $string, $textcolor);}

imagepng($im);
imagedestroy($im);

?>