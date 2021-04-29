1:CSS 选择器之所以强大，还有一个很重要的原因。那就是它支持多种多样的伪类选择器，
  例如，选择第一个节点、最后一个节点、奇偶数节点、包含某一文本的节点等

html = '''
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second items</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
print(doc('li:first-child'))            # 第一个 li 节点
print(doc('li:last-child'))             # 最后一个 li 节点
print(doc('li:nth-child(2)'))           # 第二个 li 节点
print(doc('li:gt(2)'))                  # 第三个 li 之后的 li 节点
print(doc('li:nth-child(2n)'))          # 偶数位的 li 节点
print(doc('li:contains(second)'))       # 包含 second 文本的 li 节点
