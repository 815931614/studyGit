import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re

from MovieMagneticLinkExtract.items import MoviemagneticlinkextractItem

class YinfansSpider(CrawlSpider):
    name = 'yinfans'
    allowed_domains = ['yinfans.me']
    start_urls = ['https://www.yinfans.me/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='/html/body/div[4]/div[2]/div[2]/div/a[@class="next"]')),
        Rule(LinkExtractor(restrict_xpaths='//a[@class="zoom"]'), callback='parse_item'),
    )

    def parse_item(self, response):

        magnet = re.findall(r'magnet:\?xt=urn:btih:',response.text)
        if not magnet: return


        item = MoviemagneticlinkextractItem()


        # 封面图片
        item['cover_Image'] = response.xpath('//*[@id="post_content"]/p[1]/a/img/@src').extract_first()

        # 影片标题介绍
        item['title'] = response.xpath('//*[@id="content"]/div[1]/h1/text()').extract_first()


        translated = response.xpath('//*[@id="post_co ntent"]/p[2]/text()').extract()
        if not translated: return
        translated_info = re.subn(r'\s',"","".join(translated))[0] + "◎"
        # print(translated_info)
        # 影片译名
        item['translated_name'] = re.findall('◎译名(.*?)◎', translated_info)

        # 影片原名
        item['old_name'] = re.findall('◎片名(.*?)◎', translated_info)

        # 年代
        item['years'] = re.findall('◎年代(.*?)◎', translated_info)

        # 产地
        item['country'] = re.findall('◎产地(.*?)◎', translated_info)

        # 上映日期
        item['release_date'] = re.findall('◎上映日期(.*?)◎', translated_info)

        # 类别
        item['category'] = re.findall('◎类别(.*?)◎', translated_info)

        # 影片时长
        item['duration'] = re.findall('◎片长(.*?)◎', translated_info)

        # 语言
        item['language'] = re.findall('◎语言(.*?)◎', translated_info)

        urlformat = lambda url: [i for i in url.split("/") if i != ""][-1]

        # IMDb评分
        item['imdb_grade'] = re.findall('◎IMDb评分(.*?)◎', translated_info)

        # IMDb链接
        item['imdb_link'] = response.xpath(
            "//*[@id='post_content']/p[2]/a[contains(text(),'www.imdb.com')]/text()").extract_first()

        # IMDb_id
        item['imdb_id'] = None
        if item['imdb_link']:
            item['imdb_id'] = urlformat(item['imdb_link'])

        # 豆瓣评分
        item['douban_grade'] = re.findall('◎豆瓣评分(.*?)◎', translated_info)

        # 烂 番 茄
        item['rottenTomatoes'] = re.findall('◎烂番茄(.*?)◎', translated_info)

        # Metacritic 　
        item['metacritic'] = re.findall('◎Metacritic(.*?)◎', translated_info)

        # 豆瓣链接
        item['douban_link'] = response.xpath(
            "//*[@id='post_content']/p[2]/a[contains(text(),'movie.douban.com')]/text()").extract_first()

        # douban_id
        item['douban_id'] = None
        if item['douban_link']:
            item['douban_id'] = urlformat(item['douban_link'])
        # 导演
        item['director'] = re.findall('◎导演(.*)◎', translated_info)

        # 编剧
        item['scriptwriter'] = re.findall('◎编剧(.*?)◎', translated_info)

        # 演员
        actor = []
        for t in translated:
            if t == '\n':
                continue
            if '◎演' in t or "◎主" in t:
                actor.append(re.subn(r'\u3000| |\n|','',t)[0][3:])
            elif actor and  '◎' not in t:
                actor.append(re.subn(r'\u3000| |\n', '', t)[0])


        item['actor'] = actor


        # if actor:
        #     item['actor'] = re.findall(r'[\u4e00-\u9fa5]*/[a-zA-Z]*',actor[0])

        # 简介
        item['intro'] = response.xpath('//*[@id="post_content"]/p[4]/text()').extract()


        # 磁力
        item['magnetism_link'] ={}
        tr_list = response.xpath('//*[@id="cili"]//tr')
        for tr in tr_list:
            if  tr.xpath("./td/a[contains(@href,'magnet:')]").get():
                magnetism_name = tr.xpath("./td/a/b/text()").get() +'【' + tr.xpath("./td/a/span/span[2]/text()").get() + '】'
                magnetism_link = tr.xpath("./td/a/@href").get().split('&')[0]
                item['magnetism_link'][magnetism_name] = magnetism_link


        # print(item)
        # sum
        # item['name'] = response.xpath('')
        if not item['old_name'] and not item['imdb_id'] and not item['douban_id']:
            return
        yield item
        # yield item

