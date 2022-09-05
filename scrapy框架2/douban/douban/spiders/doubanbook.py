'''
Author: 815931614 815931614@qq.com
Date: 2022-08-31 21:22:13
LastEditors: 815931614 815931614@qq.com
LastEditTime: 2022-09-01 01:51:04
FilePath: \MyNote\scrapy框架2\douban\douban\spiders\doubanbook.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import scrapy
from douban.items import DoubanItem
from copy import deepcopy
class DoubanbookSpider(scrapy.Spider):
    name = 'doubanbook'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/?view=type&icn=index-sorttags-all']
    def start_requests(self):
        cookies = {'ll': '"118254"', 'bid': 'IHGkoqBDJKM', '__utmc': '81379588', '__utmz': '81379588.1661951554.1.1.utmcsr', '_ga': 'GA1.1.1538874449.1661951058', '__gads': 'ID', '__gpi': 'UID', 'gr_user_id': '782b93b5-b964-482b-a938-8f1c27e1c013', '_vwo_uuid_v2': 'DA38A8464D7EBD54ED996DF06110FD7E2|49f9176ca438d603eaf6515550d283b8', '__yadk_uid': 'JCve9d0WCFue9LK9rsi8CYEIldRKP7UA', '_ga_RXNMP372GL': 'GS1.1.1661951061.1.1.1661952048.22.0.0', '_pk_ref.100001.3ac3': '%5B%22%22%2C%22%22%2C1661958961%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D', '_pk_ses.100001.3ac3': '*', '__utma': '81379588.1538874449.1661951058.1661951554.1661958961.2', 
            'viewed': '"4913064_35517022_30396222_35886207_35587028_35658993"', 'dbcl2': '"168282384:Lm19wc1r9/E"', 'ck': 'TZzU', 'gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03': '9e7d993a-fb91-41c6-9efd-99d6d2c6d672', 'gr_cs1_9e7d993a-fb91-41c6-9efd-99d6d2c6d672': 'user_id%3A1', 'gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_9e7d993a-fb91-41c6-9efd-99d6d2c6d672': 'true', 'push_noty_num': '0', 'push_doumail_num': '0', '__utmt_douban': '1', '__utmt': '1', '_pk_id.100001.3ac3': 'f54566227e6602f5.1661951554.2.1661966369.1661953599.', '__utmb': '81379588.34.10.1661958961'}

        yield scrapy.Request(
        'https://book.douban.com/tag/?view=type&icn=index-sorttags-all', 
        meta={'cookies' : cookies },
        cookies =  cookies,        
        callback=self.parse
        )
    def parse(self, response):
        print(1)
        div_list = response.xpath('//*[@id="content"]/div/div[1]/div[2]//div')
        for div in div_list:
            firstLabel = div.xpath('.//a/@name').extract_first() # 一级标签
           
            table_td = div.xpath(".//td") 
            for td in table_td:
                item = DoubanItem()
                item['firstLabel'] = firstLabel
                item['secondLabel'] = td.xpath('./a/text()').extract_first()
                url = 'https://book.douban.com/' + td.xpath('./a/@href').extract_first() # 链接
                yield scrapy.Request(
                    url,
                    meta = {"item" : deepcopy(item),'cookies' : response.meta['cookies']},
                    cookies = response.meta['cookies'],
                    callback = self.parse_tag
                )
                
                
           
            break                    

    def parse_tag(self,response):
      
        item = response.meta['item']
        li_list = response.xpath('//*[@id="subject_list"]//ul/li')
        for li in li_list:
            text_sp = li.xpath('./div[2]/div[1]/text()').get().split("/")
            if len(text_sp) == 4:
                text_sp.insert(1,'')
            # '[日] 奈良美智 / 陈文娟 / 新星出版社 / 2022-7 / 68.00元'
            # HIGHTONE / 香港高色調出版有限公司 / 2022-6 / 286

            item['bookName'] = li.xpath('./div[2]/h2/a/text()').extract_first().strip() # 读物名称
            item['author'] = text_sp[0].strip() # 作者
            item['translator'] =  text_sp[1].strip()
            item['publishingHouse'] = text_sp[2].strip() # 出版公司
            item['publicationTime'] = text_sp[3].strip()  # 发行时间
            item['readingCcores'] = li.xpath('./div[2]/div[1]/span[2]/text()').extract_first()  # 读物评分
            if not item['readingCcores']:
                item['readingCcores'] = li.xpath('./div[2]/div[2]/span[2]/text()').extract_first()  # 读物评分
            if not item['readingCcores']:
                print(item['bookName'])
            item['synopsis'] = li.xpath('./div[2]/p/text()').extract_first().strip() # 简介
            item['cover_img'] = li.xpath('./div[1]/a/img/@src').extract_first().strip() # 封面图片
            item['bookPrice'] = text_sp[4].strip() # 纸质版价格 
            url = li.xpath('./div[2]/h2/a/@href').extract_first().strip()
            yield scrapy.Request(
                url,
                meta = {"item" : deepcopy(item),'cookies' : response.meta['cookies']},
                cookies = response.meta['cookies'],
                callback = self.parse_detail
            )

    def parse_detail(self, response):
        item = response.meta['item']

        item['isbn'] = "" # ISBN编号
        item['numberPages'] = "" # 页数   
        text_list = response.xpath('//*[@id="info"]//text()').extract()
        for text in range(len(text_list)):
            if text_list[text].strip() == "页数:":
                item['numberPages'] = text_list[text+1]
            elif text_list[text].strip() == "ISBN:":
                item['isbn'] = text_list[text+1]
        print(item)
        yield item