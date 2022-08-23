import scrapy
from ..items import YinfansiItem

class Yinfansi2Spider(scrapy.Spider):
    name = 'yinfansi3'
    allowed_domains = ['yinfans.me']


    def start_requests(self):
        for page in range(2,15):
            url = 'https://www.yinfans.me/page/{}'.format(page)

            # 交给调度器
            yield scrapy.Request(
                url = url,
                callback= self.parse_html
            )

    def parse(self, response):
        pass


    def parse_html(self,response):
        li_list = response.xpath('//*[@id="post_container"]/li')

        for li in li_list:
            # 创建导入items对象
            item = YinfansiItem()

            # 名称
            item['name'] = li.xpath('.//div[2]/h2/a/@title').extract_first().strip()

            # 清晰度
            item['nobluray'] = li.xpath('.//div[3]/span[2]/a/text()').extract_first().strip()

            # 时间
            item['time'] = li.xpath('.//div[3]/span[1]/text()').extract_first().strip()

            # 把爬取的数据交给管道文件pipeline处理
            yield item


