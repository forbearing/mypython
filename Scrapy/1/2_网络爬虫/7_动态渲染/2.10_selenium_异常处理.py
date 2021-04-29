1:在使用 Selenium 的过程中，难免会遇到一些异常，例如超时，节点未找到等错误，一旦
  出现此类错误，程序便不会继续运行了。

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time Out')
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()
