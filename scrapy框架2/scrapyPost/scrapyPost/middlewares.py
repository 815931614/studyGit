# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

class CheckUserAgent:

    def process_response(self,request,response,spider):

        print(request.headers)
        # print(response.request)
        return response  
