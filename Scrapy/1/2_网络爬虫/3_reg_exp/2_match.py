1:概述
    1:向它传入要匹配的字符串以及正则表达式,就可以检测这个正则表达式是否匹配字符串
    2:match() 方法会尝试从字符串的起始位置匹配正则表达式,如果匹配就返回匹配成功的结果,
      如果不匹配,就会返回 None



2:
    import re
    content = 'Hello 123 4567 World_This is a Regex Demo'
    print(len(content))
    result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}',content)
    print(result)
    print(result.group())
    print(result.span())

    1:match() 方法中,第一个参数传入正则表达式,第二个参数传入要匹配的字符串.
    2:match() 的结果时 SRE_Match 对象, 该对象有两个方法, group() 方法可以输出匹配到的内容,
      span() 方法可以可以输出匹配的范围.
    3:result.group(1) 会输出第一个被 () 包围的匹配结果,如果正则表达式后面还有()包括的内容,
      那么就可以依次使用 group(2) ,group(3) 等来获取
