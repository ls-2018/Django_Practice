# sys

import sys
sys.path.append('')
print(sys.modules['sys'])# 字典
print(sys.platform) # linux
print(sys.argv[0])# /media/ace/1256389B56388191/资料/Django企业开发实战/others/python从菜鸟到高手/第十二章/常用模块.py


# subprocess
import subprocess
output = subprocess.getstatusoutput('ls')
print(output)   # (0, '常用模块.py')

# os
import os
print(os.getcwd())  # 当前目录
print(os.listdir(os.getcwd()))# 同一级的文件、文件夹
os.chdir('../') #  改变当前路径
print(os.getcwd())
# os.mkdir()创建目录
# os.makedirs() 可以递归创建目录
# os.removedirs()可以递归删除目录，前提是目录下没有文件
# os.remove()   删除文件
# os.rename()   改名字
# os.renames()   可以联目录一起改

