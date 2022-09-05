# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from faker import Faker
import random

class RandomUserAgentMiddlewares:
    fake = Faker(["zh_CN"])
    def process_request(self,request,spider):
        request.headers['User-Agent'] = self.getRandomUserAgent()         

        # request.mete['Uaer-Agent']  = random.choice(spider.settings.get("USER_AGENT"))
    def getRandomUserAgent(self):
        return self.fake.user_agent()

class ProxyMiddlewares:
    def process_request(self,request,spider):
        
        request.meta['Proxy'] = request.url.split(":")[0] + '://127.0.0.1:10809'
             
    def process_exception(self,request,exception,spider):
        return request
class CheckUserAgent:

    def process_response(self,request,response,spider):

        # print(request.headers)
        # print(response.request)
        return response  