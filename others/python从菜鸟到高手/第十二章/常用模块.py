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
# os.system('ls')  # 执行命令

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

# 堆heap,最小堆、最大堆(其实就是列表,通过算法改变顺序)
# 使用优先队列能以任意顺序增加元素值，并能快速找到最大、小的值
# Python中并没有提供独立的类型,只提供了一个包含一些堆操作函数的模块
import heapq

# heapq.heappush(heap,value)# 将value加入堆
# heapq.heapify(heap)# 将列表转换为堆
# heapq.heapreplace(heap,value)# 将最小的值弹出,并将value入堆
# heapq.nsmallest(n,iter)# 返回可迭代对象的前n个最小值,以列表形式返回
# heapq.nlargest(n,iter)# 返回可迭代对象的前n个最大值,以列表形式返回
# heapq.merge(*iter,key)# 合并多个有序的迭代对象,如果指定key,则以么米格元素的排序规则会利用key制定的函数


# 双端队列deque
from collections import deque

q = deque(range(10))
print(q)
q.append(1)
q.appendleft(2)
print(q)
print(q.pop())
print(q.popleft())

# time
import time

localtime = time.localtime(time.time())
print(
    localtime)  # time.struct_time(tm_year=2019, tm_mon=3, tm_mday=4, tm_hour=7, tm_min=50, tm_sec=24, tm_wday=0, tm_yday=63, tm_isdst=0)
print(localtime.tm_yday)  # 63
print(time.asctime(localtime))  # Mon Mar  4 07:50:24 2019

print(time.strftime("%Y-%d-%d"), time.localtime(time.time()))  # 2019-04-04,后边可以不写,默认当前

# print(time.strftime("今天是%A",))  # 这里有一个问题,这样写在win回报编码错误


# 解决办法
import locale

locale.setlocale(locale.LC_ALL, 'zh_CN.UTF-8')
print(time.strftime("今天是%A", ))

#  datetime
import datetime

d1 = datetime.datetime(2017, 1, 2)
d2 = datetime.datetime(2018, 2, 2) + datetime.timedelta(hours=10)
# print(d2.timestamp()) # 时间戳
print((d2 - d1).days)
print(d1.day)
