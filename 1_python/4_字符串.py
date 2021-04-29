1:概念:
    1:以单引号或双引号扩起来的任意文本
    2:字符串是不可变的
2:字符串运算
    str1 = "Hello Linux"
    str2 = "Hello Python"
    str3 = str1 + str3
3:输出重复字符串
    str4 = "hello"
    print(str4 * 3)
4:字符串索引下标，访问某一字符
    str5 = "Hello Python"
    print(str5[4])
5:字符串截取
    str1 = "Hello linux, Hello python"
    print(str1[2:7])                # 包含2，不包含7
    print(str1[:7])                 # 从头截取到给定下标之前
    print(str1[7:])                 # 从给定下标处开始截取到结尾
6:格式化输出
    print("num =", num)             # 逗号产生空格
    print("num = %d" %(num))
    print("num = %d, str = %s" %(num, str1))
    print("num = %d, str = %s f = %f" %(num, str1, f))
    print("num = %d\nstr = %s\nf = %f" %(num, str1, f))
    print("f = %.3f" %f)            # 精确到小数点后三位，还会四舍五入
    print('''
        Hello Linux
        Hello Python
        ''')
    print(r"C:\\Uses\hybfkuf\Desktop\file.txt")     # 当个存在多个转义符





常用方法

    eval(string)
        功能: 将字符串 string 当成有效的表达式来求值并返回计算结果
        num = eval("123")
        print(eval("+123"))                         # 正确
        print(eval("1+2"))                          # 正确，结果位3
        print(eval("2-1"))
        print(eval("1a2"))                          # 报错
    len(string)
        功能: 返回字符串的长度
        len(str1)

    string.lower()
        功能: 转换字符串中的大写字母为小写字母
        string.lower()
    string.upper()
        功能: 转换字符串中的小写字母为大写字母
    string.swapcase()
        功能: 转换大小写
    string.capitalize()
        功能: 首字母大写，其他字母为小写
    string.title()
        功能: 每个单词的首字母大写，其他字母不变

	string.center(width[, fillchar])
        功能: 返回一个指定宽度的居中字符串，fillchar 为填充的字符串，默认空格填充
        string.center(40, "*")
    string.ljust(width [,fillchar])
        功能: 返回一个指定宽度的左对齐字符串，fillchar 为填充的字符串，默认空格填充
        string.ljust(40)
        string.ljust(40, "*")
    string.rjust(width [,fillchar])
        功能: 返回一个指定宽度的右对齐字符串，fillchar 为填充的字符串，默认空格填充
        string.rjust(40)
        string.rjust(40,"*")
    string.zfill(width)
        功能: 返回一个长度为 width 的右对齐字符串，默认用0填充
        string.zfill(40)

    string.count(str,start=0,end=len(string))
        功能: 返回 str 在 start 和 end 之间在 string 里面出现的次数,默认从头到尾
        string.count("Hello")
        string.count("hello", 15, len(string))
    string.find(str,start=0,end=len(string))
        功能: 检查字符串是否包含在 string 中，如果是返回开始的索引值，否则返回-1
        string.find("Python")
        string.find("Python", 10, len(string))
    string.rfind()
        string.rfind("Hello", 10, len(string))
    string.index(str1, start=0, end=len(string))
        功能: 跟 find 一样，只不过如果 str1 找不到会报一个异常
        string.index("Hello")
        string.index("Hello", 10, len(strin))
    string.rindex()
        功能: 同 string.index()，不同是从右边往左查找

    string.strip()
        功能: 截掉字符串两侧指定的字符，默认为空格
        str1 = "Hello Linux, heLLo Python"
        str2 = str1.ljust(40)
        str3 = str2.strip()
        string.strip("*")
    string.lstrip()
        功能: 截掉字符串左侧指定的字符，默认为空格
    string.rstrip()
        功能: 截掉字符串右侧指定的字符，默认为空格
    string.replace(str1, str2, count)
        功能: 把 string 中的 str1 替换成 str2，如果 count 指定，泽替换不超过 count 次
    string.split(tr="str1",  maxsplit)
        功能: 以 str1 为分隔符切片 string,如果 maxsplit 有指定值，则分割maxsplit 个字符串
        string.split(".")
    string.startwith("str1")
        功能: 检查字符串是和否以 "str1" 开头，是则返回 True，否则返回 False
    string.endwith("str1")
        功能: 检查字符串是否是以 obj 结束，如果是返回 True，否则返回 False



其他
    字符串比较
        从第一个字符开始比较，谁的 ASCII 值大谁就大，如果相等则会比较下一个字符的
        ASCII 值大小。那么谁的值就大
        print("str1" > "str2")
        print(str1 > str2)
        print(str == str2)          # 错误
        print("str2" == "str2")     # 正确
