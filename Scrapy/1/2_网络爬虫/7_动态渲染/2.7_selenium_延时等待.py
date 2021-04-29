延时等待
    1:在 Selenium 中, get() 方法会在网页框架家在结束后结束执行,此时如果获取 page_source,
      可能并不是浏览器完全加载完成的页面. 如果某些页面有额外的 Ajax 请求.我们在网页中
      也不一定能成功获取到, 需要延迟等待一定时间,确保节点都加载出来.
    2:等待方式由隐式等待,显式等待




1:隐式等待
    1:当使用隐式等待执行测试的时候,如果 Selenium 没有在 DOM 中找到节点,将继续等待,超出
      设定时间后,则抛出找不到节点的异常
    2:当查找节点而节点没有立即出现的时候,隐式等待将等待一段是时间再查找 DOM, 默认的时间时0
    from selenium import webdriver
    browser = webdriver.Chrome()
    browser = implicitly_wait(10)
    browser.get('https://www.zhihu.com/explore')
    input = browser.find_element_by_class_name('zu-top-add-question')
    print(input)
    # 使用 implicitly_wait() 实现了隐式等待




2:显式等待
    1:隐式等待的效果其实并没有那么好,因为只规定了一个固定时间,而页面的加载时间会受到
      网络条件的影响.
    2:显式等待,指定要查找的节点,然后制定一个最长等待时间,如果在规定时间内加载出来了
      这个节点,就返回查找的节点.如果到了规定时间依然没有加载出该节点,则抛出超时异常
    3:等待条件有很多, 比如判断标题内容, 判断某个节点内是否出现了某文字等
      title_is                              标题是某内容
      title_contains                        标题包含某内容
      presence_of_element_located           节点加载出来,传入定位元组
      visibility_of_element_located         节点可见,传入定位元组
      visibility_of                         可见,传入节点对象
      presence_of_all_elements_located      所有节点加载出来
      text_to_be_present_in_element         某个节点文本包含某文字
      text_to_be_present_in_element_value   某个节点值包含某文字
      frame_to_be_available_and_switch_to_it    加载并切换
      invisibility_of_element_located       节点不可见
      element_to_be_clickable               节点可点击
      staleness_of                          判断一个节点是否扔在 DOM, 可判断页面是否已经刷新
      element_to_be_selected                节点可选择,传节点对象
      element_located_to_be_selected        节点可选择,传入定位元组
      element_selection_state_to_be         传入节点对象以及状态,相等返回 True,否则返回 False
      element_located_selection_state_to_be 传入定位元组以及状态,相等返回 True,否则返回 False
      alert_is_present                      是否出现警告
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    wait = WebDriverWait(browser, 10)
    input = wait.until(EC.presence_of_element_located(By.ID, 'q'))
    button = wait.until(EC.element_to_be_clicable((By.CSS_SELECTOR, '.btn-search')))
