#### 1. scrapy的基本结构？

​			调度器（请求队列）， 下载器（下载网页），spider（解析提取数据），pipeline（验证和持久化，一般用于存储数据库），引擎（核心） ==>resquests  分析接口，构造请求 =》 发送请求 =》数据清洗解析提取=>入库存储

#### 2.scrapy的中间件？

```
下载中间件：
爬虫中间件：	
```

#### 3.scrapy指纹去重原理和scrappy-redis的去重原理?

```
scrapy的去重原理流程：利用hash值和集合去重。首先创建fingerprint = set()结合，然后将request对象利用sha1对象进行信息摘要，摘要完成之后， 判断hash值是否在集合中，如果在，返回true,如果不在，就add到集合
```

```
fp = self.request_fingerprint(request)
       if fp in self.fingerprints:
           return True
       self.fingerprints.add(fp)
       if self.file:
           self.file.write(fp + os.linesep)
```

scrapy-redis 的去重原理基本是一样的，只不过持久化存储到redis共享数据库中，当请求数据达到10亿级以上
这个时候就会非常消耗内存，一个sha1 40个字节，就会占40G的内存，这个存储绝大部分的数据库无法承受
这个时候就要使用布隆过滤器。

#### 布隆过滤器

四个因素：请求数据，位图长度， 哈希算法个数，误判率
布隆过滤器可以极其高效的判断request请求数据是否已经存在，有一定的误判率，但是如果没有，那么一定就是不存在，这样可以进行高效的进行

#### 如何禁用scrapy中的缓存？

##### 	缓存可以通过两种方式禁用

1. 在setting.py文件中更改与缓存相关的设置中的值。通过保持HTTPCACHE_ENABLED = False
2. 或者可以在运行时完成“ scrapy crawl crawl-name –set HTTPCACHE_ENABLED = False