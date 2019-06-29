

curl -c cook.txt 'localhost:8100/ex03/cookie_crisp.php?action=set&name=plat&value=choucroute'

curl -c cook.txt 'localhost:8100/ex03/cookie_crisp.php?action=del&name=plat'
curl 'localhost:8100/ex04/raw_text.php'
lynx -dump 'localhost:8100/ex04/raw_text.php'
curl --head localhost:8100/ex05/read_img.php
curl --user zaz:jaimelespetitsponeys localhost:8100/ex06/members_only.php

    curl -v --user root:root localhost:8100/ex06/members_only.php


curl -v -c cook.txt 'localhost:8100/d04/ex00/index.php'

curl -v -b cook.txt 'localhost:8100/d04/ex00/index.php?login=sb&passwd=beeone&submit=OK'
curl -v cook.txt 'localhost:8100/d04/ex00/index.php'
