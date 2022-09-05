'''
Author: 815931614 815931614@qq.com
Date: 2022-08-31 21:21:26
LastEditors: 815931614 815931614@qq.com
LastEditTime: 2022-08-31 23:26:52
FilePath: \MyNote\scrapy框架2\douban\douban\items.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AEfi
'''
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()


    firstLabel = scrapy.Field() # 一级标签
    secondLabel = scrapy.Field() # 二级标签
    
    bookName = scrapy.Field()   # 读物名称
    author = scrapy.Field() # 作者
    translator = scrapy.Field() # 译者
    publishingHouse = scrapy.Field() # 出版公司
    publicationTime = scrapy.Field() # 发行时间
    readingCcores = scrapy.Field() # 读物评分
    synopsis = scrapy.Field() # 简介
    cover_img = scrapy.Field() # 封面图片
    bookPrice = scrapy.Field() # 纸质版价格


    isbn = scrapy.Field() # ISBN编号
    numberPages = scrapy.Field() # 页数

