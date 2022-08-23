import scrapy
import json
from ..items import SoItem
class SoSpider(scrapy.Spider):
    name = 'so'
    allowed_domains = ['image.so.com']





    def start_requests(self):
        link = 'https://image.so.com/zjl?sn={}&ch=art'

        for i in range(5):
            url = link.format(i * 30)
            yield scrapy.Request(
                url=url,
                callback=self.parse_img
            )


    def parse_img(self,response):

        resJson = json.loads(response.text)
        print(resJson)
        # 提取图片链接
        for img in resJson['list']:
            item = SoItem()
            item['img_link'] = img['imgurl']
            yield item