html = '''
v id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0 active"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''

from pyquery import PyQuery as pq
doc = pq(html)
print(doc('#container .list li'))
print(type(doc('#container .list li')))

# 初始化 PyQuery 对象之后, 传入了一个 CSS 选择器 #container .list li, 它的意思时先选取
# id 为 container 的节点, 然后再选取内部的 class 为 list 的节点内部的所有 li 节点,
# 最后打印输出
