# Redis—day01-note

### Redis介绍

- 特点级优点

  ```
  1、开源的，使用C编写,基于内存且支持持久化
  2、高性能Key-Value的NoSQL数据库
  3、支持数据类型丰富，字符串strings，散列hashes，列表lists，集合sets，
  有序集合sorted sets等等
  4、支持多种编程语言(C C++ Python Java PHP ...)
  ```

- 与其他数据库对比

  ```
  1、Mysql: 关系型数据库，表格，基于磁盘，慢
  2、MongoDB:键值对文档类型数据库，值为JSON文档，基于磁盘，慢，存储数据类型单一
  3、Redis的诞生是为了解决什么问题??
  	解决磁盘IO带来的性能瓶颈
  ```

- 应用场景

  ```
  1、使用Redis来缓存一些经常被用到、或者需要耗费大量资源的内容，通过这些内容放到Redis里面，程序可以快速读取这些内容
  2、一个网站，如果某个页面经常会被访问到，或者创建页面时消耗的资源比较多，不如需要多次访问数据库、生成时间比较长等，我们可以使用Redis将这个页面缓存起来，减轻网站负载，降低网站的延迟，比如说网站首页等；
  ```

- 掌握

  ```
  1、Redis特点
  2、Redis应用场景
  3、Redis和mysql区别
  ```

- Ubuntu

  ```
  # 安装
  sudo apt-get install reids-server
  
  # 服务端启动
  sudo /etc/init.d/redis-server start|stop|restart|status
  
  # 客户端连接
  redis-cli -h IP地址 -p 6379 -a 密码  
  ```

- Windows

  ```
  # 解决将Redis服务安装到本地服务
  1、重命名redis.windows.conf 为 redis.conf,作为redis服务的配置文件
  2、cmd命令行，进入到redis-server.exe所在目录
  3、执行:redis-server --service-install redis.conf --loglevel verbose
  4、计算机-管理-服务-Redis-启动
  
  # 卸载
  到 redis-server.exe 所在路径执行
  1、redis-server --service-uninstall
  2、sc delete Redis
  ```

- 允许远程连接

  ```
  1、注释掉本地IP地址绑定
  	bind 127.0.0.1
  2、关闭保护模式
  	protected-mode no
  3、重启服务
  	sudo /etc/init.d/redis-server restart
  ```

  

### 数据类型

### 字符串类型(string)

#### 特点

```
字符串、数字、都会转为字符串来存储
```

#### 必须掌握命令

```
1、set key value
2、setnx key value
3、set key value ex seconds
4、get key
5、mset key1 value1 key2 value2
6、mget key1 key2 key3
7、strlen key
# 数字操作
8、incr key
9、decr key
10、incrby key 步长
11、decrby key 步长
12、incrbyfloat key number
# 设置过期时间的两种方式
# 方式1
1、set key value ex 3
# 方式2
1、set key value
2、expire key 5 # 秒
3、pexpire key 5 # 毫秒
# 查看存活时间
ttl key
# 删除过期
persist key
```

#### 扩展命令

```
1、append key value
2、setrange key index value
3、getrange key start stop
4、incrby key step
5、decrby key step
```

#### 常用命令

- set | get命令

  **作用：**设置建值，获取键对应的值

  **命令格式：**set key value

  ​					get  key

- set命令之-setnx

  setnx key value **:键不存在时才能进行设置(必须掌握)

  ```python
  # 键不存在，进行设置，如果键已经操作，则不进行任何操作
  ```

- set命令之-ex

  **作用：**设置过期时间

  **命令格式：**set key value ex seconds

  

- mset|mget

  mset key1 value1 key2 value2 key3 value3.....

  mget key1 key2....

  **作用：**同时设置多个值，获取多个值

- strlen

  **作用：**获取值的长度

  **命名格式：**strlen key

  ```
  strlen name
  (integer) 11
  ```

- 字符串索引操作

  **setrange**key索引值value

  **作用：**从索引值开始，value替换原内容

  ```
  127.0.0.1:6379> get message
  "hello world"
  127.0.0.1:6379> setrange message 6 'tarena'
  (integer) 12
  127.0.0.1:6379> get message
  "hello tarena"
  127.0.0.1:6379>
  ```

  **getrange** key 起始值 终止值(包括终止值)

  **作用：**获取指定范围切片内容

  ```
  127.0.0.1:6379> get message
  "hello tarena"
  127.0.0.1:6379> getrange message 0 4
  "hello"
  127.0.0.1:6379> getrange message 0 -1
  "hello tarena"
  ```

- append key value

  **作用：**追加拼接value的值

  ```
  127.0.0.1:6379> get message
  "hello tarena"
  127.0.0.1:6379> append message ' ttt'
  (integer) 16
  127.0.0.1:6379> get message
  "hello tarena ttt"
  127.0.0.1:6379>
  ```

  

#### 整数操作

​	INCRBY key 步长

​	DECRBY key 步长

```
127.0.0.1:6379> set number 10
OK
127.0.0.1:6379> INCRBY number 5
(integer) 15
127.0.0.1:6379> DECRBY number 5
(integer) 10
```

**INCR key: +1操作**
**DECR key： -1操作**

```
127.0.0.1:6379> get number
"10"
127.0.0.1:6379> incr number
(integer) 11
127.0.0.1:6379> decr number
(integer) 10
```



#### 通用命令

```python
# 切换库
select number(0-15)

# 查看键
keys * 

# 键类型
TYPE key

# 键是否存在
exists key

# 删除键
del key

# 键重命名
rename key newkey

# 返回旧值并设置新值(如果键不存在，就创建并赋值)
getset key value

# 清除当前库中所有数据(慎用)
flushdb

# 清除所有库中所有数据(慎用)
flushall
```

#### string数据类型注意

```
# key值取值原则
1、key值不宜过长，消耗内存，且数据中查找这类键值的计算成本高
2、不宜过短，可读性差
# 值
1、一个字符串类型的值最多能存储512M内容
```

### 列表数据类型（List）

#### 列表常用命令总结

​		

```
# 增
1、 LPUSH key value1 value2
2、 RPUSH key value1 value2
3、 RPIPLPUSH source destination
4、 LINSERT key|before value newvalue
# 查
5、 LRANGE key start stop
6、 LLEN key
# 删
7、 LPOP key
8、 RPOP key
9、 BLPOP key timeout
10、 BRPOP key timeout
11、 LREM key count value
12、 LTRIM key start stop
# 改
13、LSET key index newvalue
```

​	

- 特点

  ```
  1、元素时字符串类型
  2、列表头尾增删快、中间增删慢，增删元素时常态
  3、元素可重复
  4、最多包含2^32 -1个元素
  5、索引同Python列表
  ```

- **头尾压入元素( LPUSH | RPUSH )**

  1、LPUSH key value

  2、RPUSH key value

  ```
  
  ```

- **查看|设置 列表元素**
  查看(LRANGE)

  ```
  # lrange key start stop
  lrange mylist1 0 2 # 显示前3个元素
  lrange mylist 0 -1 # 显示列表中所有元素
  ```

  获取列表长度(llen)

  ```
  llen mylist
  ```

  获取指定位置的元素(LINDEX)

  ```
  127.0.0.1:6379> LRANGE mylist 0 -1
  1) "4"
  2) "3"
  3) "2"
  4) "1"
  5) "0"
  127.0.0.1:6379> LINDEX mylist 1
  "3"
  ```

  设置指定位置元素的值(LSET)

  ```
  127.0.0.1:6379> LSET mylist 1 tom
  OK
  127.0.0.1:6379> LRANGE mylist 0 -1
  1) "4"
  2) "tom"
  3) "2"
  4) "1"
  5) "0"
  ```

- **头尾弹出元素(LPOP | RPOP)**

  LPOP key: 从列表头部弹出一个元素

  RPOP key: 从列表尾部弹出一个元素

  RPOPLPUSH  source destination: 从一个列表尾部弹出元素压入到另一个列表头部

  ```
  rpoplpush mylist1 mylist2
  ```

  

- **移除指定元素(LREM)**

  LREM key count value

  ```
  count>0: 表示从头部开始向表尾搜索，移除value相等的元素，数量为count
  count<0: 表示从尾部开始向表头搜索，移除与value相等的元素，数量为count
  count=0: 移除表中所有与value相等的值
  ```

- 去除指定范围外元素(LTRIM)

  LTRIM key start stop

  ```
  127.0.0.1:6379> lrange mylist2 0 -1
  1) "4"
  2) "3"
  3) "2"
  4) "1"
  127.0.0.1:6379> LTRIM mylist2 0 2
  OK
  127.0.0.1:6379> lrange mylist2 0 -1
  1) "4"
  2) "3"
  3) "2"
  127.0.0.1:6379>
  ```

  应用场景:保存微博评论最后500条

  ```
  lrange mylist2 0 499
  ```

- **列表中插入值（LINSERT）**

  LINSERT key BEFORE|AFTER pivot value

  key和pivot不存在，不进行任何操作

  示例代码

  ```
  LINSERT mylist2 after 1 8
  ```

- **阻塞弹出( BLPOP | BRPOP)**

  BLPOP key timeout

  BRPOP key timeout

  ```
  1、如果弹出的列表不存在或者为空，就会阻塞
  2、超时时间设置为0，就是永久阻塞，直到有数据可以弹出
  3、如果多个客户端阻塞再同一个列表上，使用First In First Service原则，先到先服务
  ```

  示例

  ```
  brpop mylist 0 # 永久阻塞
  brpop mylist 3 # 超时时间3秒
  ```

  

#### 	Python操作redis

- 使用流程

  ```python
  import redis
  # 创建数据库连接对象
  r = redis.Redis(host='127.0.0.1',port=6379,db=0,password='123456')
  ```

- 通用命令代码示例

  ```
  
  ```

  



















































