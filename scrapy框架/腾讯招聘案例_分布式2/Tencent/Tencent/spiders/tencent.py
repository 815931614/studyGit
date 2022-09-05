import scrapy
import json
from ..items import TencentItem
import pytesseract
# 使用redis_key改写,导入scrapy_redis的RedisSpider
from scrapy_redis.spiders import RedisSpider


class TencentSpider(RedisSpider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    one_link = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1659939630829&countryId=&cityId=&bgIds=&productId=&categoryId=40001001,40001002,40001003,40001004,40001005,40001006&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
    two_link = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1659939982659&postId={}&language=zh-cn'

    # 1.json. 出掉start_urls
    # 项目启动时,阻塞，等待redis发送的指令(URL)
    redis_key = 'tencent:spider'


    def parse(self, response):
        for page_index in range(1,51):
            url = self.one_link.format(page_index)
            yield scrapy.Request(
                url = url,
                callback= self.parse_one
            )



    def parse_one(self,response):
            html = json.loads(response.text)
            for post in html['Data']['Posts']:
                item = TencentItem()

                item['zh_name'] = post['RecruitPostName']
                item['zh_type'] = post['CategoryName']
                item['zh_duty'] = post['Responsibility']
                post_id = post['PostId']


                yield scrapy.Request(
                    url = self.two_link.format(post_id),
                    meta={'item': item},
                    callback=self.parse_two
                )

    def parse_two(self,response):

        item = response.meta['item']
        html = json.loads(response.text)
        item['zh_require'] = html['Data']['Requirement']

        yield item