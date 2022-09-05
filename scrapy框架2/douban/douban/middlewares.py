# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class DoubanSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i
    
    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
class DoubanCookiesMiddleware:
    def process_request(self, request, spider):
        print(2222222)
        request.meta['cookies'] = {'ll': '"118254"', 'bid': 'IHGkoqBDJKM', '__utmc': '81379588', '__utmz': '81379588.1661951554.1.1.utmcsr', '_ga': 'GA1.1.1538874449.1661951058', '__gads': 'ID', '__gpi': 'UID', 'gr_user_id': '782b93b5-b964-482b-a938-8f1c27e1c013', '_vwo_uuid_v2': 'DA38A8464D7EBD54ED996DF06110FD7E2|49f9176ca438d603eaf6515550d283b8', '__yadk_uid': 'JCve9d0WCFue9LK9rsi8CYEIldRKP7UA', '_ga_RXNMP372GL': 'GS1.1.1661951061.1.1.1661952048.22.0.0', '_pk_ref.100001.3ac3': '%5B%22%22%2C%22%22%2C1661958961%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D', '_pk_ses.100001.3ac3': '*', '__utma': '81379588.1538874449.1661951058.1661951554.1661958961.2', 
'viewed': '"4913064_35517022_30396222_35886207_35587028_35658993"', 'dbcl2': '"168282384:Lm19wc1r9/E"', 'ck': 'TZzU', 'gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03': '9e7d993a-fb91-41c6-9efd-99d6d2c6d672', 'gr_cs1_9e7d993a-fb91-41c6-9efd-99d6d2c6d672': 'user_id%3A1', 'gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_9e7d993a-fb91-41c6-9efd-99d6d2c6d672': 'true', 'push_noty_num': '0', 'push_doumail_num': '0', '__utmt_douban': '1', '__utmt': '1', '_pk_id.100001.3ac3': 'f54566227e6602f5.1661951554.2.1661966369.1661953599.', '__utmb': '81379588.34.10.1661958961'}

        request.cookies ={'ll': '"118254"', 'bid': 'IHGkoqBDJKM', '__utmc': '81379588', '__utmz': '81379588.1661951554.1.1.utmcsr', '_ga': 'GA1.1.1538874449.1661951058', '__gads': 'ID', '__gpi': 'UID', 'gr_user_id': '782b93b5-b964-482b-a938-8f1c27e1c013', '_vwo_uuid_v2': 'DA38A8464D7EBD54ED996DF06110FD7E2|49f9176ca438d603eaf6515550d283b8', '__yadk_uid': 'JCve9d0WCFue9LK9rsi8CYEIldRKP7UA', '_ga_RXNMP372GL': 'GS1.1.1661951061.1.1.1661952048.22.0.0', '_pk_ref.100001.3ac3': '%5B%22%22%2C%22%22%2C1661958961%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D', '_pk_ses.100001.3ac3': '*', '__utma': '81379588.1538874449.1661951058.1661951554.1661958961.2', 
'viewed': '"4913064_35517022_30396222_35886207_35587028_35658993"', 'dbcl2': '"168282384:Lm19wc1r9/E"', 'ck': 'TZzU', 'gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03': '9e7d993a-fb91-41c6-9efd-99d6d2c6d672', 'gr_cs1_9e7d993a-fb91-41c6-9efd-99d6d2c6d672': 'user_id%3A1', 'gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_9e7d993a-fb91-41c6-9efd-99d6d2c6d672': 'true', 'push_noty_num': '0', 'push_doumail_num': '0', '__utmt_douban': '1', '__utmt': '1', '_pk_id.100001.3ac3': 'f54566227e6602f5.1661951554.2.1661966369.1661953599.', '__utmb': '81379588.34.10.1661958961'}

class DoubanDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
