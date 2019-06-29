#!/usr/bin/env php
<?php
	if ($argc == 2)
	{
		$handle = fopen($argv[1], 'r');
		while (!feof($handle))
		{
			$text = fgets($handle);
			$text = preg_replace_callback('/<a.*?title="(.*?)">/', function ($matches) {
                /* print_r("matches0: $matches[0]\n");
                print_r("matches1: $matches[1]\n"); */
                return (str_replace($matches[1], strtoupper($matches[1]), $matches[0]));
                /* str_replace ( mixed $search , mixed $replace , mixed $subject [, int &$count ] ) : mixed */
            }, $text);            
			$text = preg_replace_callback('/<a.*?>(.*?)</', function ($matches) {
				return (str_replace($matches[1], strtoupper($matches[1]), $matches[0]));
			}, $text);
			echo $text;
		}
	}
?>