# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy 
from pymongo import MongoClient
from scrapy.pipelines.images import ImagesPipeline
class JilePipeline:
    def process_item(self, item, spider):
        return item

class ImageDownLoadPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for url in item['img_list']:
            
            yield scrapy.Request(
                url = url
            )
        
    def file_path(self, request, response=None, info=None, *, item=None):
        imgNmae = request.url.split('/')[-1]
        return imgNmae
    # def process_item(self, item, spider):
    #     print("返回")
    #     return item

    def item_completed(self, results, item, info):
        return item


class JileMongoDBPipeline:
    def open_spider(self, spider):
        self.clien = MongoClient()
        self.collection = self.clien['ppbav']['arttype']

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item