#!/bin/env python3

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# browser = webdriver.Chrome()
# try:
    # browser.get('https://www.baidu.com')
    # input = browser.find_element_by_id('kw')
    # input.send_keys('Python')
    # input.send_keys(Keys.ENTER)
    # wait = WebDriverWait(browser, 10)
    # wait.until_not(EC.presence_of_element_located((By.ID),'content_left'))
    # print(browser.current_url)
    # print(browser.get_cookies())
    # print(browser.page_source)
# finally:
    # browser.close()

from selenium import webdriver
from selenium.webdriver.common.by import By

# #browser = webdriver.Firefox()
# browser = webdriver.Chrome()

# #browser.get('https://www.jd.com')
# browser.get('https://www.taobao.com')

# #lis = browser.find_elements_by_css_selector('.service-bd li')
# lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')

# print(lis)
# browser.close()


# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input = browser.find_element_by_id('q')
# input = send_keys('iPhone')
# time.sleep(1)
# input.clear()
# input.send_keys('ipad')
# button = browser.find_element_by_class_name('btn-search')
# button.click()

from selenium
