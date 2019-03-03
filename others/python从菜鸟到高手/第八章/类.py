class Student:
    def __run(self):
        print("run")

    def play(self):
        pass



s = Student()
print(Student.__dict__)
print(s.__class__.__dict__)
print(s.__dict__)
# super()
s._Student__run()

# 获去类中所有的方法
import inspect

methods = inspect.getmembers(s, predicate=inspect.ismethod)
for i in methods:
    print(i)

from inspect import isfunction, ismethod

print(isfunction(s.play))
print(ismethod(s.play))
from types import FunctionType, MethodType

print(isinstance(s.play, FunctionType))
print(isinstance(s.play, MethodType))
