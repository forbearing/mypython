#!/usr/bin/env python3

import time
import requests
import re
import signal
import sys

def handler(signum, frame):
    if signum == signal.SIGINT:
        print("Ctrl-C, exit ...")
        sys.exit()
signal.signal(signal.SIGINT, handler)


base_url = ""
first_url = "http://www.win4000.com/meinv"

for x in range(200000,201000):
    second_url = first_url+str(x)
    for y in range(1,12):
        base_url = second_url + "_" + str(y) + ".html"
        print(base_url)
        try:
            content = requests.get(base_url).text
            #item = re.findall('img class="pic-large" src="(.*?)".*?', content, re.S)
            item = re.findall('img.*?class="pic-large".*?url="(.*?)".*?', content, re.S)
            true_url = item[0]
            print(true_url)

            meitu = requests.get(true_url)
            path = "/Users/jonas/Desktop/images/win4000/" + str(x) + "_" + str(y) + ".jpg"
            with open(path, 'wb') as f:
                f.write(meitu.content)
        except IndexError as e:
            print("IndexError, continue")
            continue
