#!/bin/env python3

import re
import requests




first_url = "http://www.win4000.com/meinv197289_"
last_url = ""
for num in range(1,12):
    # 1:构造需要爬取图片的网址
    last_url = str(num)+".html"
    base_url = first_url + last_url
    
    # 2:解析出图片下载地址
    content = requests.get(base_url).text
    url = re.findall('img.*?class="pic-large".*?url="(.*?)".*?', content, re.S)
    url = url[0]

    # 3:获取图片并保存
    meitu = requests.get(url)

    with open(str(num)+'.jpg', 'wb') as f:
        f.write(meitu.content)
        f.close()

