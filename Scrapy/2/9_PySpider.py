#!/usr/bin/env python3

介绍
    pyspider 带有强大的 WebUI、脚本编辑器、任务监控器、项目管理器以及结果处理器，它支持
    多种数据库后端、多种消息队列、JavaScript 渲染页面的爬取，使用起来非常方便

基本功能
    1:提供方便易用的 WebUI 系统，可以可视化编写和调试爬虫
    2:提供爬去进度监控，爬取结果查看，爬虫项目管理等功能
    3:支持多种后端数据库，如 MySQL、MongoDB、Redis、SQLite、Elasticsearch、PostgreSQL
    4:支持多种消息队列：RabbitMQ、Beanstalk、Redis、Kombu
    5:提供优先级控制、失败重试、定时抓取等功能
    6:对接了 PhantomJS，可以抓取 JavaScript 渲染的页面
    7:支持单机和分布式部署，支持 Docker 部署

PySpider 架构
    1:PySpider 的架构主要分为 Scheduler（调度器）、Fetcher（抓取器）、Process（处理器）
      三个部分，整个爬取过程受到 Monitor（监控器）的监控，抓取的结果被 Result Worker
      （结果处理器）处理。
    2:Scheduler 发起任务调度，Fetch 负责抓取网页内容，Processer 负责解析网页内容。然后
      将新的 Request 发送给 Scheduler 进行调度，将生成的提取结果输出保存

PySpider 任务执行流程
    1:每个 PySpider 的项目对应一个 Python 脚本，该脚本中定义了一个 Handler 类，他有一个
      on_start() 方法，爬取首先调用 on_start() 方法生成最初的抓取任务，然后发送给
      Scheduler 进行调度
    2:Scheduler 将抓取任务分发给 Fetcher 进行抓取，Fetcher 执行并得到响应，随后将响应
      发送给 Processer
    3:Processer 处理响应并提取出新的 URL 生成新的抓取任务，然后通过消息队列通知 Scheduler
      当前抓取任务执行情况，并将新生成的抓取任务发送给 Scheduler。如果生成了新的提取结果
      则将其发送到结果队列等待 Result Worker 处理
    4:Scheduler 接收到新的抓取任务，然后查询数据库，判断其如果是新的抓取任务或者是需要
      重试的任务就继续进行调度，然后将其发送会 Fetcher 进行抓取
    5:不断重复以上工作，直到所有任务都执行完毕，抓取结束
    6:抓取结束后后，程序会调用 on_finished() 方法，这里可以定义后续处理
