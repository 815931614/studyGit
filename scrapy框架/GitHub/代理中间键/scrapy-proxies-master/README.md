# Scrapy 的随机代理中间件(http://scrapy.org/)

使用列表中的随机代理处理 Scrapy 请求，以避免 IP 禁令并提高爬网速度。

[从http://www.hidemyass.com/](http://www.hidemyass.com/)等网站获取您的代理列表（复制粘贴到文本文件并重新格式化为[http://host:port](http://host:port/)格式）

## 安装

快捷方式：

    pip install scrapy_proxies

或签出源并运行

    python setup.py install


settings.py
-----------

    # 多次重试，因为代理通常会失败
    RETRY_TIMES = 10
    # 重试大多数错误代码，因为代理失败的原因不同
    RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]
    
    DOWNLOADER_MIDDLEWARES = {
        'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
        'scrapy_proxies.RandomProxy': 100,
        'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    }
    
    # 包含如下条目的代理列表
    # http://host1:port
    # http://username:password@host2:port
    # http://host3:port
    # ...
    PROXY_LIST = '/path/to/proxy/list.txt'
    
    # Proxy mode
    # 0 = 每个请求都有不同的代理
    # 1 = 只从列表中获取一个代理，并将其分配给每个请求
    # 2 = 在设置中放入要使用的自定义代理
    PROXY_MODE = 0
    
    # 如果代理模式是2，取消注释
    # CUSTOM_PROXY = "http://host1:port"


对于旧版本的 Scrapy（1.0.0 之前），您必须改用 scrapy.contrib.downloadermiddleware.retry.RetryMiddleware 和 scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware 中间件。


你的爬虫
-----------

在每个回调中，通过检查站点徽标或其他一些重要元素，确保代理 /really/ 返回您的目标页面。如果不是 - 使用 dont_filter=True 重试请求

    if not hxs.select('//get/site/logo'):
        yield Request(url=response.url, dont_filter=True)
