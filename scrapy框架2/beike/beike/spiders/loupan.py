'''
Author: 815931614 815931614@qq.com
Date: 2022-08-31 16:21:41
LastEditors: 815931614 815931614@qq.com
LastEditTime: 2022-08-31 17:48:31
FilePath: \MyNote\scrapy框架2\beike\beike\spiders\loupan.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import scrapy
from beike.items import BeikeItem

class LoupanSpider(scrapy.Spider):
    name = 'loupan'
    allowed_domains = ['wh.fang.ke.com']
    start_urls = ['https://wh.fang.ke.com/loupan/']

    def parse(self, response):
        # print(response.text)
        li_list = response.xpath('//html/body/div[6]/ul[2]//li')
        # print(li_list)
        for li in li_list:
            item = BeikeItem()
            item['loupanNmae'] = li.xpath('./div/div[1]/a/text()').extract_first()
            item['resblock'] = li.xpath('./div/div[1]/span[1]/text()').extract_first()
            item['address'] = li.xpath('./div/a[1]/@title').extract_first()
            yield item
          
