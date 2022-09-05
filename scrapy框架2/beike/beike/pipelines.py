# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
from beike.items import BeikeItem


class BeikePipeline:
    def open_spider(self,spider):
        self.client = MongoClient()

        self.collection = self.client['beike']['loupan']


    def process_item(self, item, spider):
        if isinstance(item,BeikeItem):
            self.collection.insert_one(dict(item))
            print(item)
        return item
