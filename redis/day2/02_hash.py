import redis


r = redis.Redis(
    host='localhost',
    port=6379,
    db=0
)


# 新建1条键名为userinfo的数据，包含属性username值自定义
r.hset('userinfo','username','tom')


r.hset('userinfo','username','tom2')

print(r.hget('userinfo','username'))

r.hset('userinfo',mapping={'password':'123456','age' : 22,'height':231})

print(r.hgetall('userinfo'))

r.hdel('userinfo','height')

r.hkeys('userinfo')

r.hmget('userinfo',r.hkeys('userinfo'))