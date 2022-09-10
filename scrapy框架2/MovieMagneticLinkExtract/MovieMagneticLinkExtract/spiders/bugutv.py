# coding:utf-8
'''
@Project ：MyNote
@File    ：bugurv.py
@IDE     ：PyCharm
@Author  ：lifucheng
@Date    ：2022/9/5 0:19
'''
import re
import scrapy
from  scrapy_redis.spiders import RedisSpider
from MovieMagneticLinkExtract.items import MoviemagneticlinkextractItem

class BugutvSpider(scrapy.Spider):

    name = 'bugutv'
    allowed_domains = ['www.bugutv.net']
    start_urls = [
        'https://www.bugutv.net/4kuhd', # 4K蓝光原盘
        'https://www.bugutv.net/4kmovie', # 4K电影
        'https://www.bugutv.net/dolbyvision', # 杜比视界
        'https://www.bugutv.net/4kdocu', # 4K纪录片
        'https://www.bugutv.net/bluraymovie' # 蓝光原盘
    ]

    def parse(self, response):
        '''
        提取电影列表中详情页链接
        :param response:
        :return:
        '''

        detailsLink_list = response.xpath("//article[contains(@id,'post-')]/div[1]/div/a/@href").extract()
        for detailsLink in detailsLink_list:
            yield scrapy.Request(
                detailsLink,
                callback=self.parse_detail
            )
            # break
        # yield scrapy.Request(
        #     detailsLink_list[28],
        #     callback=self.parse_detail
        # )
        next_url = response.xpath("/html/body/div[1]/main/div[2]/div[1]/div/div/div[2]/a[contains(@class,'next')]/@href").extract_first()
        if next_url:
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )
    def parse_detail(self, response):

        magnet = re.findall(r'magnet:\?xt=urn:btih:', response.text)
        if not magnet: return
        # print(response.text)
        item = MoviemagneticlinkextractItem()

        # 封面图片
        item['cover_Image'] = response.xpath('//div/div[3]/div[1]/figure/img/@src').extract_first()


        # 影片标题介绍
        item['title'] = response.xpath('//*[@id="app"]/div[2]/div[1]/header/h1/text()').extract_first()

        # 影片译名
        item['translated_name'] = re.findall(f'◎译.*?名(.*?)<br>', response.text)

        # 影片原名
        item['old_name'] = re.findall(f'◎片.*?名(.*?)<br>', response.text)

        # 年代
        item['years'] = re.findall(f'◎年.*?代(.*?)<br>', response.text)

        # 产地
        item['country'] = re.findall(f'◎产.*?地(.*?)<br>', response.text)

        # 上映日期
        item['release_date'] = re.findall(f'◎上映 日期(.*?)<br>', response.text)

        # 类别
        item['category'] = response.xpath("//div/div[3]/div[1]/p[1]/a[contains(@href,'https://www.bugutv.net/tag/')]/text()").extract()

        # 影片时长
        item['duration'] = re.findall(f'◎片.*?长(.*?)<br>', response.text)

        # 语言
        item['language'] = re.findall(f'◎语.*?言(.*?)<br>', response.text)

        urlformat = lambda url: [i for i in url.split("/") if i != ""][-1]

        # IMDb评分
        item['imdb_grade'] = re.findall(f'◎IMDb评分(.*?)<br>', response.text)

        # IMDb链接
        item['imdb_link'] = response.xpath("//div/div[3]/div[1]/p[1]/a[contains(@href,'www.imdb.com')]/text()").extract_first()

        # IMDb_id
        item['imdb_id'] =None
        if item['imdb_link']:
            item['imdb_id'] = urlformat(item['imdb_link'])

        # 豆瓣评分
        item['douban_grade'] = re.findall(f'◎豆瓣 评分(.*?)<br>', response.text)

        # 烂 番 茄
        item['rottenTomatoes'] = re.findall(f'◎烂 番 茄(.*?)<br>', response.text)

        # Metacritic 　
        item['metacritic'] = re.findall(f'◎Metacritic(.*?)<br>', response.text)


        # 豆瓣链接
        item['douban_link'] = response.xpath("//div/div[3]/div[1]/p[1]/a[contains(@href,'movie.douban.com')]/text()").extract_first()

        # douban_id
        item['douban_id'] = None
        if item['douban_link']:
            item['douban_id'] =  urlformat(item['douban_link'])
        # 导演
        item['director'] = re.findall(f'◎导.*?演(.*?)<br>', response.text)

        # 编剧
        item['scriptwriter'] = re.findall(f'◎编.*?剧(.*?)<br>', response.text)

        # 演员
        item['actor'] = []
        actor = re.findall(f'◎主.*?演(.*?)</p>', response.text)
        if actor:
            item['actor'] = [i.strip() for i in actor[0].split("<br>")]



        # 简介
        item['intro'] = response.xpath('//div/div[3]/div[1]/p[3]/text()').extract()

        # 磁力

        item['magnetism_link'] = response.xpath("//div/div[3]/div[1]/p/a[contains(@href,'magnet:?xt=')]/..//text()").extract()
        # print(item)
        # sum
        # item['name'] = response.xpath('')
        if not item['old_name'] and not item['imdb_id'] and not item['douban_id']:
            return
        yield item