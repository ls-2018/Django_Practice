import json
demo ='{"name": "zhangsan", "age": 123}'
class Product:
    def __init__(self,d):
        self.__dict__ = d

my1 = json.loads(demo,object_hook=Product)
print(my1)
print(my1.age)
print(my1.name)






def json2Product(d):
    return Product(d)

my1 = json.loads(demo,object_hook=json2Product)
print(my1)
print(my1.age)
print(my1.name)