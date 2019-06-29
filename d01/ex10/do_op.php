#!/usr/bin/env php
<?php  
	
	$n1 = trim($argv[1]);	
	$operator = trim($argv[2]);	
	$n2 = trim($argv[3]);
	$rezult = 0;
	switch ($operator) {
		case '+':
			$result = $n1 + $n2;
			echo ($result."\n");
			break;
		case '-':
			$result = $n1 - $n2;
			echo ($result."\n");
			break;
		case '*':
			$result = $n1 * $n2;
			echo ($result."\n");
			break;
		case '/':
			$result = $n1 / $n2;
			echo ($result."\n");
			break;
		case '%':
			$result = $n1 % $n2;
			echo ($result."\n");
			break;
		default:
			echo ($result."\n");
			break;
	}
?>