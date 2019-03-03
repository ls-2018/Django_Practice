# 对于自定义类


'''
列表是一下子将所有的数据都装在到内存中,而且是一整块空间.当数据比较小时,比较容易；但是当数据量很大时，会非常消耗内存资源。
而迭代不同,是读取多少元素,就将多少元素装载到内存当中,不读取就不装载。
'''


class Student():
    def __init__(self):
        self.n = 1

    def __iter__(self):
        return self  # 返回一个迭代器

    def __next__(self):
        result = '*' * (2 * self.n - 1)
        self.n += 1

        """
        因此：之前的斐波那契算法，也可以在这里实现
        停止迭代：抛出StopIteration异常
        """

        return result


s = Student()
for et in s:
    if len(et) < 20:
        print(et)
