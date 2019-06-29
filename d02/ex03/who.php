#!/usr/bin/env php

<?php
    $fd = fopen("/var/run/utmpx", 'r');
    date_default_timezone_set("Pacific/Easter");
    while ($str = fread($fd, 628)) {
        
        $elem = unpack("a256user/a4id/a32line/ipid/itype/Itime", $str);
        //unpack — Unpack data from binary string
        //print_r($elem);
        if ($elem['type'] == 7) {
            echo "$elem[user] $elem[line]  ". date('M  j H:i', $elem['time'])."\n";
        }
    }
?>