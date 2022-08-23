# redis_day01回顾

### Redis的特点

```
1、基于key-value的非关系型数据库
2、基于内存存储，速度快
3、基于内存存储，经常当作缓存型数据库使用，常用信息存储在redis数据库中
```

### 五大数据类型

```
1、字符串类型(string)
2、列表类型(list)
3、哈希类型(hash)
4、集合类型(set)
5、有序集合类型(sorted set)
```



#### 字符串类型

```python
#  设置key相关操作
1、set key value
2、setnx key value # 当键不存在的时候设置值，存在则不设置
3、mset k1 v1 k2 v2 k3 v3 # 一次性设置多个
4、set key value ex seconds # 设置过期时间 set strname 'a' ex 3
5、set key value   
   expire key 5  秒
   pexpire key 5 毫秒
   ttl key  # 查看过期时间
   persist key # 删除过期时间
# 获取key相关操作
6、get key
7、mget k1 k2 k3 ... # 获取多个value
8、strlen key  # 长度

# 数字相关操作
7、incrby key 步长 #  加
8、decrby key 步长 #  减
9、incr key # 加一
10、decr key # 减一
11、incrbyfloat key number # 浮点
```

#### 列表类型

```python
# 插入元素相关操作
1、LPUSH key value1 value2 # 头压入
2、RPUSH key value1 value2  # 尾压入
3、RPOPLPUSH source destination #  从一个列表尾部弹出一个元素压入到另一个列表头部
4、LINSERT key after|before value newvalue # 列表中插入值
# 查询相关操作
5、LRANGE key start stop  
6、LLEN key
# 删除相关操作
7、LPOP key # 头弹出
8、RPOP key  # 尾弹出
9、BLPOP key timeout # 头阻塞弹出
10、BRPOP key timeout # 尾阻塞弹出
# timeout必须有，0代表永久阻塞

11、LREM key count value # 去除指定元素
12、LTRIM key start stop # 去除指定范围外元素
# 修改指定元素相关操作
13、LSET key index newvalue
```

# redis_day02笔记

#### 位图操作bitmap

##### 定义

```
1、位图不是真正的数据类型，他是定义在字符串类型中
2、一个字符串类型的值最多能存储512M字节的内容，位上限:2^32
# 1MB = 2024kb
# 1kb = 1024Byte(字节)
# 1Byte = 8bit(位)
```

##### 强势点

```
可以实时的进行统计，极其节省空间。官方在模拟1亿2千8百万用户的模拟环境下，在一台MacBook Pro上，典型的统计如’日用户数‘的时间消耗小于50ms，占用16MB内存
```

##### 常用命令

```python
# 设置某一位上的值(offset是偏移量,从0开始)
setbit key offset value

# 获取某一位上的值
GETBIT key offset

# 统计键所对应的值中有多少个 1
BITCOUNT key [start|end]
```

#### Hash散列数据类型

- 定义

  ```
  1、由field和关联的value组成的键值对
  2、field和value是字符串类型
  3、一个hash中最多包含2^32-1个键值对
  ```

- 优点

  ```
  1、节约内存空间
  2、每创建一个键，它都会为这个键存储一些附加的管理信息(比如这个键的类型，这个键最后一次被访问的时间等)
  3、键越多，redis数据库在存储附件管理信息方面耗费内存越多，花在管理数据库键上的cpu也会越多
  ```

- **缺点(不适合hash情况)**

  ```
  1、使用二进制位操作命令:SETBIT、GETBIT、BITCOUNT等如果想使用这些操作，只能用字符串键
  2、使用过期键功能:键过期功能只能对键进行过期操作，二不能对散列的字段进行过期操作
  ```

  

#### 基本命令操作

```python
# 1、设置单个字段
HSET key field value
HSETNX key field value  # field 不存在再设置

# 2、设置多个字段
HMSET key field value field value

# 3、返回字段个数
HLEN key

# 4、判断字段是否存在(不存在返回0)
HEXISTS key field

# 5、返回字段值
HGET key field

# 6、返回多个字段值
HMGET key field field

# 7、返回所有字段名
HGETALL key

# 8、返回所有字段名
HKEYS key

# 9、返回所有值
HVALS key

# 10、删除指定字段
HDEL key field

# 11、在字段对应值上进行整数增量运算
HINCRBY key filed increment

# 12、在字段对应值上进行浮点数增量运算
HINCRBYFLOAT key field increment
```

#### Python基本方法

```python
# 1、更新一条数据的属性，没有则创建
hset(name, key, value)

# 2、读取这条数据的指定属性，返回字符串类型
hget(name, key)

# 3、批量更新数据(没有则新建)属性
hmset(name, keys, *args)

# 4、批量读取数据(没有则新建)属性
hmget(name, keys, *args)

# 5、获取这条数据的所有属性和对应的值，返回字典类型
hgetall(name)

# 6、获取这个数据的所有属性名，返回列表类型
hkeys(name)

# 7、删除这条数据的指定属性
hdel(name, *keys)
```

#### 集合数据类型(set)

- 特点

```、
1、无序、去重
2、元素是字符串类型
3、最多包含2^32-1个元素
```

- 基本命令

  ```python
  # 1、增加一个或多个元素，自动去重
  SADD key member1 member2
  
  # 2、查看集合中所有元素
  SMEMBERS key
  
  # 3、删除一个或者多个元素，元素不存在自动忽略
  SREM key member1 member2
  
  # 4、元素是否存在
  SISMEMBER key member
  
  # 5、随机返回集合中指定个数的元素，默认为1个
  SRANDMEMBER key [count]
  
  # 6、返回集合中元素的个数，不会遍历整个集合，只是存储在键当中了
  SCARD key
  
  # 7、把元素从源集合移动到目标集合
  SMOVE source destination member
  
  # 8、差集
  SDIFF key key2
  
  # 9、差集保存到另一个集合中
  SDIFFSTORE destination key1 key2
  
  # 10、交集
  SINTER key1 key2
  SINTERSTORE destination key1 key2
  
  # 11、并集
  SUNION key1 key2
  SUNIONSTORE destination key1 key2
  ```

有序集合sortedset

- **特点**

  - 1、有序、去重
  - 2、元素是字符串类型
  - 3、每个元素都关联着一个浮点数分值(score),并按照分支从小到大的顺序排列集合中的元素(分值可以相同)
  - 4、最多包括2^32-1元素

- **基本命令**

  ```python
  # 在有序集合中添加一个成员
  zadd key score member
  
  # 查看指定区间元素(升序)
  zrange key start stop [withscores]
  
  # 查看指定区间元素(降序)
  ZREVRANGE key start stop [withscores]
  
  # 查看指定元素的分值
  # ZSCORE key member
  
  # 返回指定区间元素
  # offset:跳过多少个元素
  # count: 返回几个
  # 小括号： 分开间 zrangebyscore fruits(6000 8000
  zrangebyscore key min max [withscores] [limit offset count]
  
  # 删除成员
  zrem key member
  
  # 增加或减少分值
  zincrby key increment member
  
  # 返回元素排名
  zrank key member
  
  # 返回元素逆序排名
  zrevrank key member
  
  # 删除指定区间内的元素
  zremrangebyscore key min max 
  
  # 返回集合中元素个数
  zcard key
  
  # 返回指定范围中元素的个数
  zcount key min max
  zcount fruits 4 7
  zcount fruits (4 7
                 
  # 并集（先计算权重值，再聚合默认sum）
  zunionstore destination numkeys key [weights 权重值] [AGGREGATE SUM|MIN|MAX]
  
  # 交集:和并集类似，只取相同的元素
  ZINTERSTORE destination numkeys key1 key2 WEIGHTS weight AGGREGATE SUM|MIN|MAX
  ```

  
