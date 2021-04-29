#!/bin/env python3
import re


1:匹配单个字符
    .       匹配除换行符以外的任意字符
    []      字符集合, 表示匹配方括号中所包含的任意个字符, [a-z], "-" 可以表示一段范围
            "[0-9a-zA-Z]"  匹配任意数字和字母
            "[0-9a-ZA-Z_]"  匹配任意数字,字母和下划线
    [^]     "^" 称为脱字符, 表示不匹配集合中的字符
            "[^0-9]"  匹配除了数字之外的所有字符

    \d      匹配数字, 效果同 [0-9]
    \D      匹配非数字, 效果同 [^0-9]
    \w      匹配数字,字母和下划线, 效果同 "[0-9a-zA-Z_X]"
    \W      匹配非数字,字母和下划线, "[^0-9a-zA-Z_X]"
    \s      匹配任意的空白符(空格,换行,回车,换页,制表符),效果同 "[ \f\n\r\t]"
    \S      匹配任意的非空白符, 效果同"[^ \f\n\r\t]"


2:锚字符(边界字符)
    ^       行首匹配, 和 [] 里面的 "^" 不是一个意思
    $       行尾匹配
    \A      匹配字符串开始, 它和 ^ 的区别是, \A 只匹配整个字符串的开头, 即使在
            re.M 模式下,也不会
            res1 = re.findall("^hello", "hello python\nhello linux", re.M)
            print(res1)
            res2 = re.findall("\Ahello", "hello python\nhello linux", re.M)
    \Z      匹配字符串结束, 与 $ 有区别
    \b      匹配一个单词的边界,也就是指单词和空格间的位置
            res = re.findall(r"ux\b", "hello python hello linux")
    \B      匹配非单词边界


3:多个字符
    (xyz)       匹配小括号内的 xyz (作为一个整体去匹配)
    x?          匹配0个或1个x
    x*          匹配0个或者任意多个x
    x+          匹配至少1个x
                print(re.findall(r"a?", "aaa"))     # 非贪婪匹配, 尽可能少的匹配
                print(re.findall(r"a*", "aaabaa"))  # 贪婪匹配, 尽可能多的匹配
                print(re.findall(r"a+", "aaabaa"))  # 贪婪匹配,尽可能多的匹配
    x{n}        匹配确定的n个x (n是一个非负整数)
    x{n,}       匹配至少n个x
    x{n,m}      匹配至少n个,最多m个x.
    x|y         |表示活,匹配的是x或y

4:特殊
    *?  +?  ??      最小匹配,非贪婪匹配,通常都是尽可能多的模式
        string = "hybfkuf is a good man! hybfkuf is a nice man! hybfkuf is a handsome man"
        print(re.findall(r"hybfkuf.*?man", string))     # 匹配到3个
        print(re.findall(r"hybfkuf.*man", string))      # 匹配到1个
    (?:x)           类似(xyz),但是不表示一个组

