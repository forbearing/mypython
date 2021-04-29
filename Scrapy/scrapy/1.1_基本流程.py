#!/usr/bin/env python3

1:组件介绍
    Scrapy Engine（Scrapy 已实现）
        总指挥，负责数据和信号的在不同模块间的传递
    Scheduler（Scrapy 已实现）
        一个队列，存放引擎发过来的 request 请求
    Downloader（Scrapy 已实现）
        下载把引擎发过来的 requests 请求，并返回给引擎
    Spider（需要手写）
        处理引擎发送过来的的 reponse，提取数据，提取 url，并交给引擎
    Item Pipeline（需要手写）
        处理引擎发送过来的数据，比如存储
    Downloader Middlewares（一般不用手写）
        可以自定义的下载扩展，比如设置代理
    Spider Middlewares（一般不用手写）
        可以自定义 requests 请求和进行 repnonse 过滤


2:入门使用
    1:生成一个项目
        scrapy startproject mySpider
    2:生成一个爬虫
        scrapy genspider hybfkuf "hybfkuf.com"
    3:开启爬虫
        scrapy crawl itcast
    3:提取数据
        完善 spier，使用 xpath 等方法
    4:保存数据
        pipeline 中保存数据



完善 Spider
    class ItcastSpider(scrapy.Spider):      # 自定义 Spider 类，继承自 scrapy.spider
        name = 'itcast'                     # 爬虫名字，爬取时用 scrapy crawl itcast
        allowed_domains = ['itcast.cn']     # 允许爬取的范围，防止爬虫爬到了其他的网站
        start_urls = ['https://www.itcast.cn/channel/teacher.shtml']    # 开始爬取的地址
        def parse(self, response):          # 数据提取方法，接受来自下载中间件传过来的 response
            names = reponse.xpath("//div[@class='tea_con']//li/div/h3/text()")
            print(names)

    从选择器中提取字符串
        1:extract() 返回一个包含字符串数据的列表
        2:extract_first() 返回列表中的第一个字符串

    注意：
        1:spider 中的 parse 方法名不能修改
        2:pipelines.py 中的 process_item 方法名不能修改
        3:需要爬取的 url 地址要属于 allow_domain 下的链接
        4:reponse.xpath() 返回的是一个含有 selector 对象的列表

使用 pipeline
    import json
    class MyspiderPipeline(object):
        def process_item(self, item, spider):           # 实现存储方法
            with open('temp.txt', 'a') as f:
                json.dump(item, f, ensure_ascii=False, indent=2)
    完成 pipeline 代码后，需要在 settings 中设置开启
        ITEM_PIPELINES = {
            'myspider.pipelines,MyspiderPipeline': 300,     # pipeline的位置: 权重
        }

    从 pipeline 的字典形式可以看出，pipeline 可以有多个，而且确实 pipeline 能够定义多个
    为什么需要多个 pipeline
        1:可能会有多个 Spider，不同的 pipeline 处理不同的 item 的内容
        2:一个 spider 的内容可能要做不同的操作，比如存入不同的数据库中
    注意
        1:pipeline 的权重越小优先级越高
        2:pipeline 中process_item 方法名不能修改为其他的名称
