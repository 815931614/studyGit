import redis

r = redis.Redis(
    host='localhost',
    port=6379,
    db=0
)


while True:
    # 从列表中获取地址
    url = r.brpop('xiaomi:urls',5)

    # (b'xiaomi:urls', b'http://www.***.com/#page=3')
    print(url)

    if url:
        print(url[1].decode())
    else:
        print('抓取结束')
        break