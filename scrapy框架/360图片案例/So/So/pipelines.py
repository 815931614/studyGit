# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# scrapy 图片管道类
from scrapy.pipelines.images import ImagesPipeline
import scrapy
# 1、继承ImagesPipeline
# 2、重写 类方法
class SoPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # 把图片链接发给调度器
        yield scrapy.Request(
            url = item['img_link']
        )


    # def process_item(self, item, spider):
    #     return item
