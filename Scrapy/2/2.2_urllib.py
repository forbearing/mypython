#!/usr/bin/env python3

import urllib.request
import sys
import time
import random

=== urllib.request.urlopen
#res.read()          读取文件的全部内容，会把读取到的数据赋值给一个字符串变量
#res.readline()      读取一行
#res.readlines()     读取文件的全部内容，会把读取到的数据赋值给一个列表变量

url = "https://www.baidu.com"
res = urllib.request.urlopen(url)
data = res.read()
data = res.readline()
data = res.readlines()



=== urllib.request.urlretrieve
# urlretrieve 在执行过程中，会产生一些缓存，使用之后可以清楚缓存 urlcleanup(
# urllib.request.urlcleanup() 清除缓存
url = "https://www.baidu.com"
filepath = "/Users/jonas/Desktop/wokao.html"
urllib.request.urlretrieve(url, filepath)
urlib.request.urlcleanup()



=== 方法和属性
res.info()              # 返回当前环境的有关信息
res.getcode()           # 返回状态吗
if res.getcode() == 200 or res.getcode() == 304:
    pass

res.geturl()            # 返回当前正在爬去的 url 地址

url = "http://www.baidu.com/s?wd=%E9%94%AE%E7%9B%98%E9%80%89%E6%8B%A9&rsv_spt=1&rsv_iqid=0xf8097f490004218e&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=ib&rsv_sug3=20&rsv_sug1=4&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&inputT=7866&rsv_sug4=7866"
newUrl = urllib.request.unquote(url)        # 解码
newUrl2 = urlib.request.quote(newUrl)       # 编码



=== urllib.request.Request
headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:76.0) Gecko/20100101 Firefox/76.0"
        }
req = urllib.request.Request(url, headers=headers)          # 设置一个请求体
res = urllib.request.urlopen(req)
print(res.read().decode('utf8'))

agentList = []
agentStr =  random.choice(agentList)
req = urllib.request.Request(url)
req.add_header("User-Agent": agentStr)
res = urllib.request.urlopen(req)
print(res.read().decode('utf8'))
