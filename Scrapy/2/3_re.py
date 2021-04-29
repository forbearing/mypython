1:常见的匹配模式
    \w      匹配字母数字及下划线
    \s      匹配任意空白字符,等价于 [\t\n\r\f]
    \d      匹配任意数字,等价于 [0-9]
    \A      匹配字符串开始
    \Z      匹配字符串结束,如果存在换行,只匹配到换行前的结束字符串
    \z      匹配字符串结束
    \G      匹配最后匹配完成的位置
    \n      匹配一个换行符
    \t      匹配一个制表符
    ^       匹配字符串的开头
    $       匹配字符串的末尾
    .       匹配任意字符,除了换行符,当 re.DOTALL 标记被指定时,则可以匹配包括
            换行符的任意字符
    [...]   用来表示一组字符,单独列出: [amk] 匹配 'a', 'm' 或 'k'
    [^...]  不在 [] 中的字符
    *       匹配0个或多个的表达式
    +       匹配1个或多个的表达式
    ?       匹配0个或1个由前面的正则表达式定义的片段,非贪婪方式
    {n}     精确匹配 n 个前面表达式
    [n,m]   匹配 n 到 m 次由前面的正则表达式定义的片段,贪婪方式
    a|b     匹配 a 或 b
    ()      匹配括号内的表达式,也表示一个组




re.match

    - re.match 尝试从字符串的起始位置匹配一个模式,如果不是起始位置匹配成功的话,
      match() 就返回 none.
    re.match(pattern, string, flags=0)

    === 最常规的匹配
    import re
    content = 'Hello 123 4567 World_This is a Regex Demo'
    result = re.match('^Hello\s\d{3}\s\d{4}\s\w{10}.*')
    print(result)
    print(result.group())
    print(result.span())

    === 泛匹配
    import re
    content = 'Hello 123 4567 World_This is a Regex Demo'
    result = re.match('^Hello.*Demo', content)
    print(result)
    print(result.group())
    print(result.span())

    === 匹配目标
    import re
    content = 'Hello 123 4567 World_This is a Regex Demo'
    result = re.match('^Hello\s(\d+)\sWorld.*Demo$', content)
    print(result)
    print(result.group(1))
    print(result.span())

    === 贪婪匹配
    import re
    content = 'Hello 1234567 World_This is a Regex Demo'
    result = re.match('^Hello.*World.*Demo$', content)
    print(result.group(1))

    === 非贪婪匹配
    import re
    content = 'Hello 1234567 World_This is a Regex Demo'
    result = re.match('^Hello.*?World.*Demo$', content)
    print(result.group(1))

    === 匹配模式
    import re
    content = ''' Hello 1234567 World_This
    is a Regex Demo
    '''
    result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
    print(result.group(1))

    === 转义
    import re
    content = 'price is $5.00'
    result = re.match('price is \$5\.00', content)

    === 总结
        1:尽量使用泛匹配
        2:使用括号获得匹配目标
        3:尽量使用非贪婪匹配
        4:有换行符就用re.S




re.search
    re.search 扫描整个字符串返回第一个成功的匹配

    import re
    content = 'Extra strings Hello 1234567 World_This is a Regex Demo Extra Stings'
    result = re.match('Hello.*?(\d+).*?demo', content)
    result = re.search('Hello.*?(\d+).*?Demo', content)
    print(result.string)



re.findall
    搜索字符串,以列表返回全部能匹配的子串



re.sub
    替换字符串中每一个匹配的子串后返回替换后的字符串

    import re
    content = 'Extra strings Hello 1234567 World_This is a Regex Demo Extra Stings'
    content = re.sub('\d+', '', content)
    print(content)

    import re
    content = 'Extra strings Hello 1234567 World_This is a Regex Demo Extra Stings'
    content = re.sub('\d+', 'wokao', content)
    print(content)

    import re
    content = 'Extra strings Hello 1234567 World_This is a Regex Demo Extra Stings'
    content = re.sub('(\d+)', r'\1 890', content)
    print(content)



re.compile
    把正则表达式编译成在正则表达式对象
    将一个正则表达式编译成正则对象, 以便于复用该匹配模式

    import re
    content = '''Hello 1234567 World_This
    is a Regex Demo
    '''
    pattern = re.compile('Hello.*Demo', re.S)
    result = re.match(pattern, content)
    print(result)
