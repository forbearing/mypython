#!/usr/bin/env python3

import urllib.request
import json

r = urllib.request.urlopen('http://httpbin.org/get')

# 读取 response 的内容
print(r.status, r.reason)

# 返回的内容是 Json 格式，直接 load 函数加载
text = r.read()
obj = json.loads(text)
print(obj)

# r.headers 是一个 HTTPMessage 对象
print(r.headers)
for k,v in r.headers._headers:
    print("%s: %s" %(k,v))
