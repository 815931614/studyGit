import redis

r = redis.Redis(
    host='localhost',
    port=6379,
    db=0
)

# set:设置{'mystring':'python'}
r.set('mystring','python')


# 获取mystring的值,打印查看类型
print(r.get('mystring').decode())


# 设置mystring,当键不存在的时候设置，存在则不做操作
r.setnx('mystring','redis')


# 一次性设置多个键值对，(mystring2:mysql,'mystring2','redis')
r.mset({'mystring2':'redis','mystring3':'mysql'})


# 一次性获取 三个键的所有值，查看结果类型？
print(r.mget('mystring2','mystring','mystring3'))


# 打印mystring的长度
print(r.strlen('mystring'))


# 设置number值为20
r.set('number',20)
print(r.get('number'))

# +10
r.incrby('number',10)
print(r.get('number'))


# -10
r.decrby('number',10)
print(r.get('number'))

# +8.88
r.incrbyfloat('number', 8.88)
print(r.get('number'))


# -8.88
r.incrbyfloat('number', -8.88)
print(r.get('number'))


# 查看number的值

