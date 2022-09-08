# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
import re
import redis
import pymysql
from MovieMagneticLinkExtract.settings import *
from scrapy_redis import connection
import logging

class MovieRedisFilterPipeline:
    '''
    由于同一个电影在电影平台的的url地址不同，所以可以用IMDb和豆瓣的地址对电影进行去重
    如果遇到重复，可以对一存在数据库中的电影磁力列表，进行更新和新增

    ◎IMDb链接 https://www.imdb.com/title/tt1618442
    ◎豆瓣链接　https://movie.douban.com/subject/10440076/

    将IMDb链接和豆瓣链接的页面id编号，存储到redis中，


    tt1618442 + 10440076

    '''
    def open_spider(self,spider):
        self.client = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            db=0

        )

    def process_item(self,item,spider):

        isaddd =self.client.sadd('moviefilter',item['imdb_id'] + ":" + item['douban_id'])

        item['isUpdate_magnetism_link'] = isaddd == 0

        return item



# mongodb
class MovieMongoDBPipeline:

    def open_spider(self,spider):
        client = MongoClient()
        self.conn = client['movie']['film']


    def process_item(self,item,spider):

        # 判断该电影是否已经在数据库中，如果存在则对原数据中的磁力链接列表进行比较新增
        if item['isUpdate_magnetism_link']:
            self.update_magnetism_link(item)
        else:
            item_dict = dict(item)
            del item_dict['isUpdate_magnetism_link']
            self.conn.insert_one(item_dict)
        return item

    def update_magnetism_link(self,item):

        if not item['magnetism_link']: # 如果磁力列表为空，则不更新

            return


        # 取出mongo中该电影的磁力信息
        find_sql = [{'$match':{'$or':[{'imdb_id': item['imdb_id']}, {'douban_id': item['douban_id']}]}},{'$project':{'magnetism_link':'$magnetism_link','_id':0}}]
        old_link = self.conn.aggregate(find_sql).next()

        # 如果库当前抓取到的磁力信息，都已存在于库中，则不更新
        if not set(item['magnetism_link'].values()) - set(old_link['magnetism_link'].values()):
            return


        # 更新
        magnetism_link = old_link['magnetism_link']
        for magnetism_key, magnetism_value in item['magnetism_link'].items():
            if magnetism_value not in magnetism_link.values():
                magnetism_link[magnetism_key] = magnetism_value


        update_where_sql = {'$or': [{'imdb_id': item['imdb_id']}, {'douban_id': item['douban_id']}]}
        self.conn.update_one(update_where_sql,{"$set":{'magnetism_link':magnetism_link}})

# mysql
class MovieMysqlPipeline:

    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            database=MYSQL_DATABASE,
            charset='utf8',
            user=MYSQL_USER,
            password=MYSQL_PASSWORD
        )
        self.cursor = self.conn.cursor()
        self.logger = logging.getLogger(spider.name)


    def process_item(self, item, spider):
        # print(item)
        if item['isUpdate_magnetism_link']:
            self.update_magnetism_link(item)
        else:
            self.insert_translatedinfo(item)



    def insert_translatedinfo(self,item):

        # 插入磁力链接
        magnetism_sql = 'INSERT INTO translatedinfo() values ()'


        # 插入电影信息
        translatedinfo_sql = 'INSERT INTO translatedinfo VALUES ()'

        if self.execute(translatedinfo_sql):
            self.logger.error(f"MySQL电影信息插入失败,sql:({translatedinfo_sql})")





    def update_magnetism_link(self,item):
        pass


    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()


    def execute(self,sql):
        try:

            self.cursor.execute(sql)
            self.conn.commit()
        except:

            self.conn.rollback()
            return False



# 对item中数据进行格式处理
class MovieDisposeResult:

    def process_item(self,item,spider):
        item['source'] = spider.name
        if spider.name == 'bugutv':
            return self.data_formatting_bugutv(item)


    def data_formatting_bugutv(self,item):
        '''
        bugutv
        :param item:
        :return:
        '''

        for key, value in dict(item).items():

            if key != 'actor' and key != 'category':

                if key == 'intro':
                    item[key] = [i.replace(" ", '').strip() for i in value]
                elif key == 'magnetism_link':

                    item[key] = {re.sub('①|②|③|④|⑤|⑥|⑦|⑧|⑨|⑩| ', "", value[i].strip()): value[i + 1].replace(" ", '').strip() for
                               i in range(0, len(value), 2)}
                    for i in value:
                        pass
                elif type(value) == list:
                    if value:
                        item[key] = value[0].strip()
                    else:
                        item[key] = ''

                elif type(value) == str:
                    item[key] = value.strip()

                elif value == None:
                    item[key] = ""
                if key == 'title':
                    item[key] = value.replace(" ", '')

        return item