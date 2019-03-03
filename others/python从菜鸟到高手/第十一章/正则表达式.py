import re

# 从头开始，只匹配一次
m = re.match('bird', 'bird')  # 第二个字符是待匹配的字符串
m = re.match('bird|car|truck', 'truck')  # 第二个字符是待匹配的字符串

# 这里要特别注意，如果匹配不到group\groups会抛异常AttributeError
if m is not None:
    print(m.span())  # 所属位置，起始、结束
    print(m.group())

# 匹配一次,
m = re.search('abc', '123abcabcxabc')
# 注意要注意,group span 是SRE_Match对象的方法，因此如果匹配不到，会抛异常
print(m.group())
print(m.span())
"""
注意第一个参数，可以使用正则表达式
"""
#

#
#
#
#


# 分组
m = re.match('(\d\d\d)-(\d\d)', '111-22')

print(m.group())  # 111-22    # 匹配的字符串
print(m.group(1))  # 111  # 从一开始，如果匹配到的话
print(m.groups())  # ('111', '22')
print(m.groups(1))  # ('111', '22')

# 查找所有
print(re.findall('a', 'abcdefa'))  # 返回列表
print(re.finditer('a', 'abcdefa'))
# finditer节省内存，返回的是一个迭代器





# 搜索与替换
result = re.sub('old','new','oldbody')
print(result)#newbody
result = re.subn('old','new','oldbody')
print(result)#('newbody', 1)



result = re.sub('([0-9]+)-([a-z]+)',r'\1,,,,\2','111111123123123-asdf') # 使用\N形式引用匹配字符串中的分组
print(result)#newbody

"""
常用正则表达式
Email       [0-9a-zA-Z]+@[0-9a-zA-Z]+\.[a-zA-Z]{2-3}
IP          \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}
Web         https?:/{2}\w.+
"""

