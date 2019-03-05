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











import json
class Product:
    def __init__(self, name,price,count):
        self.name = name
        self.price = price
        self.count = count
def product2Dict(obj):
    return {
        'name': obj.name,
        'price': obj.price,
        'count': obj.count
    }
product = Product('特斯拉',1000000,20)
jsonStr = json.dumps(product, default=product2Dict,ensure_ascii=False)
print(jsonStr)
