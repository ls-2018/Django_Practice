import re

# 从头开始，只匹配一次
m = re.match('bird', 'bird')  # 第二个字符是待匹配的字符串

# 这里要特别注意，如果匹配不到group\groups会抛异常AttributeError
if m is not None:
    print(m.span())  # 所属位置，起始、结束
    print(m.group())

# 匹配一次,
m = re.search('abc', '123abcabcxabc')
# 注意要注意,group span 是SRE_Match对象的方法，因此如果匹配不到，会抛异常
print(m.group())
print(m.span())
