1:search()
    1:match()方法从字符串的开头开始匹配,一旦开头不匹配,那么整个匹配就失败.
    2:因为 match() 方法在使用时需要考虑到开头的内容,这在做匹配时并不方便. 它更适合用来检测
      某个字符串是否符合某个正则表达式的规则.
    import re
    content = 'Extra strings Hello 1234567 World_This is a Regex Demo Extra strings'
    result = re.match('Hello.*?(\d+).*?Demo', content)
    print(result)

    1:search() 在匹配时扫描整个字符串,然后返回第一个成功匹配的结果. 也就是说正则表达式可以是
      字符串的一部分,在匹配时,search() 方法会依次扫描字符串,知道找到第一个符合规则的字符串.
      然后返回匹配的内容.如果搜索完了还没找到,就返回 None
    2:返回匹配正则表达式的第一个内容
    result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
    if result:
        print(result.group(1), result.group(2))




2:findall()
    1:搜索整个字符串,然后返回匹配正则表达式的所有内容




3:sub()
    1:除了使用正则表达式提取信息外,有时候还需要借助它来修改文本
    2:比如,想要把一串文本中的所有数字都去掉,如果只用字符串单独 replace() 方法,那就太麻烦了
      这时借助 sub() 方法
    3:第一个参数匹配所有的数字,第二个参数为替换成的字符串(如果去掉该参数的话,可以赋值为空),
      第三个参数时原字符串.
    import re
    content = '54aKS4yrsoiRS4ixSL2g'
    content = re.sub('\d+','', content)
    print(content)




4:compile()
    1:这个方法可以将正则字符串编译成正则表达式对象,以便在后面的匹配中复用
    2:compile() 还可以传入修饰符, 例如 re.S 等修饰符, 这样在 search(), findall() 等方法中就
      不需要额外传了,所以 compile() 方法可以说是给正则表达式做了一层封装,以便我们更好地复用
    import re
    content1 = '2016-12-15 12:00'
    content2 = '2016-12-17 12:55'
    content3 = '2016-12-22 13:21'
    pattern = re.compile('\d{2}:\d{2}')
    result1 = re.sub(pattern, '', content1)
    result2 = re.sub(pattern, '', content2)
    result3 = re.sub(pattern, '', content3)
    print(result1, result2, result3)
