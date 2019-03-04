# 命名元祖
from collections import namedtuple

Duck = namedtuple('duck', 'bill tail')
duck = Duck('wide orange', 'long')
print(duck)  # duck(bill='wide orange', tail='long')
print(duck.bill)
print(duck.tail)

duck_3 = duck._replace(bill='newbill')
print(duck)  # duck(bill='wide orange', tail='long')
print(duck_3)  # duck(bill='newbill', tail='long')

