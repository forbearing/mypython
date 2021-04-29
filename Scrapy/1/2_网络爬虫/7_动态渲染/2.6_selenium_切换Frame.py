1:网页中有一种节点叫做 iframe, 也就是子 Frame, 相当于页面的子页面, 他的结构和外部网页的
  结构完全一致.
2:Selenium 打开网页后, 它默认是在父级 Frame 里面操作,而此时如果页面中还有子 Frame, 它是
  不能后去到子 Frame 里面的节点的.
3:这里需要使用 switch_to.frame() 方法来切换 Frame

import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
try:
    logo = browser.find_element_b_class_name('logo')
except NoSuchElementException:
    print('NO LOGO')
browser.switch_to.parent_frame()
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)
