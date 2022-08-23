import redis

r = redis.Redis(
    host='localhost',
    port=6379,
    db=0
)

# user1： 一年之中第一天和第5天登录
r.setbit('user1',0,1)
r.setbit('user1',4,1)

# user2： 一年之中第100天和第200天登录
r.setbit('user2',99,1)
r.setbit('user2',199,1)

# user3： 一年之中有100天以上登录了，登录时间自己定
for i in range(0,365,2):
    r.setbit('user3',i,1)

# user4： 一年之中有100天以上登录了，登录时间自己定
for i in range(0,365,3):
    r.setbit('user4',i,1)

# 先找出所有用户
user_list = r.keys('user*')
for user in user_list:
    if r.bitcount(user) > 100:
        print(user.decode() + "活跃用户")
    else:
        print(user.decode() + "不活跃用户")

# 统计非活跃用和活跃用户

# 打印活跃用户