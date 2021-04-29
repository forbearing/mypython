#!/bin/env python3

import requests
headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }
res = requests.get('https://www.zhihu.com/explore', headers=headers)
print(res.text)
