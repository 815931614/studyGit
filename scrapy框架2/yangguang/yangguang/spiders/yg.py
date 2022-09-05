'''
Author: 815931614 815931614@qq.com
Date: 2022-08-31 18:18:29
LastEditors: 815931614 815931614@qq.com
LastEditTime: 2022-08-31 19:14:43
FilePath: \MyNote\scrapy框架2\yangguang\yangguang\spiders\yg.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import scrapy
from yangguang.items import YangguangItem

class YgSpider(scrapy.Spider):
    name = 'yg'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['https://wz.sun0769.com/political/index/supervise?page=2']

    def parse(self, response):
        item = YangguangItem()
        li_list = response.xpath('/html/body/div[2]/div[3]/ul//li')
                                
        for li in li_list:
            item['id'] = li.xpath("./span[1.json]/text()").extract_first().strip()
            item['state'] = li.xpath("./span[2]/text()").extract_first().strip()
            item['title'] = li.xpath("./span[3]/a/text()").extract_first().strip()
            item['replyTime'] = li.xpath('./span[4]/text()').extract_first().strip()
            item['submitTime']= li.xpath('./span[5]/text()').extract_first().strip()
            item['href'] = "https://wz.sun0769.com" + li.xpath("./span[3]/a/@href").extract_first().strip()
            # print(dict(item))
            yield scrapy.Request(
                item["href"],
                meta = {'item':item},
                callback=self.parse_detail
            )    

            next_url = "https://wz.sun0769.com" + response.xpath("/html/body/div[2]/div[3]/div[3]/a[2]/@href")
            if next_url.split("=")[1] != "1.json":
                yield scrapy.Request(
                    next_url,
                    callback = self.parse
                )
                   
               
    
    
    def parse_detail(self,response):
        item = response.meta['item']
             
        
        item['submit_data'] = response.xpath("/html/body/div[3]/div[2]/div[2]/div[2]/pre/text()").extract_first()
    
        item['replyContent_data'] = response.xpath("/html/body/div[3]/div[2]/div[2]/div[5]/div/pre/text()").extract_first()

        item['replyContent_img'] =response.xpath("/html/body/div[3]/div[2]/div[2]/div[3]//img//@src").extract()

        print(item)
        yield item