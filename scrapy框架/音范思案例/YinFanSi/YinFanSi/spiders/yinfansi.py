import scrapy
from ..items import YinfansiItem

class YinfansiSpider(scrapy.Spider):
    name = 'yinfansi'
    allowed_domains = ['yinfans.me']
    start_urls = ['https://www.yinfans.me/page/1']
    page = 0

    def parse(self, response):
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

        # 拼接新的URL地址交给调度器入队列
        self.page += 1
        if self.page <= 90:
            url = 'https://www.yinfans.me/page/{}'.format(self.page)

            # 交给调度器入队列
            yield scrapy.Request(
                url=url,
                callback= self.parse
            )