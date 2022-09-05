# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdbookredisItem(scrapy.Item):
    bookName = scrapy.Field()
    coverImg = scrapy.Field()
    bookLink = scrapy.Field()
    author = scrapy.Field()
    publishingHouse = scrapy.Field()
    publishingTime = scrapy.Field()
    price = scrapy.Field()
    category = scrapy.Field()


