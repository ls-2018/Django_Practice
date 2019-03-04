import unittest
from .doc import add as add
# def add(x, y):
#     return x + y


class TestCase(unittest.TestCase):

    def testAdd(self):
        for x in range(-20, 20):
            for y in range(-10, 10):
                result = add(x, y)
                self.assertEqual(result, x + y, '%d + %d失败' % (x, y))


if __name__ == '__main__':
    unittest.main()
