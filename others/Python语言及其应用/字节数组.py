
'''
字节不可变           元组
字节数组可变          列表
'''

blist = [1,2,3,4,5]
b_1 = bytes(blist)
b_2 = bytearray(blist)
print(b_1)
print(b_2)
r'''
b'\x01\x02\x03\x04\x05'
bytearray(b'\x01\x02\x03\x04\x05')
'''
# b_1[0]=12 报错
b_2[0]=12
print(blist)
print(b_2)
r'''[1, 2, 3, 4, 5]
bytearray(b'\x0c\x02\x03\x04\x05')'''
