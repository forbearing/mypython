#!/bin/env python3

from urllib import request,error
try:
    res = request.urlopen('https://hybfkuf.com/index.html', timeout=0.01)
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print("Request Successfully")
