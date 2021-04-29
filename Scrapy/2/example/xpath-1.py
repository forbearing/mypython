#!/usr/bin/env python3

from lxml import etree
html = etree.parse('./test.html', etree.HTMLParse())
res = etree.tostring(html)
print(res.decode("utf8"))
# 这次的输出结果略有不同，多了一个 DOCTYPE 的声明，不过对解析无任何影响
