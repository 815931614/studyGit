import scrapy


class Demo01Spider(scrapy.Spider):
    name = 'demo01'
    allowed_domains = ['httpbin.org']
    start_urls = ['https://httpbin.org/get']

    def parse(self, response):
          print(response.text)
