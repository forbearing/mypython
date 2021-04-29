#!/bin/env python3

import re
import requests




first_url = "http://www.win4000.com/meinv197289_"
last_url = ""
for i in range(1,12):
    last_url = str(i)+".html"
    url = first_url + last_url
    content = requests.get(url).text
    mycontent = re.findall('img.*?class="pic-large".*?url="(.*?)".*?', content, re.S)

    urlfile  = open('url.txt', 'w+')
    for url in mycontent:
        urlfile.write(url)
        urlfile.write('\n')
    urlfile.close()
