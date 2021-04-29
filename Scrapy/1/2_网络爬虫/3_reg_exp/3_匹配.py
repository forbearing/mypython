1:匹配目标
    1:使用 () 括号将想要提取的字符串括起来, () 实际上标记了一个子表达式的开始和结束位置,
      被标记的每个子表达式会依次对应每一个分组,调用 group() 方法传入分组的索引即可获取
      提取的结果
    import re
    content = 'Hello 1234567 World_This is a Regex Demo'
    result = re.match('^Hello\s(\d+)\sWorld', content)
    print(result)
    print(result.group())
    print(result.group(1))
    print(result.span())




2:通用匹配
    1:有一个万能匹配可以用,那就是.*, .(点)可以匹配任意字符(除了换行符). *(星)代表匹配的
      字符无限次,所以它们组合在一起就可以匹配任何字符了.
    import re
    content = 'Hello 123 456 World This is a Regex Demon'
    result = re.match('^Hello.*Demo', content)
    print(result)
    print(result.group(1))
    print(result.span())




3:贪婪与非贪婪
    1:在贪婪模式下, .* 会匹配尽可能多的字符,正则表达式中 .* 后面时 \d+, 也就是至少一个数字,
      并没有指定具体多少个数字,因此 .* 就尽可能匹配多的字符,这里 .* 就把 123456 也匹配了,
      给 \d+ 留下一个可满足条件的数字7,
    import re
    content = 'Hello 123456 World This is a Regex Demon'
    result = re.match('^He.*(\d+).*Demo$', content)
    
    1:非贪婪模式的写法 .*?
    2:非贪婪模式匹配就是尽可能匹配少的字符. 当 .*? 匹配到 Hello 后面的空白字符时,再往后的字符
      就是数字了, 而 \d+ 恰好可以匹配,那么 .*? 就不再进行匹配了,交给 \d+ 去匹配后面的数字,
      这样 .*? 匹配了尽可能少的字符.
    3:在做匹配的时候,字符串中间尽可能使用非贪婪匹配.
    4:需要注意,如果匹配的结果在字符串结尾, .*? 就可能匹配不到任何内容了.因为它会匹配尽可能
      少的内容.
    import re
    content = 'Hello 123456 World This is a Regex Demon'
    result = re.match('^He.*?(\d+).*Demo$', content)
    print(result)
    print(result.group(1))
    print(result.span())




4:修饰符
    import re
    content = '''Hello 1234567 World_This
    is a Regex Demo
    '''
    result = re.match('He.*?(\d+).*?Demo$', content)
    print(result.group(1))
    # 运行直接报错,正则表达式没有匹配到这个字符串,返回结果为 None,
    # 这是因为 . 匹配的是除换行符之外的任意字符,当遇到换行符时 .*? 就不能匹配了.
    
    1:只需要加一个修饰符 re.S 即可修正这个错误, 这个修饰符的作用就是使 . 匹配包括换行符
      在内的所有字符.
    2:这个 re.S 在网页匹配中经常用到,因为 HTML 节点经常会有换行
    3:其他的一些修饰符
        re.I        使匹配对大小写不敏感
        re.L        做本地化识别(locale-aware)匹配
        re.M        多行匹配,影响 ^ 和 $
        re.S        使 . 匹配包含换行在内的所有字符
        re.U        根据 Unicode 字符集解析字符.这个标志影响 \w \W \b \B
        re.X        该标志通过给予你更灵活的格式以便你将正则表达式写的更于理解
    4:在网页匹配中,较为常用的有 re.S 和 re.I
    result = re.match('^He.*?(\d+).*?Demo$', content, re.S)




5:转移匹配
    1:当遇到用于正则表达式匹配模式的特殊字符时,在前面加反斜线转移一下即可,例如
      可以用 \. 来匹配
