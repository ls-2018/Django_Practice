demo = 'this is a bike a'
print(demo.replace('a', 'b'))

table = demo.maketrans('ak', '$b')
print(table)
print(demo.translate(table))
'''
this is b bike b
{97: 36, 107: 98}
this is $ bibe $
'''

table = demo.maketrans('ak', '$b', ' ')  # 替换并删除空格（一个字符）
print(table)
print(demo.translate(table))
'''
{97: 36, 107: 98, 32: None}
thisis$bibe$
'''
