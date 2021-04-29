#!/usr/bin/env python3

# import requests
# res = requests.get('https://www.baidu.com')
# print(type(res))
# print(type(res.text))
# print(res.status_code)
# print(res.cookies)
# print(res.text)

# import requests
# import json
# data = {
        # 'name': 'hybfku',
        # 'age': 23
        # }
# res = requests.get('http://httpbin.org/get', params=data)
# print(res.json())
# print(json.loads(res.text))

# import requests
# data = {
        # 'name': 'hybfkuf',
        # 'age': 23
        # }
# res = requests.post('http://httpbin.org/post', data=data)
# print(res.text)

# import requests
# res = requests.get('https://www.baidu.com')
# print(type(res.status_code), res.status_code)
# print(type(res.headers), res.headers)
# print(type(res.cookies), res.cookies)
# print(type(res.url), res.url)
# print(type(res.history), res.history)

# import requests
# res = requests.get('https://www.baidu.com')
# if res.status_code == requests.codes.ok:
    # print("Request Success")
# else:
    # print("Request Failure")

# import requests
# files = {'file': open('hello.txt', 'rb')}
# res = requests.post('http://httpbin.org/post', files=files)
# print(res.text)

# import requests
# res = requests.get('https://www.baidu.com')
# print(res.cookies)
# for key,value in res.cookies.items():
    # print(key + '=' + value)

# import requests
# requests.get('http://httpbin.org/cookies/set/number/123456789')
# response = requests.get('http://httpbin.org/cookies')
# print(response.text)
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# response = s.get('http://httpbin.org/cookies')
# print(response.text)

# import requests
# from requests_packages import urllib3
# res = requests.get('https://www.12306.cn')
# print(res.status_code)

# urllib3_disable_warnings()
# res = requests.get('https://www.12306.cn', verify=False)
# print(res.status_code)

import requests
from requests.exceptions import ReadTimeout
try:
    res = requests.get('https://taobao.com', timeout=1)
    print(res.status_code)
except ReadTimeout:
    print('TIMEOUT')
