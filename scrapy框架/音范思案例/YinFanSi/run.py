from scrapy import cmdline

# cmdline.execute('scrapy crawl yinfansi3'.split())
cmdline.execute('scrapy crawl yinfansi3 -o yinfansi.json'.split())
# cmdline.execute('scrapy crawl yinfansi3 -o yinfansi.csv'.split())
