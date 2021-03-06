1:ajax
    1:有时候通过浏览器和 requesets 获取的页面数据不同.这是因为 requests 获取的时原始的 
      html 文档, 而浏览器中的页面是经过 JavaScript 处理数据后生成的结果.
    2:这种数据的来源有很多种, 可能是通过 Ajax 加载的,可能时包含在 HTML 文档中, 也可能是
      经过 JavaScript 和特定算法计算后生成的.
    3:通过 Ajax 加载: 数据加载是一种异步加载方式,原始的页面最初不会包含某些数据.原始页面
      加载完后,会再向服务器请求某个接口获取数据,然后数据才被处理从而呈现到网页上,这其实
      就是发送了一个 Ajax 请求




2:什么是 Ajax
    1:Asynchronous JavaScript and XML, 异步的 JavaScript 和 XML. 它不是一门编程语言,而是
      利用 JavaScript 在保证页面不被刷新,页面链接不改变的情况下与服务器交换数据并更新
      部门网页的技术.
    2:对于传统网页, 如果想要更新其内容,那么必须要刷新整个页面,但有了 Ajax, 便可以在页面不被
      全部刷新的情况下更新其内容. 在这个过程中,页面实际上是在后台与服务器进行了数据交互,
      获取到数据之后, 再利用 JavaScript 改变网页,这样网页内容就会更新了
    3:基本原理
        1:发送请求
        2:解析内容
        3:渲染网页
