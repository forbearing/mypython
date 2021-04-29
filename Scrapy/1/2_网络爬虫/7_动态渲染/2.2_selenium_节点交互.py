1:Selenium 可以驱动浏览器来执行一些操作,让浏览器模拟执行一些动作,比较常见的用法有:
  输入文字时用 send_keys() 方法. 清空文字时用 clear() 方法, 点击按钮时用 click() 方法.



from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')
input.send_keys('iphone')
time.sleep(1)
input.clear()                       # 清空输入框
input.send_keys(ipad)
button = browser.find_element_by_class_name('btn-search')
button.click()
