settings

REDIS_URL = 'redis://127.0.0.1:6379'

或者

REDIS_HOST = "127.0.0.1:6379"

REDIS_PORT = 6379







去重方式:hashlib.sha1().hexdigest()

settings.py说明



    # 重新指定调度器: 启用Redis调度器存储请求队列
    SHEDULER = "scrapy_redis.scheduler.Scheduler"
    
    # 重新指定去重机制: 确保所有的爬虫通过Redis去重
    DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
    
    # 不清除Redis队列: 暂停/恢复/断电续爬,True:不清除,False:清除
    SCHEDULER_PERSIST = True
    
    # 优先级队列(默认)
    SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.priorityQueue'
    # 可选用的其他队列
    # 先进先出队列
    SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.FifoQueue'
    # 后进先出队列
    SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.LifoQueue'
    
    # Redis管道
    ITEM_PIPELINES = {
        'scrapy_redis.pipelines.RedisPipeline' : 200
    }

爬虫文件

```python
from scrapy_redis.spiders import RedisSpider



class ScrapyRedisDemoSpider(RedisSpider):
    name = "ScrapyRedisDemo"
    allowed_domains = ['ScrapyRedisDemo.com']
    redis_key = 'ScrapyRedisDemo'
    
    
    

from scrapy_redis.spiders import RedisCrawlSpider

class ScrapyRedisDemoSpider(RedisCrawlSpider):
    name = "ScrapyRedisDemo"
    allowed_domains = ['ScrapyRedisDemo.com']
    redis_key = 'ScrapyRedisDemo'
    
    rules = (
    	Rule(LinkExtractor(),callback='parse_page',follow=True)
    )
```

