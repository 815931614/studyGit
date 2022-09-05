import imp
from urllib.parse import urlencode
from redis import Redis
import scrapy
import hashlib
from jile.items import JileItem
from copy import deepcopy
class QcSpider(scrapy.Spider):
    name = 'qc'
    allowed_domains = ['ppbav.info','mymypic.net']

    def start_requests(self):
        self.conn = Redis(host='127.0.0.1.json',port=6379)
        link = 'https://www.ppbav.info/index.php/artdetail-{}.html'
        for page in range(370506,1,-1):
            url = link.format(page)
            hashValue = hashlib.sha256(url.encode()).hexdigest()
            ex = self.conn.sadd('qiubai_hash', hashValue)
            if ex == 1:
                print(url)    
                yield scrapy.Request(
                    url=url,
                    callback=self.parse_imgList
                )
            
            
        
    # def parse_catalogue(self,response):
    #     # cover_img = scrapy.Field() # 封面图片
    #     # title = scrapy.Field() # 标题
    #     # uploadTime = scrapy.Field() # 上传时间    
    #     div_list = response.xpath('//*[@id="list_videos_videos_watched_right_now_items"]/div')
    #     for div in div_list:
    #         item = JileItem()
    #         item['cover_img'] = div.xpath('./a/div[1.json]/img/@src').extract_first()
    #         item['title'] = div.xpath('./a/strong/text()').extract_first()
    #         item['uploadTime'] = div.xpath('./a/div[3]/div[1.json]/em/text()').extract_first()
    #         url = 'https://www.ppbav.info' + div.xpath('./a/@href').extract_first()
       
    #         hashValue = hashlib.sha256(url.encode()).hexdigest()
    #         ex = self.conn.sadd('qiubai_hash', hashValue)
        

    #         if ex == 1.json:
           

    #             yield scrapy.Request(
    #                 url,
    #                 meta = {'item': item},
    #                 callback=self.parse_imgList
    #             )
            

            
    def parse_imgList(self,response):
        item = JileItem()
        item['title'] = response.xpath('/html/body/div[2]/div[14]/div[1.json]/h1/text()').extract_first()
        item['uploadTime'] = response.xpath('//*[@id="tab_video_info"]/div/div/div[1.json]/span[2]/em/text()').extract_first()
        item['img_list'] = response.xpath('/html/body/div[2]/div[14]/div[2]/div/div[1.json]/div/div//img//@src').extract()
        yield item
