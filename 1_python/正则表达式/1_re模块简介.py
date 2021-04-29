#!/usr/bin/env python3
import re

概述
    1:python 从1.5以后增加了 re 模块, 提供了正则表达式
    2:re 模块使得 python 拥有了全部的正则表达式功能




常见方法

1:match
    re.match(pattern, string, flags=0)
    参数:
        pattern:    匹配的正则表达式
        string:     要匹配的字符串
        flags:      标志位,用于控制正则表达式的匹配方式. re.I re.L re.M re.U re.X
                        re.I    忽略大小写
                        re.L    做本地化识别
                        re.M    多行匹配,影响'~'和'$'
                        re.S    使'.'匹配包括换行符在内的所有字符
                        re.U    根据 Unicode 字符集解析字符, 影响 '\w' '\W' '\b' '\B'
                        re.X    使我们以更灵活的格式理解表达式
    功能: 尝试从字符串的起始位置匹配一个模式, 如果不是起始位置匹配, 即使成功的话,
        也返回 None 相当于匹配失败.
    ---
    import re
    string = "www.baidu.com"
    pattern = "www"
    if(re.match(pattern, string, flags=0)):
        print("匹配成功")
    else:
        print("匹配失败")
    res = re.match("www", "WWW.baidu.com", flags=re.I)
    print(res.span())

search
    re.search(pattern, string, flags=0)
    功能: 扫描整个字符串,并返回第一个成功的匹配
    ---
    re.search("heLLo", "python hello linux hello", flags=re.I)
    print(res)
    print(res.span())

findall
    re.findall(pattern, string, flags=0)
    功能: 扫描整个字符串,并返回结果列表
    res = re.findall("hello", "hello python, hello linux, hello language")
    print(res)
    for i in res:
        print(i, end=" ")
