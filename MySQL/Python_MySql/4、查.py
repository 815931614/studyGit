import pymysql



db = pymysql.connect(host='localhost',
                     user='root',
                     passwd='123456',
                     database='sh256',
                     charset='utf8')


cur =  db.cursor()

sql = "select paynum from paypassword where paypass=(%s);"

cur.execute(sql,['f9200e0934f3c98a0a6b7dcfbc5753aa0d6e4a401a89db72cccd84e2845d057a'])

print(cur.fetchone())

sql = "select paynum from paypassword where paypass=(%s);"

cur.execute(sql,['f9200e0934f3c98a0a6b7dcfbc5753aa0d6e4a401a89db72cccd84e2845d057a'])

print(cur.fetchone())
cur.close()
db.close()