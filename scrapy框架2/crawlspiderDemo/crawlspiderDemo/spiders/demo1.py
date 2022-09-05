import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Demo1Spider(CrawlSpider):
    name = 'demo1'
    allowed_domains = ['yinfans.me']
    start_urls = ['https://www.yinfans.me/page/1.json']

    # 定义提取url地址规则，每个Rule代表一条规则
    rules = (
        # LinkExtractor 链接提取器，提取url地址
        # allow=r'Items/' 正则
        # callback 提取出来的url地址的response会交给callback处理
        # follow  表示当前url地址的响应是否重新经过rules来提取url
        Rule(LinkExtractor(allow=r'https://www.yinfans.me/movie/\d+'), callback='parse_item'),
        Rule(LinkExtractor(allow=r'https://www.yinfans.me/page/\d+'),follow=True),
    )

    # parse函数有特殊功能，不能定义
    def parse_item(self, response):
        item = {}
        item['title'] = response.xpath('//*[@id="content"]/div[1.json]/h1/text()').get()
        item['publish_date'] = response.xpath('//*[@id="content"]/div[1.json]/div[1.json]/span[3]/text()').extract_first()
      
        print(item)
        # yield scrapy.Reuqest(
        #     url,
        #     callback=self.fun,
        #     meta = {"item": item}
        # )