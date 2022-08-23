import  pymysql



db = pymysql.connect(host='43.142.106.22',
                     user='root',
                     passwd='123456',
                     database='test',
                     charset='utf8')






cur = db.cursor()


# # 存储文件
# with open('./images/test.jpg','rb') as fd:
#     data = fd.read()
#
#
#
# try:
#     sql = f'insert into images values (1, "test.jpg", %s);'
#
#     # 用execute自动传参的方法将二进制内容传入语句
#     cur.execute(sql,[data])
#     db.commit()
# except Exception as e:
#     db.rollback()
#     print(e)



# 获取文件
sql = 'select * from images where id = 1;'

cur.execute(sql)
image = cur.fetchone()

with open("./images/" + image[1],'wb') as f:
    f.write(image[2])


cur.close()
db.close()