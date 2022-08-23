
import pymysql

# 数据库连接
db = pymysql.connect(host='43.142.106.22',
                     port=3306,
                     user='root',
                     password='123456',
                     database='test',
                     charset='utf8')


# 获取游标对象
cur = db.cursor()


# 数据库操作

# 执行sql语句
cur.execute('insert into textbook(bookName,createTime,shoopTime,xiajiaTime) values("book3","1999-06-06",now(),"1999")')

# 将修改内容提交到数据库
db.commit()

# 关闭游标和数据库连接
cur.close()
db.close()