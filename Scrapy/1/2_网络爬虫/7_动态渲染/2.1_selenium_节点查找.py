1:基本使用
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait
    browser = webdriver.Chrome()
    try:
        browser.get('https://www.baidu.com')
        input = browser.find_element_by_id('kw')
        input.send_keys('Python')
        input.send_keys(Keys.ENTER)
        wait = WebDriverWait(browser,10)
        wait.until(EC.parsence_of_element_located((By.ID, 'content_left')))
        print(browser.current_url)
        print(browser.page_source)
    finally:
        browser.close()



2:声明浏览器对象
    1:Selenium 支持非常多的浏览器, 如 Chrome, Firfox, Edge 等. 还有 Android, BlackBerry
      等手机浏览器. 另外也支持无界浏览器 PhantomJS
    from selenium import webdriver
    browser = webdriver.Chrome()
    browser = webdriver.Firefox()
    browser = webdriver.Edge()
    browser = webdriver.PantomJS()
    browser = webdriver.Safari()
    # 完成浏览器对象的初始化并将其赋值为 browser 对象,
    # 接下来需要做的就是调用 browser 对象,让其执行各个动作以模拟浏览器操作




3:访问页面
    1:get() 来请求页面
    from selenium import webdriver
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    print(browser.page_source)
    browser.close()
    # browser.page_source 打印出源代码



4:查找节点
    Selenium 可以驱动浏览器完成各种操作, 比如填充表单,模拟点击. 比如,我们想要完成向某个
    输入框输入文字的操作.需要知道输入框在哪里. 而 Selenium 提供了一系列查找节点的方法.
    我们可以用这些方法来获取想要的节点,以便下一步执行一些动作或者提取信息
    
    ===== 1:单个节点 =====
    1:想要从淘宝页面中提取搜索框这个节点,首先需要观察它的源代码
    2:find_element_by_name() 根据 name 获取
    3:find_element_by_id() 根据 id 获取
    4:还有根据 XPath, CSS 选择器等获取的方式
    5:所有获取单个节点的方法
        find_element_by_id
        find_element_by_name
        find_element_by_xpath
        find_element_by_link_text
        find_element_by_partial_link_text
        find_element_by_tag_name
        find_element_by_class_name
        find_element_by_css_selector
    from selenium import webdriver
    browser = webdriver.Chrome()
    input_first = browser.find_element-by_id('q')
    input_second = browser.find_element_by_css_selector('#q')
    input_third = browser.find_element_by_xpath('//*[@id="q"]')
    print(input_first, input_second, input_third)
    browser.close()

    1:另外, Selenium 还提供了通用方法, find_element(), 他需要传入两个参数: 查找方式By和值
      实际上,它就是 find_element_by_id() 这种方法的通用函数版本. 比如 find_element_by_id(id)
      就等价于 find_element(By.ID, id), 两者结果完全一致
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    input_first = browser.find_element(By.ID, 'q')
    print(input_first)
    browsser.close()

    ===== 2:多个节点 ====
    1:如果查找的目标在网页中有多个,就是用 find_elements() 方法
    2:获取多个节点的方法
        find_elements_by_id
        find_elements_by_name
        find_elements_by_xpath
        find_elements_by_link_text
        find_elements_by_partial_link_text
        find_elements_by_tag_name
        find_elements_by_class_name
        find_elements_by_css_selector
    from selenium import webdriver
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    lis = browser.find_elements_by_css_selector('.service-bd li')
    print(lis)
    browser.close()
