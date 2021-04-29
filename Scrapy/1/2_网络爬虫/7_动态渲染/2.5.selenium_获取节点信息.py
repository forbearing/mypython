1:获取节点信息
    1:前面,通过 page_source 属性可以获取网页的源代码,接着可以使用解析库(如正则表达式,
      Beautiful Soup, pyquery 等)来提取信息.
    2:既然 Selenium 已经提供了选择节点的方法,返回的是 WebElement 类型.那么它也有相关的
      方法和属性来直接提取节点信息, 如属性,文本等.
    3:这样就不需要通过解析源代码来提取信息了,非常方便




2:获取属性
    1:使用 get_attribute() 方法来获取节点的属性,但是其前提是先选中这个节点.
    from selenium import webdriver
    from selenium.webdriver import ActionChains
    browser = webdriver.Chrome()
    url = 'https://www.zhihu.com/explore'
    browser.get(url)
    logo = browser.find_element_by_id('zh-top-link-logo')
    print(logo)
    print(logo.get_attribute('class'))
    # 传入想要获取的属性名, 就可以得到它的值了.




3:获取文本值
    1:每个 WebElement 节点都有 text 属性,直接调用这个属性就可以得到节点内部的文本信息.
      这相当于 Beautiful Soup 的 get_text() 方法, pyquery 的 text() 方法
    from selenium import webdriver
    browser = webdriver.Chrome()
    url = 'https://www.zhihu.com/explore'
    input = browser.find_element_by_class_name('zu-top-add-question')
    print(input.text)




3:获取 id,位置,标签名和大小
    1:另外, WebElement 节点还有一些其他属性, 比如 id 属性可以获取节点id, location 属性
      可以获取节点在页面中的相对位置, tag_name 属性可以获取标签名称, size 属性可以获取
      节点的大小,也就是宽高,这些属性还是很有用的.
    from selenium import webdriver
    browser = webdriver.Chrome()
    url = 'https://www.zhihu.com/explore'
    browser.get(url)
    input = browser.find_element_by_class_name('zu-top-add-question')
    print(input.id)
    print(input.location)
    print(input.tag_name)
    print(input.size)
    # 这里首先获得 "提问" 按钮这个节点, 然后调用其 id, location, tag_name, size 属性来
    # 获取对应的属性值.
