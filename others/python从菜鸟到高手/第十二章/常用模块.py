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