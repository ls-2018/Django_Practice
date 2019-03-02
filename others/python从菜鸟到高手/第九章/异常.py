"""
Exception               所有异常的基类
AttributeError          属性引用或赋值失败
OSError                 当前系统无法执行任务
IndexError
KeyError                在使用映射中不存在的键值时
NameError               找不到变量
SyntaxError             语法错误
TypeError
ValueError
ZeroDivisionError       除除法或者取模操作的第二个参数值为0时抛出的异常
"""


try:
    print(1)
except Exception:
    pass
else:
    pass
    # 正常执行完后执行
finally:
    pass
    # 不管有没有正常执行完毕，都执行


