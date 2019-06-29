#!/usr/bin/env php
<?php  
	function ft_split($str)
	{
		$word = explode(" ", $str);
		$sort_word = array_values(array_filter($word));
		return ($sort_word);
	}
	function custom_sort($i, $j)
	{
		if (ctype_alpha($i[0]) && ctype_alpha($j[1]))
			return (strcasecmp($i, $j));
		if (ctype_digit($i[0]) && ctype_digit($b[0]))
			return ($i > $j ? 1 : ($i == $j ? 0 : -1));
		return ($ret < 0 ? 1 : ($ret == 0 ? 0 : -1));
	}
	function ssap2($str)
	{
		$args = $str;		
		reset($args);
		$key = key($args);		
		print_r($key);
		unset($args[$key]);
		$result = array();
		foreach ($args as $arg)
		{
			$array = explode(" ", $arg);
			$result = array_merge($result, $array);
        }       

		sort($result, "custom_sort");
		foreach ($result as $word)
		{
			echo $word."\n";
		}
	}
	ssap2($argv);	
?>