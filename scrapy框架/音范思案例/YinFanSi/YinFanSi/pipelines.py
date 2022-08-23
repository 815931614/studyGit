# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from .settings import *
import pymongo

class YinfansiPipeline:

    def process_item(self, item, spider):
        return item

# 定义一个MySQL管道类
class YinfansiMysqlPipeline:
    def open_spider(self,spider):
        # 爬虫程序启动时，只执行一次，一般用于建立数据库连接
        self.db = pymysql.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PWD,
            database=MYSQL_DB,
            charset=MYSQL_CHAR
        )

        self.cursor = self.db.cursor()

        print('open_spider连接数据库')


    def process_item(self, item, spider):
        sql = 'insert into yinfansi values(%s,%s,%s);'
        film_list = [
            item['name'], item['nobluray'], item['time']
        ]
        self.cursor.execute(sql,film_list)
        self.db.commit()
        return item


    def close_spider(self,spider):
        # 爬虫程序结束时，只执行一次，一般用于断开数据库连接
        self.db.close()
        self.cursor.close()
        print('断开连接')




class YinfansiMongoPipeline:

    def open_spider(self,spider):
        # 链接对象
        self.conn = pymongo.MongoClient(
            host=MONGO_HOST,
            port = MONGO_PORT
        )

        # 库对象
        self.db = self.conn['yinfansi']

        # 集合（表）对象
        self.myset = self.db['filmtab']



    def process_item(self,item,spider):

        film_dict = {
            'name' : item['name'],
            'nobluray' : item['nobluray'],
            'time' : item['time']
        }

        self.myset.insert_one(film_dict)

        return item


    def close_spider(self,spider):
        pass
