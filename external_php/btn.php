<?php

header("Content-type: image/png");
$state = $_GET['state'];
$type = $_GET['type'];
//$txtSize = 5;
$height = 75;
$width = $height;
//$px     = ($width - 7.5 * strlen($string)) / 2;
//$py     = (imagesy($im) / 2) - ($txtSize * 2) ;
$py     = $height -22;
$orange = imagecolorallocate($im, 231, 185, 56);
$blue = imagecolorallocate($im, 50, 142, 206);

$im = @imagecreate($width, $height);

if ($type == 'GPIO' && $state == 1) {
	$background_color = imagecolorallocate($im, 231, 185, 56);
	$txtcolor = imagecolorallocate($im, 50, 142, 206);
	$txtSize = 5;
	$txtstring = 'ON';
	$px     = ($width - 8 * strlen($txtstring)) / 2;
	imagestring($im, $txtSize, $px, $py, $txtstring, $txtcolor);
	}
elseif ($type == 'GPIO' && $state == 0) {
	$background_color = imagecolorallocate($im, 50, 142, 206);
	$txtcolor = imagecolorallocate($im, 231, 185, 56);
	$txtSize = 5;
	$txtstring = 'OFF';
	$px     = ($width - 8 * strlen($txtstring)) / 2;
	imagestring($im, $txtSize, $px, $py, $txtstring, $txtcolor);
	}
elseif ($type == 'Temp' && $state == 1) {
	$background_color = imagecolorallocate($im, 231, 185, 56);
	$txtcolor = imagecolorallocate($im, 50, 142, 206);
	}
elseif ($type == 'Temp' && $state == 0) {
	$background_color = imagecolorallocate($im, 50, 142, 206);
	$txtcolor = imagecolorallocate($im, 231, 185, 56);
	$txtSize = 3;
	$txtstring = 'Err';
	$px     = ($width - 8 * strlen($txtstring)) / 2;
	imagestring($im, $txtSize, $px, $py, $txtstring, $txtcolor);
	}
elseif ($type == 'Script' && $state == 1) {
	$background_color = imagecolorallocate($im, 231, 185, 56);
	$txtcolor = imagecolorallocate($im, 50, 142, 206);
	$txtSize = 5;
	$txtstring = 'Up';
	$px     = ($width - 8 * strlen($txtstring)) / 2;
	imagestring($im, $txtSize, $px, $py, $txtstring, $txtcolor);
	}
elseif ($type == 'Script' && $state == 0) {
	$background_color = imagecolorallocate($im, 50, 142, 206);
	$txtcolor = imagecolorallocate($im, 231, 185, 56);
	$txtSize = 5;
	$txtstring = 'Dwn';
	$px     = ($width - 8 * strlen($txtstring)) / 2;
	imagestring($im, $txtSize, $px, $py, $txtstring, $txtcolor);
	}
else {
	$background_color = imagecolorallocate($im, 0, 0, 0);
	$txtcolor = imagecolorallocate($im, 255, 255, 255);
	}


imagepng($im);
imagedestroy($im);

?>