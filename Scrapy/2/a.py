#!/usr/bin/env python3

# import urllib.request
# res = urllib.request.urlopen('http://www.win4000.com')
# print(res.read().decode('utf-8'))


# import urllib.request
# import urllib.parse
# data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding='utf8')
# res = urllib.request.urlopen('http://httpbin.org/post', data=data)


# import urllib.request
# res = urllib.request.urlopen('http://httpbin.org/get', timeout=1)
# print(res.read())


# import socket
# import urllib.request
# import urllib.error
# try:
    # response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# except urllib.error.urlerror as e:
    # if isinstance(e.reason, socket.timeout):
        # print("time out")


# import urllib.request
# res = urllib.request.urlopen('https://www.python.org')
# print(type(res))


# import urllib.request
# res = urllib.request.urlopen('https://www.python.org')
# print(res.status)
# print(res.getheaders())
# print(res.getheader('server'))


# import urllib.request
# res = urllib.request.urlopen('https://www.python.org')
# #print(res.read().decode('utf8'))
# print(res.read())



# =============  request =============

# import urllib.request
# req = urllib.request.request('https://www.python.org')
# res = urllib.request.urlopen(req)
# print(res.read().decode('utf8'))

# from urllib import request,parse
# url = 'http://httpbin.org/post'
# headers = {
        # 'user-agent': 'mozilla/4.0(compatible; msie 5.5; windows nt)',
        # 'host': 'httpbin.org'
        # }
# dict = {
        # 'name': 'germey'
        # }
# data = bytes(parse.urlencode(dict), encoding='utf8')
# req = request.request(url=url, data=data, headers=headers, method='post')
# res = request.urlopen(req)
# print(res.read().decode('utf8'))

# import urllib.request
# proxy_handler = urllib.request.proxyhandler({
    # 'http': '127.0.0.1:1080',
    # 'https': '127.0.0.1:1080'
    # })
# opener = urllib.request.build_opener(proxy_handler)
# res = opener.open('http://httpbin.org/get')
# print(res.read())

# import http.cookiejar, urllib.request
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# res = opener.open('http://www.baidu.com')
# print(cookie)
# for item in cookie:
    # print(item.name + " = " + item.value)

# import urllib.request, http.cookiejar
# cookie = http.cookiejar.LWPCookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# res = opener.open('https://www.baidu.com')
# print(res.read().decode('utf8'))




# 异常处理

# from urllib import error, request
# try:
    # request.urlopen('http://hybasia.com/wokao.txt')
# except error.URLError as e:
    # print(e.reason)
# else:
    # print('Request Successfully')

import socket
import urllib.request
import urllib.error
try:
    res = urllib.request.urlopen('http://www.baidu.com', timeout=0.01)
except urllib.error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print("TIME OUT")
