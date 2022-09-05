import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
from jdbookRedis.items import JdbookredisItem
class AmazonSpider(RedisCrawlSpider):
    name = 'amazon'
    allowed_domains = ['amazon.cn']
    # start_urls = ['https://www.amazon.cn/s?k=%E5%9B%BE%E4%B9%A6&rh=n%3A658390051&dc&ds=v1%3AU92vY%2FX%2FLHMfDPXGUHw3rUW8RUO2V45Ims6yo9r8XFI&__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&crid=J6BWQ52ET5LI&qid=1662272296&rnid=124355071&sprefix=%E5%9B%BE%E4%B9%A6%2Caps%2C72&ref=sr_nr_n_7']
    redis_key = "amazon"
    rules = [

        # 匹配大分类和小分类的url
        Rule(LinkExtractor(restrict_xpaths=('//*[@id="departments"]/ul/li[@class="a-spacing-micro s-navigation-indent-2"]',)),follow=True),

        # 详情页
        Rule(LinkExtractor(restrict_xpaths=('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[@data-component-type]//h2/a',)),callback="parse_book_detall"),

        # 翻页
        Rule(LinkExtractor(restrict_xpaths=('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[20]/div/div/span',)),follow=True)
    ]


    def parse_book_detall(self,response):
        item = JdbookredisItem()


        # 书名
        item['bookName'] = response.xpath('//*[@id="productTitle"]/text()').extract_first()

        # 封面图片
        item['coverImg'] = response.xpath('//*[@id="ebooksImgBlkFront"]/@src').extract_first()

        # 页面链接
        item['bookLink'] = response.url

        # 作者
        item['author'] = response.xpath('//*[@id="bylineInfo"]/span[1]/a/text()').extract_first()

        # 出版社
        item['publishingHouse'] = ""

        # 出版时间
        item['publishingTime'] = ""

        li_list = response.xpath('//*[@id="detailBullets_feature_div"]/ul/li')
        # response.xpath("//b[text()='出版社:']/../text())

        for li in li_list:
            key = li.xpath('./span/span[1]/text()').extract_first()
            value = li.xpath('./span/span[2]/text()').extract_first()
            if "出版社" in key:
                item['publishingHouse'] = value
            elif "出版日期" in key:
                item['publishingTime'] = value
            elif not item['publishingHouse'] and "品牌" in key:
                item['publishingHouse'] = value
        # 价格
        item['price'] = response.xpath('//*[@id="kindle-price"]/text()').extract_first()

        # 一级类别
        item['category'] = [ i.strip() for i in response.xpath('//*[@id="wayfinding-breadcrumbs_feature_div"]/ul//text()').extract() if '›' not in i and i.strip()]

        print(dict(item))

