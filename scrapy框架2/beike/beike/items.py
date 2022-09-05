'''
Author: 815931614 815931614@qq.com
Date: 2022-08-31 16:20:25
LastEditors: 815931614 815931614@qq.com
LastEditTime: 2022-08-31 17:45:13
FilePath: \MyNote\scrapy框架2\beike\beike\items.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BeikeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    loupanNmae = scrapy.Field()

    resblock = scrapy.Field()

    address = scrapy.Field()
