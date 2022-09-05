'''
Author: 815931614 815931614@qq.com
Date: 2022-08-31 18:17:34
LastEditors: 815931614 815931614@qq.com
LastEditTime: 2022-08-31 19:25:20
FilePath: \MyNote\scrapy框架2\yangguang\yangguang\pipelines.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AEde
'''
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from pymongo import MongoClient
import re

class YangguangPipeline:

    def open_spider(self, spider):
        client = MongoClient()
        self.collection = client['yangguang']['yg']

    def process_item(self, item, spider):

       

        # self.collection.insert_one(dict(item))
        return item

    def process_content(self,content):
        # 替换列表中的无效字符
        content = [re.sub(r'\xa0|\s',"",i) for i in content]
        content = [i for i in content if i]   # 去除列表中空字符
        return content