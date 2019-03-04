'''
    测试add函数
    >>>  add(1,2)
    3

'''


def add(x, y):
    return x + y


if __name__ == '__main__':
    import doctest, doc

    doctest.testmod(doc)

    # python3 ./doc.py -v
