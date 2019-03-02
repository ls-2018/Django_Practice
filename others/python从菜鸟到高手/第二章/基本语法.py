# format
x = 123456.789
print(format(x, '_>20.5f'))
print(format(x, '_^20.5f'))
print(format(x, '0.2E'))
print(format(x, '0.2e'))

# 数值
print(bin(1000))
print(oct(1000))
print(bin(1000))
print(hex(1000))

# python解释器無法判斷字符串中間的引號是單引號還是正常的字符串
print(repr('hello \n world'))  # repr按原始字符串輸出， 會用一對單引號括起來
# 转义的三种
"""
repr
转义符号\
在字符前面加r
"""

print("hello\n"
      "world" ,end='\n',sep=',')  # 输出一行



# 为空的值
# False 0 [] {}  '' 




from string import Template
template = Template('$s $s $s')
print(template.substitute(s = 'hello'))
print(__name__)



