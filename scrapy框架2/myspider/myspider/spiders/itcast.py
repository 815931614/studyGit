
import scrapy

import logging
class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['https://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # print(response.text)
        # res = response.xpath('//ul/li[1]/div[3]/h3').extract()
        # print('输出：',res)


        
        li_list = response.xpath('//*[@id="mCSB_1_container"]/ul//li').get()
        print(li_list)
        # for li in li_list:
        #     item = {}
        #     item['name'] = li.xpath('//div[2]/h2/text()').extract()[0]
        #     print(item)


