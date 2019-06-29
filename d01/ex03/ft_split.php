#!/usr/bin/env php
<?php  
	function ft_split($str)
	{
		$word = explode(" ", $str);
		print_r($word);
		$sort_word = array_values(array_filter($word));
		sort($sort_word);
		return ($sort_word);
	}
	print_r(ft_split(" dff 112 llo "))
?>

<!--
explode — Split a string by a string
array_filter — Filters elements of an array using a callback function
array_values — Return all the values of an array
sort — Sort an array
-->