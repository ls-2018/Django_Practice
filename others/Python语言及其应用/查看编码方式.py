
import unicodedata
demo='中'
name = unicodedata.name(demo)
print(name)
value = unicodedata.lookup(name)
print(value)
'''
CJK UNIFIED IDEOGRAPH-4E2D
中
'''
# 编码  encode
# 解码  decode