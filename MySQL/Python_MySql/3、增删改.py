
import pymysql



db = pymysql.connect(host='43.142.106.22',
                     user='root',
                     passwd='123456',
                     database='test',
                     charset='utf8')


cur =  db.cursor()


try:
    # 插入操作
    sql = 'insert into textbook values(6,"book6","1999-06-06",now(),"1999")'
    cur.execute(sql)

    # 修改操作
    sql = "update textbook set xiajiaTime=1990 where id = 1.json"
    cur.execute(sql)

    # 删除操作
    sql = "delete from textbook where  xiajiaTime = 1998"
    cur.execute(sql)



except Exception as e:
    db.rollback()