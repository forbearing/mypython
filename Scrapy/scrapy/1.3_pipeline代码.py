#!/usr/bin/env python3


--- pipelines 处理代码
1:item 是 spider 中 yield 返回的
2:spider 是 spider 自身
3:process_item 方法名固定的，否则无法进行 pipelines 处理
4:每一个 pipeline 类中的 process_item 必须有一个 return

class FirstSpiderPipeline(object):
    def process_item(self, item, spider):
        item["hello"] = "world"
        return item

class FirstSpiderPipeline1(object):
    def process_item(self, item, spider):
        print(item)
        return item



--- 设置 log
import logging
logger = logging.getLogger(__name__)            # 用来显示 log 位置

class MyspiderPipeline(object):
    def process_item(self, item, spider):
        if spider.name == "itcast":
            logger.warning("-"*10)
        return item

