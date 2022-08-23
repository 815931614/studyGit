import redis

r = redis.Redis(host='localhost',db=0,port=6379)
# lpush rpush 命令
r.lpush('tedu:python','socket','pythonweb')
r.rpush('tedu:python','spiderman')

# 查看:[b'pythonweb', b'socket', b'spiderman']
print(r.lrange('tedu:python', 0 , -1))

# 从列表尾部弹出一个元素
r.rpop('tedu:python')

# 从列表头部弹出一个元素
r.lpop('tedu:python')

# 列表尾部插入3个元素
r.rpush('tedu:python','html','css','js')

# 删除索引为2的元素
r.lrem('tedu:python',1,r.lindex('tedu:python',2).decode())

# 保留列表中的2个元素
r.ltrim('tedu:python',0,1)

# 把表索引为0的元素设置为：redis
r.lset('tedu:python',0,'redis')

# 在redis元素的后面插入一个元素:AI
r.linsert('tedu:python','after','redis','AI')


# 获取列表长度
r.llen('tedu:python')

print(r.lrange('tedu:python',0, -1))


# 删除tedu:python
r.delete('tedu:python')