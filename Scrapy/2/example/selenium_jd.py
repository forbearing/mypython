#!/usr/bin/env python3
'''
1:搜索关键字
    利用 Selenium 驱动浏览器搜索关键字,得到查询后的商品列表
2:分析页码并翻页
    得到商品页码数,模拟翻页,得到后续页面的商品列表
3:分析提取商品内容
    利用 PyQuery 分析源代码,解析得到商品列表
4:存储至 MongoDB
    将商品列表信息存储到数据看 MongoDB
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_condition as EC

browser = webdriver.Chrome()

def search():
    browser.get('https://www.vip.com')
    input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(By.CLASS_NAME, "c-search-input")
    )
    submit = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'c-search-button')))
