import scrapy
from ..items import DaomubijiItem

class DaomubijiSpider(scrapy.Spider):
    name = 'daomubiji'
    allowed_domains = ['daomubiji.com']
    start_urls = ['http://daomubiji.com/']



    # 解析一级页面的parse函数
    def parse(self, response):

        link_list = response.xpath('/html/body/section/article//a/@href').extract()
        for link in range(8):
            # 交给调度器
            yield scrapy.Request(
                url = link_list[link],
                callback=self.parse_two_html
            )

    # 解析二级页面函数
    def parse_two_html(self,response):
        article_list = response.xpath("//article")
        for article in article_list:
            item = DaomubijiItem()

            name = article.xpath("./a/text()").extract_first().split()
            # 卷名
            item['volume_name'] = name[0]

            # 章节数
            item['zh_num'] = name[1]

            # 章节名称
            if len(name) == 2:
                item['zh_name'] = name[1]
            else:
                item['zh_name'] = name[2]

            # 章节连接
            item['zh_link'] = article.xpath("./a/@href").extract_first()

            yield scrapy.Request(
                url = item['zh_link'],
                # meta 参数： 传递item对象到下一个解析函数
                meta = {'item' : item},
                callback=self.parse_three_html
            )

    def parse_three_html(self, response):
        # 获取上一个函数传递过来的item对象
        item = response.meta['item']

        p_list = response.xpath("/html/body/section/div[1]/div/article//p/text()").extract()

        item['zh_content'] = '\n'.join(p_list)

        yield item