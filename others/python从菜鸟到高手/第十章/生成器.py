# 生成值
def xx():
    numlist = [1, 2, 3, 3, 4, 3, 5, ]
    for i in numlist:
        m = yield i
        print(m, '---')


f = xx()
for num in f:
    f.close()
    # f.throw(StopIteration)
    print(num)

# 当一个对象不是迭代器、生成器时   for 循环会抛出TypeError错误
