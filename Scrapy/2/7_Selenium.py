1:Selenium
    1:自动化测试工具，支持多种浏览器
    2:爬虫中主要用来解决 JavaScript 渲染的问题
    3:pip install selenium


基本使用
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
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
        print(browser.current_url)
        print(browser.get_cookies())
        print(browser.page_source)
    finally:
        browser.close()




声明浏览器对象
    from selenium import webdriver
    browser = webdriver.Chrome()
    browser = webdriver.Firefox()
    browser = webdriver.Edge()
    browser = webdriver.Phantom.JS()
    browser = webdriver.Safari()



访问页面
    from selenium import webdriver
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    print(browser.page_source)
    browser.close()




查找元素
    === 单个元素
    from selenium import webdriver
    browser.get('https://www.taobao.com')
    input_first = browser.find_element_by_id('q')
    input_second = browser.find_element_by_css_selector('#q')
    input_third = browser.find_element_by_xpath('//*[@id="q"]')
    print(input_first, input_second, input_third)
    browser.close()

    find_element_by_name
    find_element_by_xpath
    find_element_by_link_text
    find_element_by_partial_link_text
    find_element_by_tag_name
    find_element_by_class_name
    find_element_by_css_selector

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    input_first = browser.find_element(By.ID, 'q')
    input_second = browser.find_element(By.CLASS_NAME, "hr")
    print(input_first)
    browser.close()

    === 多个元素
    from selenium import webdriver
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    lis = browser.find_elements_by_css_selector('.service-bd li')
    print(lis)
    browser.close()

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')

    find_elements_by_name
    find_elements_by_xpath
    find_elements_by_link_text
    find_elements_by_partial_link_text
    find_elements_by_tag_name
    find_elements_by_class_name
    find_elements_by_css_selector




元素交互操作
    === 对获取的元素调用交互方法
    from selenium import webdriver
    import time
    browser = webdriver.Chrome()
    browser.get('https://www.taogao.com')
    input = browser.find_element_by_id('q')
    input.send_keys('iPhone')
    time.sleep(1)
    input.clear()
    input.send_keys('iPad')
    button = browser.find_element_by_class_name('btn-search')
    button.click()



交互动作
    === 将动作附加到动作链中串行执行
    from selenium import webdriver
    from selenium.webdriver import ActionChains
    browser = webdriver.Chrome()
    url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    browser.get(url)
    browser.switch_to.frame('iframeResult')
    source = browser.find_element_by_css_selector('#draggable')
    target = browser.find_element_by_css_selector('#droppable')
    actions = ActionChains(browser)
    actions.drag_and_drop(source, target)
    actions.perform()



执行 JavaScript
    from selenium import webdriver
    browser = webdriver.Chrome()
    browser.get('https://www.zhihu.com/explore')
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    browser.execute_script('alert("To Bottom")')



获取元素信息
    === 获取属性
    from selenium import webdriver
    from selenium.webdriver import ActionChains
    browser = webdriver.Chrome()
    url = "https://www.zhihu.com/explore"
    browser.get(url)
    logo = browser.find_element_by_id('zh-top-link-logo')
    print(logo)
    print(logo.get_attribute('class'))

    === 获取文本值
    from selenium import webdriver
    browser = webdriver.Chrome()
    url = "https://www.zhihu.com/explore"
    browser.get(url)
    input = browser.find_element_by_class_name('zu-top-add-question')l

    === 获取 ID、位置、标签名、大小
    browser.get("https://www.zhihu.com/explore")
    input = browser.find_element_by_class_name('zu-top-add-question')
    print(input.id)
    print(input.location)
    print(input.tag_name)
    print(input.size)

    === Frame
    import time
    from selenium import webdriver
    from selenium.ccommon.exceptions import NoSuchElementException
    browser = webdriver.Chrome()
    url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
    browser.get(url)
    browser.switch_to_frame('iframeResult')
    source = browser.find_elemnt_by_class_name('logo')
    print(source)
    try:
        logo = browser.find_element_by_class_name('logo')
    except NoSuchElementException:
        print("NO LOGO")
    browser.switch_to.parent_frame()
    logo = browser.find_element_by_class_name('logo')
    print(logo)
    print(logo.text)




等待
    === 隐式等待
    当使用隐式等待执行测试的时候，如果 WebDriver 没有在 DOM 中找到元素，将继续等待，
    超出设定时间后则抛出找不到元素的异常，换句话说，当查找元素或元素并没有立即出现
    的时候，隐式等待一段时间再查找 DOM，默认的时间是0

    from selenium import webdriver
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get('https://www.zhihu.com/explore')
    input = browser.find_element_by_class_name('zu-top-add-question')
    print(input)

    === 显式等待
    from selenium import webdriver
    from selenium import webdriver.common.by import By
    from selenium import webdriver.support.ui import WebDriverWait
    from selenium import webdriver.support import expected_conditions as EC
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    wait = WebDriverWait(browser, 10)
    input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
    print(input, button)

    title_is                                标题是某内容
    title_contains                          标题包含某内容
    presence_of_element_located             元素加载出,传入定位元组, 如(By.ID, 'p')
    visibility_of_element_located           元素可见, 传入定位元组
    visibility_of                           可见,传入元素对象
    presence_of_all_elements_located        所有元素加载出
    text_to_be_present_in_element           某个元素文本包含文字
    text_to_be_present_in_element_value     某个元素值包含某文字
    frame_to_be_available_and_swith_to_it   frame 加载并切换
    invisibility_of_element_located         元素不可见
    element_to_be_clickable                 元素可点击
    staleness_of                            判断一个元素是否仍在 DOM, 可判断页面是否已经刷新
    element_to_be_selected                  元素可选择, 传元素对象
    element_located_to_be_selected          元素可选择, 传入定位元组
    element_selection_state_to_be           传入元素对象以及状态,想等返回 True, 否则返回 False
    element_located_selection_state_to_be   传入定位元组以及状态,相等返回 True,否则返回 False
    alert_is_present                        是否出现 Alert



前进后退
    browser.get('https://www.baidu.com')
    browser.get('https://www.taobao.com')
    browser.get('https://www.python.org')
    browser.back()
    time.sleep(1)
    browser.forward()
    browser.close()



Cookie
    browser.get('https://www.zhihu.com/explore')
    print(browser.get_cookies())
    browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
    print(browser.get_cookies())
    browser.delete_all_cookies()
    print(browser.get_cookies())



选项卡管理
    import time
    from selenium import webdriver
    browser = webdriver.Chrome()
    browser.get("https://www.baidu.com")
    browser.execute_script("window.open()")
    print(browser.window_handles)
    browser.switch_to_window(browser.window_handles[1])
    browser.get('https://www.taobao.com')
    time.sleep(1)
    browser.switch_to_window(browser.window_handles[0])
    browser.get('https://python.org')



异常处理
    from selenium import webdriver
    browser = webdriver.Chrome()
    browser.get('https://www.baidu.com')
    browser.find_element_by_id('hello')

    from selenium import webdriver
    from selenium.common.exceptions import TimeoutException, NoSuchElementException
    browser = webdriver.chrome
    try:
        browser.get("https://www.baidu.com")
    except TimeoutException:
        print("Time Out")
    try:
        browser.find_element_byid("hello")
    except NoSuchElementException:
        print("No Element")
    finally:
        browser.close()
