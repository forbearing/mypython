动作链
    1:一些交互式动作都是针对某些节点执行的. 对于输入框,我们就调用了它输入文字和清空文字方法
      对于按钮,就调用它的点击方法.
    2:还有另外一些操作, 它们没有特定的执行对象,比如鼠标拖拽,键盘按钮等.这些动作用另一种方式
      来执行,那就是动作链
    from selenium import webdriver
    from selenium.webdriver import ActionChains
    browser = webdriver.Chrome()
    url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    browser.get(url)
    browser.switch_to.frame('iframeResult')
    source = browser.find_element_by_css_selector('#draggable')
    target = browser.find_element_by_css_selector('#drappable')
    actions = ActionChains(browser)
    actions.drag_and_drop(source, target)
    actions.perform()
