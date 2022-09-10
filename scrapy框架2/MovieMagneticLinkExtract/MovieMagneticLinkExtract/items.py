# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MoviemagneticlinkextractItem(scrapy.Item):
    # define the fields for your item here like:

    # 影片类型电影或剧集
    # movie_type = scrapy.Field

    # 影片封面
    cover_Image = scrapy.Field()

    # 影片标题介绍
    title = scrapy.Field()

    # 影片译名
    translated_name = scrapy.Field()

    # 影片原名
    old_name = scrapy.Field()

    # 产地
    country = scrapy.Field()

    # 年代
    years = scrapy.Field()

    # 上映日期
    release_date = scrapy.Field()

    # 类别
    category = scrapy.Field()

    # 影片时长
    duration = scrapy.Field()

    # 语言
    language = scrapy.Field()

    # IMDb评分
    imdb_grade = scrapy.Field()

    # IMDb id
    imdb_id = scrapy.Field()

    # IMDb链接
    imdb_link = scrapy.Field()

    # 豆瓣评分
    douban_grade = scrapy.Field()

    # 豆瓣id
    douban_id = scrapy.Field()

    # 豆瓣链接
    douban_link = scrapy.Field()

    #烂 番 茄
    rottenTomatoes = scrapy.Field()

    #Metacritic 　
    metacritic  = scrapy.Field()

    # 导演
    director = scrapy.Field()

    # 编剧
    scriptwriter = scrapy.Field()

    # 演员
    actor = scrapy.Field()

    # 简介
    intro = scrapy.Field()

    # 来源
    source = scrapy.Field()

    # 磁力
    magnetism_link = scrapy.Field()

    # 是否更新磁力
    isUpdate_magnetism_link = scrapy.Field()
    # sum
    # name = scrapy.Field()
