选项卡管理
    1:在访问网页时，回开启一个个选项卡，在 Selenium 中，我们可以对这个选项卡进行操作。
    import time
    from selenium import webdriver
    browser = webdriver.Chrome()
    browser.get('https://www.baidu.com')
    browser.execute_script('window.open()')
    print(browser.window_handles)
    browser.switch_to_window(browser.window_handles[1])
    browser.get('https://www.taobao.com')
    time.sleep(1)
    browser.switch_to_window(browser.window_handles[0])
    browser.get('https://python.org')
    # execute_script('window.open())，这个javascript语句开启一个选项卡
    # window_handles属性 获取当前开启的所有选项卡   
    # switch_to_window() 切换选项卡
