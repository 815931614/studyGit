# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DaomubijiPipeline:
    def process_item(self, item, spider):
        filename = 'C:/Users/cc/Desktop/笔记/scrapy框架/三级页面案例/盗墓笔记/{}_{}_{}.txt'.format(
            item['volume_name'],
            item['zh_num'],
            item['zh_name'],

        )
        with open(filename, 'w') as f:
            f.write(item['zh_content'])
        return item
