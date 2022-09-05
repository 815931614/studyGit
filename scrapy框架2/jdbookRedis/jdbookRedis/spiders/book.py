import scrapy
from scrapy_redis.spiders import RedisSpider,RedisCrawlSpider

class BookSpider(RedisCrawlSpider):
    name = 'book'
    allowed_domains = ['jd.com']
    start_urls = ['https://book.jd.com/']

    def parse(self, response):
        dt_list = response.xpath('//*[@id="booksort"]/div[2]/dl//dt')
        for dt in dt_list:
            item = {}


