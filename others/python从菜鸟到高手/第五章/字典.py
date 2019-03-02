a = ['a', 'b', 'c']
b = [1, 2, 3]
print(dict(zip(a, b)))

print('-')
for value in zip(a, b):
    print(value)
print('-')
print(list(zip(a, b)))

c = {'a': 1}
print(list(c))
print('====')

newDict = {}.fromkeys(['a', 'b', 'c'], 1)

print(newDict)

newDict2 = newDict.fromkeys(['a', 'b', 'c'])

print(newDict2)

test = {}
test['name'] = 'zhangsan'
print(test.setdefault('name', 'suiji'))  # suiji,并不会修改原来的值
print(test)

big_news = {'a': 1, 'b': 2, 'c': 3, 'a': 2}

for k in big_news.keys():
    print(k)
for v in big_news.values():
    print(v)
for i in big_news.items():
    print(i)
# a
# b
# c
# 2
# 2
# 3
# ('a', 2)
# ('b', 2)
# ('c', 3)