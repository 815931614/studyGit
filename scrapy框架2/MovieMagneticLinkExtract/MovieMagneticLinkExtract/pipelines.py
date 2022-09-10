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
import json
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
        if not item['imdb_id'] and not item['douban_id']:  # 当电影无豆瓣和imdb链接时使用影片原名进行去重
            old_name = self.client.sadd('moviefilter:old_name', item['old_name'])
            item['isUpdate_magnetism_link'] = old_name == 0
        else:
            if item['imdb_id']:
                imdb = self.client.sadd('moviefilter:imdb_id', item['imdb_id'])
                item['isUpdate_magnetism_link'] = imdb == 0
            if item['douban_id']:
                douban = self.client.sadd('moviefilter:douban_id', item['douban_id'])
                item['isUpdate_magnetism_link'] = douban == 0
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


        update_where_sql = {'$or': [{'imdb_id': item['imdb_id']}, {'douban_id': item['douban_id']},{'old_name': item['old_name']}]}
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
        translatedinfo = dict(item.deepcopy())

        if translatedinfo.pop('isUpdate_magnetism_link'):
            self.update_magnetism_link(translatedinfo)
        else:
            self.insert_translatedinfo(translatedinfo)
        return item


    def insert_translatedinfo(self,item):
        '''
        插入新数据
        :param item:
        :return:
        '''
        try:
            magnetism_link = item.pop('magnetism_link')
            key = ','.join(item.keys())
            # 插入磁力链接
            for key,value in item.items():
                if type(value) != str:
                    item[key] = json.dumps(value)

            translatedinfo_sql = f'INSERT INTO translatedinfo({",".join(item.keys())}) VALUES({",".join(["%s"] * len(item))})'
            self.cursor.execute(translatedinfo_sql,tuple(item.values()))

            # 插入磁力链接
            if magnetism_link:
                insert_data = []
                for k, v in magnetism_link.items():
                    insert_data.append([item["old_name"],item['imdb_id'], item['douban_id'], k, v])
                magnetism_sql = 'INSERT INTO magnetism VALUES (%s,%s,%s,%s,%s)'

                self.cursor.executemany(magnetism_sql,insert_data)
            self.conn.commit()
        except Exception as e:
            self.logger.error(e)
            self.conn.rollback()


    def update_magnetism_link(self,item):
        '''
        更新磁力
        :param item:
        :return:
        '''
        if not item['magnetism_link']:  # 如果磁力列表为空，则不更新
            return

        # 取出原数据
        sql = f'SELECT magnetism_link FROM magnetism WHERE douban_id=%s or imdb_id=%s or old_name=%s'
        self.cursor.execute(sql,[item["douban_id"],item["imdb_id"],item["old_name"]])
        fetch = self.cursor.fetchall()
        old_link = [f[0] for f in fetch]
        # # 如果库当前抓取到的磁力信息，都已存在于库中，则不更新
        if not set(item['magnetism_link'].values()) - set(old_link):
            return

        # 新增磁力
        new_link = []
        for magnetism_key, magnetism_value in item['magnetism_link'].items():
            if magnetism_value not in old_link:
                new_link.append([item["old_name"],item["imdb_id"],item["douban_id"],magnetism_key, magnetism_value])
        magnetism_sql = 'INSERT INTO magnetism VALUES (%s,%s,%s,%s,%s)'
        self.cursor.executemany(magnetism_sql, new_link)
        self.conn.commit()
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()






# 对item中数据进行格式处理
class MovieDisposeResult:

    def process_item(self,item,spider):
        item['source'] = spider.name
        if spider.name == 'bugutv':
            return self.data_formatting_bugutv(item)
        elif spider.name == 'yinfans':
            return self.data_formatting_yinfans(item)
    def data_formatting_yinfans(self,item):
        '''
        bugutv
        :param item:
        :return:
        '''

        for key, value in dict(item).items():

            if key != 'actor' and key != 'category':

                if key == 'intro':
                    item[key] = [i.replace(" ", '').strip() for i in value]
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
                    value = [re.sub('①|②|③|④|⑤|⑥|⑦|⑧|⑨|⑩| ', "", value[i].strip()) for i in range(0, len(value), 2) if value[i].strip()]
                    item[key] = {}
                    magnet_name = ""

                    for magnet in range(len(value)):
                        if re.findall('【|】|2160p|1080P', value[magnet]):
                            magnet_name = value[magnet]
                        if value[magnet].startswith('magnet:?xt'):
                            if magnet_name:
                                item[key][magnet_name] = value[magnet]
                            else:
                                item[key][value[magnet-1]] = value[magnet]

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