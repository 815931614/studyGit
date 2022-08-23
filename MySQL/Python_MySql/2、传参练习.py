import pymysql




# 创建数据库连接
db = pymysql.connect(host='43.142.106.22',
                     port=3306,
                     user='root',
                     passwd='123456',
                     database='test',
                     charset='utf8')



# 创建游标
cur = db.cursor()

# sql = "insert into textbook values('%d','%s','%s',now(),'%s');" %(5,'book5','19980402','1998')
sql = "insert into textbook values(%s,%s,%s,now(),%s);"

try:
    # 列表中的类型全是字符串，自动识别类型
    cur.execute(sql,["5",'book5','19980402','1998'])
    db.commit()

except Exception as e:
    db.rollback() # 回滚到操作之前的状态
    print(e)



# 关闭游标和数据库连接
cur.close()
db.close()