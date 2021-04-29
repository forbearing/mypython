#!/usr/bin/env python3
框架介绍
    Scrapy 是一个基于 Twisted 的异步处理框架，是纯 Python 实现的爬虫框架，其架构清晰，
    模块耦合度低，可扩展性极强，可以灵活完成各种需求我们只需要开发几个模块就可以
    轻松实现一个爬虫。

Scrapy 架构
    Engine: 引擎,用来处理整个系统的数据流处理,触发事务,是整个框架的核心
    Item: 项目,它定义了爬取结果的数据结构,爬取的数据会被赋值成该对象
    Scheduler: 调度器,用来接收引擎放过来的请求并加入队列中,并在引擎再次请求的时候
        提供给引擎.
    Downloader: 下载器,用于下载网页内容,并将网页内容返回给蜘蛛
    Spider: 蜘蛛,其定义了爬取的逻辑和网页的解析规则,它主要负责解析响应并生成
        提取结果和新的请求
    Item Pipeline: 项目管道,负责处理蜘蛛从网页中抽取的项目,它主要的任务是
        清洗,验证和存储数据
    Downloader Middlewarse: 下载器中间件,位于引擎和下载器之间的钩子框架,主要处理引擎
        与下载器之间的请求及响应
    Spider Middlewarse: 蜘蛛中间件,位于引擎蜘蛛之间的钩子框架,主要工作是处理蜘蛛输入的
        响应和输出的结果及新的请求

数据流
    Scrapy 中的数据流由引擎控制
    1:Engine 首先打开一个网站,找到处理该网站的 Spider 并向该 Spider 请求第一个要爬取的url
    2:Engine 从 Spider 中获取到第一个要爬取的 URL 并通过 Scheduler 以 Request 的形式调度
    3:Engine 向 Scheduler 请求下一个要爬取的 URL
    4:Scheduler 返回下一个要爬去的 URL 给 Engine, Engine 将 URL 通过 Downloader Middlewarse
      转发给 Downloader 下载
    5:一旦页面下载完毕, Downloader 生成一个该页面的 Response, 并将通过 Downloader Middlewarse
      发送给 Engine
    6:Engine 从下载器中接收到 Response 并通过 Spider Middlewarse 发送给 Spider 处理
    7:Spider 处理 Response 并返回 item 给 Item pipeline, 将新的 Request 给 Scheduler
    8:重复第二步到最后一步,直到 Scheduler 中没有更多的 Request, engine 关闭该网站,爬取结束

项目结构
    scrapy.cfg
    project/
        __init__.py
        items.py
        pipelines.py
        settings.py
        middlewares.py
        spiders/
            __init__.py
            spider1.py
            spider2.py
    scrapy.cfg          Scrapy 项目的配置文件,其定义了项目的配置文件路径,部署相关信息等内容
    items.py            它定义 item 数据结构, 所有的 item 的定义都可以在这里
    pipelines.py        它定义了 Item pipeline 的实现, 所有 item pipeline 的实现都可以放这里
    settings.py         它定义了项目的全局配置
    middlewares.py      它定义了 Spider Middlewarse 喝 Downloader Middlewarse 的实现
    Spiders             其内包含了一个个 Spider 的实现,每个 Spider 都有一个文件


1:依赖包
    wheel, PyOpenssl, Twisted, Pywin32


2:流程
    1:抓取第一页
        请求第一页的URL并得到源代码
    2:获取内容和下一页链接
        分析源代码，提取首页内容，获取下一页链接等待进一步提取
    3:翻页爬取
        读取下一页信息，分析内容并请求再下一页链接
    4:保存爬取结果
        将爬取结果保存为特定格式如文本、数据库

3:
    scrapy startproject quotesproject
    cd first
    scrapy genspider quotes quotes.toscrape.com
    scrapy crawl quotes
