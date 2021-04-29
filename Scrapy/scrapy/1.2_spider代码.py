#!/usr/bin/env python3

--- yield 返回给 pipeline
import scrapy
class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['https://www.itcast.cn/channel/teacher.shtml']

    # def parse(self, reponse):
        # res = response.xpath("//div[@class='tea_con']//h3/text()")
        # ret1 = res.extract()
        # print(ret1)
        # print(type(res))
        # print(type(ret1))

    def parse(self, reponse):
        li_list = reponse.xpath("//div[@class='tea_con']//li")
        for li in li_list:
            item = {}
            item['name'] = li.xpath(".//h3/text()").extract_first()
            item['title'] = li.xpath(".//h4/text()").extract()[0]
            yield item



--- logging 模块的使用
import scrapy
class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['https://www.itcast.cn/channel/teacher.shtml']

    def parse(self, reponse):
        for i in range(10):
            item = {}
            item['com_from']
            logging.warning(item)
            yield item
