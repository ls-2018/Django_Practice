import unittest
from others.python从菜鸟到高手.测试 import xxxxxxxxxxxxx



class TestCase(unittest.TestCase):

    def testAdd(self):
        for x in range(-20, 20):
            for y in range(-10, 10):
                result = xxxxxxxxxxxxx.xxx(x, y)
                self.assertEqual(result, x + y, '%d + %d失败' % (x, y))


if __name__ == '__main__':
    unittest.main()
# 此文件名不能包含中文