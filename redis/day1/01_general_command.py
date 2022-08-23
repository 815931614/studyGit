import redis

# 创建数据库连接对象
r = redis.Redis(host='127.0.0.1',port=6379,db=0)

# 查看所有key:[b'spider::urls']
print(r.keys("*"))

# 查看键类型:type
print(r.type('spider::urls'))

# 判断键是否存在:返回值0  或 1
print(r.exists('spider::urls2'))

# 删除key
r.delete('name')

