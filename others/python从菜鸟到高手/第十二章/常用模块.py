# sys

import sys

sys.path.append('')
print(sys.modules['sys'])  # 字典
print(sys.platform)  # linux
print(sys.argv[0])  # /media/ace/1256389B56388191/资料/Django企业开发实战/others/python从菜鸟到高手/第十二章/常用模块.py

# subprocess
import subprocess

output = subprocess.getstatusoutput('ls')
print(output)  # (0, '常用模块.py')

# os
import os

print(os.getcwd())  # 当前目录
print(os.listdir(os.getcwd()))  # 同一级的文件、文件夹
os.chdir('../')  # 改变当前路径
print(os.getcwd())
# os.mkdir()创建目录
# os.makedirs() 可以递归创建目录
# os.removedirs()可以递归删除目录，前提是目录下没有文件
# os.remove()   删除文件
# os.rename()   改名字
# os.renames()   可以联目录一起改

# os.path.exists('')
#
# os.symlink('a','b')     # a---->b       软链接
# os.link('a','b')        #               硬链接
# 如果链接文件存在，会抛出异常
print(os.sep)  # 路径分割符     w \   l m  /
print(os.pathsep)  # 环境变量中的分割符
print(os.name)  # posix
print(os.environ)  # 环境变量
# print(os.getenv(key))# 获取操作系统的变量
# print(os.putenv(key,value))   # 只设置当前进程中的值
os.system('ls')  # 执行命令

# 集合set
set(range(10))
a = set([1, 2])
b = set([2, 3])
print(a.union(b))  # 返回并集
print(a | b)  # 返回并集
print(a)
print(b)
print(a.intersection(b))  # 返回交集
print(a & b)  # 返回交集
print(a)
print(b)
print(a.issubset(b))
print(a.issuperset(b))
print(a == b)
print(a.difference(b))  # 返回a独有的              -
print(a.symmetric_difference(b))  # 返回ab独有的集合             ^

# 堆heap

# 双端队列deque

