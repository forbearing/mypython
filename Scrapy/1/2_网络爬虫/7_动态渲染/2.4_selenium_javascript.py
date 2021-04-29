执行 JavaScript
    1:对于某些操作, Selenium API 并没有提供,比如,下拉进度条,它可以直接模拟运行 JavaScript,
      此时使用 execute_script() 方法即可实现.
    from selenium import webdriver
    browser = webdriver.Chrome()
    browser.get('https://www.zhihu.com/explore')
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    browser.execute_script('alert("To Bottom")')
    # execute_script() 方法将进度条下拉到最底部,然后弹出 alert 提示框
    # 所有有了这个方法,基本上 API 没有提供的所有功能都可以用执行 JavaScript 的方式来实现了.
