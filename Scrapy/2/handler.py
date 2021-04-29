#!/usr/bin/env python3


# 代理
# import urllib.request
# proxy = urllib.request.ProxyHandler({
    # 'http': 'http://127.0.0.1:1080',
    # 'https': 'https://127.0.0.1:1080',
    # 'socket': 'socket://127.0.0.1:1080'
    # })
# opener = urllib.request.build_opener(proxy)
# res = opener.open('https://www.baidu.com')
# print(res.read())




# # Cookie
# import urllib.request, http.cookiejar
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# res = opener.open('https://www.google.com')
# for item in cookie:
    # print(item.name + ' = ' + item.value)

# import http.cookiejar, urllib.request
# filename = 'cookie.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# res = opener.open('https://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)

# import http.cookiejar, urllib.request
# filename = 'cookie2.txt'
# cookie = http.cookiejar.LWPCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# res = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)

import http.cookiejar,urllib.request
cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookie2.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
res = opener.open('http://www.baidu.com')
print(res.read().decode('utf8'))
