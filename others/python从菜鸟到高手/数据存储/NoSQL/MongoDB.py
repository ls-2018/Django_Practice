'''
pip3 install pymongo
'''
from pymongo import *

Client = MongoClient()  # 连接数据库
db = Client.data    # 打开或创建名为data的collection,   collection 相当于关系型数据库中的数据库
# db = Client['data']


# collection = db['test_collection']# 打开或创建一个一个名为test_collection的文档,类似于关系型数据库里的表

# 插入数据
person1 = {"name": "Bill", "age": 55, "address": "地球", "salary": 1234.0}
persons = db.persons

persons.delete_many({'age': {'$gt': 0}})    # 删除文档中的数据, $gt引用文档里的数据.

personId1 = persons.insert_one(person1).inserted_id
print(personId1)
'''
和上面的不能同时使用
personList = [person1,]
result = persons.insert_many(personList)
print(result.inserted_ids)
'''

print(persons.find_one())# 文档
print(persons.find_one()['name'])
# 搜索所有数据
for person in persons.find():
    print(person)
print('--------------')
persons.update_one({'age': {'$lt': 50}}, {'$set': {'name': '超人'}})  # update_many更新所有满足条件的文档
# persons.delete_one({'age':{'$gt':0}})  # 只删除满足条件的第1个文档
# 搜索指定数据
for person in persons.find({'age': {'$lt': 50}}):
    print(person)

print('--------------')
# 更新

for person in persons.find({'age': {'$gt': 50}}):
    print(person)
print('总数', '=', persons.count())
