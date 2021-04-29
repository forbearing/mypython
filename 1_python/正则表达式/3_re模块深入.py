import re

re.split
    功能: 字符串切割
    string = "hello     welcome to my channel"
    print(string.split(" "))
    print(re.split(r" +", string))


re.finditer
    re.finditer(pattern, string, flags=0)
    功能: 与 findall 类似,扫描整个字符串, 返回的是一个迭代器
    ---
    string = "hello python hello linux"
    myiter = re.finditer(r"(hello)", string)
    while True:
        try:
            print(next(myiter))
        except StopIteration as e:
            break

re.sub
re.subn
    re.sub(pattern, repl, string, count=0, flags=0)
    re.subn(pattern, repl, string, count=0, flags=0)
    repl: 指定的用来替换的字符串
    string: 目标字符串
    count: 最多替换次数
    功能: 在目标字符串中以正则表达式的规则匹配次字符串, 再把他们替换成指定的字符串.
        可以指定替换次数,如果不指定,替换所有的匹配字符串
        sub 返回被替换的字符串
        subn 返回元组, 第一个元素为被替换的字符串, 第二个元素为被替换的次数
    ---
    string = "hybfkuf is a good good good man"
    res1 = re.sub(r"(good)", "nice", string)
    res2 = re.subn(r"(good)", "nice", string)
    print(res)
    print(type(res))


分组
    概念: 除了简单判断是否匹配之外, 正则表达式还有提取子串的功能. 
        用 () 表示提取出来的分组
    ---
    string = "010-12345678"
    res = re.match(r"(\d{3})-(\d{8})", string)
    print(res)
    print(res.group(0))                 # group(0) 一直代表的是原始字符串
    print(res.group(1))
    print(res.group(2))
    print(res.groups())                 # 返回元组
    ---
    string = "010-12345678"
    res = re.match(r"(?P<first>\d{3})-(?P<second>\d{8})", string)
    print(res.group("first"))
    print(res.group("second"))


编译
    概念: 当我们使用正则表达式时, re 模块会干两件事
        1:编译正则表达式, 如果正则表达式本身不合法,会报错
        2:用编译后的正则表达式去匹配对象
    re.compile(pattern, flags=0)
    ---
    string = "010-12345678"
    pattern = r"(\d{3})-(\d{8})"
    re_phone = re.compile(pattern)
    res = re_phone.matcch(string)
    print(res.group(0))
    print(res.group(1))
    print(res.group(2))
