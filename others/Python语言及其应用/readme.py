a = {'a': 3}
print(a.setdefault('a', 2))

from collections import defaultdict

demo = defaultdict(int)
print(demo)

from collections import Counter

demo_2 = Counter([1, 2, 3, 4, 2, 1])
print(demo_2)  # Counter({1: 2, 2: 2, 3: 1, 4: 1})
print(demo_2.most_common(1))  # 降序

'''+ - | &'''

from collections import OrderedDict

demo_3 = OrderedDict([('a', 1), ('b', 2)])
print(demo_3)  # OrderedDict([('a', 1), ('b', 2)])

from collections import deque  # 双端队列













