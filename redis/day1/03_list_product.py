import redis
import random
import time

r = redis.Redis(
    host='localhost',
    port=6379,
    db=0
)


# 生成很多个URL地址，放到redis列表中
for i in range(1, 51):
    url = 'http://www.***.com/#page=' + str(i)
    # 放到redis列表
    r.lpush('xiaomi:urls',url)


    time.sleep(random.randint(3,5))