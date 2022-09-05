# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter



from pymongo import MongoClient

import re


class MovieMongoDBPipeline:
    def open_spider(self,spider):
        client = MongoClient()
        self.conn = client['movie']['film']

    def process_item(self,item,spider):
        print(item)
        return item

        # self.conn.insert_one()








class MovieDisposeResult:


    def process_item(self,item,spider):
        # 对item中数据进行格式处理
        for k,v in dict(item).items():
            if k !='actor' and  k !='category':
                if k == 'intro':
                    item[k] = [i.replace(" ",'').strip() for i in v]
                elif type(v) == list:
                    if  v:
                        item[k] = v[0].strip()
                    else:
                        item[k] = ''

                elif type(v) == str:
                    item[k] = v.strip()

                elif v == None:
                    item[k] = ""
                if k == 'title':
                    item[k] = v.replace(" ",'')
        return item