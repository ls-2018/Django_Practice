class Demo:

    # 比较相关
    def __eq__(self, other):
        return self == other

    def __ne__(self, other):
        return self != other

    def __lt__(self, other):
        return self < other

    def __gt__(self, other):
        return self > other

    def __le__(self, other):
        return self <= other

    def __ge__(self, other):
        return self >= other

    # 和数学相关
    def __add__(self, other):  # 对象 +
        return self + other

    def __sub__(self, other):  # 对象 -
        return self - other

    def __mul__(self, other):  # 对象 *
        return self * other

    def __floordiv__(self, other):  # 对象 //
        return self // other

    def __truediv__(self, other):  # 对象 /
        return self / other

    def __mod__(self, other):  # 对象 %
        return self % other

    def __pow__(self, other):  # 对象 **
        return self ** other

    # 其他方法
    def __str__(self):
        return str(self)

    def __repr__(self):
        # 优先级更高
        return repr(self)

    def __len__(self):
        return len(self)
