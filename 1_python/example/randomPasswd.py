#!/usr/bin/env python3

import random
from random import choice
import string

def genePasswd1():
    passwd = ""
    for i in range(12):
        ty = random.randrange(3)
        if ty == 0:             # 随机生成一个大写字母
            ch = chr(random.randrange(ord('A'), ord('Z')+1))
            passwd += ch
        elif ty == 1:           # 随机生成一个小写字母
            ch = chr(random.randrange(ord('a'), ord('z')+1))
            passwd += ch
        else:                   # 随机生成一个数字
            ch = chr(random.randrange(ord('0'), ord('9')+1))
            passwd += ch
    return passwd

def genePasswd2(length=12, 
        chars=string.ascii_letters+string.digits+string.punctuation):
    return ''.join([choice(chars) for i in range(length)])


passwd1 = genePasswd1()
print(passwd1)
passwd2 = genePasswd2(12)
print(passwd2)
