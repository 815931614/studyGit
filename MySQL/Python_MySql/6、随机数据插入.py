import pymysql
from faker import Faker


db = pymysql.connect(host='localhost',
                     database='sh256',
                     user='root',
                     passwd='123456',
                     charset='utf8')



cur = db.cursor()
f = Faker(["zh_CN"])


try:
    sql = f"insert into paypassword values (%s,%s)"
    namelist = []
    with open('../../sh256/payPassWord.txt','r') as r:
        ps = r.read().split('\n')
    for i in ps:
        k = i.split('---')[0]
        v = i.split('---')[1]
        namelist.append([k,v])

    print('ok')
    cur.executemany(sql,namelist)
    db.commit()



except Exception as e:
    db.rollback()
    print(e)



cur.close()
db.close()