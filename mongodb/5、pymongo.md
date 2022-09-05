#### pymongo

```python
from pydoc import cli
from pymongo import MongoClient

class TestMongo:

    
    def __init__(self):
        client = MongoClient(host=1.json,port=27017)
        
        # 选择数据库和集合
        self.collection = client['test101']['t1']

    def test_insert(self):
        # insert接收字典，返回objectID
        ret = self.collection.insert_one({"name":"test101","age":33})
        print(ret.inserted_id)

    def test_insert_many(self):
        item_list = [{"name":"test1000{}".format(i)} for i in range(10)]
        
        # insert_many接收一个列表，列表中为所有需要插入的字典
        t = self.collection.insert_many(item_list)
        print(t.inserted_ids)
        # t.inserted_ids为所有插入的id
        for i in t.inserted_ids:
            print(i)


    def try_find_one(self):
        # find_one 查找并且返回一个结果，接收一个字典形式的条件
        t = self.collection.find_one({"name":"test101"})
        print(t) # {'_id': ObjectId('630dfaa18b2f6e84f92e238d'), 'name': 'test101', 'age': 33}
    
    def try_find_many(self):
        # find 返回所有满足条件的结果，如果条件为空，则返回数据库的所有
        t = self.collection.find({"name":"test101"})
        print(t)
        for i in t:
            print(i)
        for i in t:  # 此时t中没有内容
            print(i)
        print(list(t))

    def try_update_one(self):
        # update_one更新一条数据
        u = self.collection.update_one({"name":"test101"},{"$set":{"name":"test102"}})
        print(u)

    def try_update_many(self):
        # update_one更新全部数据
        self.collection.update_many({"name":"test10005"},{"$set":{"name":"test102"}})

    def try_delete_one(self):
        # delete_one删除一条数据
        self.collection.delete_one({"name":"test10010"})
    
    def try_delete_one(self):
        self.collection.delete_many({"name":"test10010"})
tm = TestMongo()

# tm.test_insert()
# tm.test_insert_many()
tm.try_delete_one()
```

