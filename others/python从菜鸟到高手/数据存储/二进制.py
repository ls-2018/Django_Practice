'''
Python没有二进制类型,但是可以用string存储二进制类型数据,因为string是以字节为单位的.
pack(格式化字符串,数据)





'''

import struct

a = 'hello'
b = 2
d = 1.2
bytes = struct.pack('5sif',a.encode('utf8'),b,d)
print(bytes)

bytes = struct.unpack('5sif',bytes)
print(bytes)


'''
格式字符        C语言类型               Python类型                    字节
c               char            string of length 1                  1
b            signed char                integer                     1
B            usigned char               integer                     1
?               _Bool                   bool                        1
h               short                   integer                     2
H            usigned short              integer                     2
i                int                    integer                     4
I               usigned int         integer or long                 4
l                long                   integer                     4
L             usigned long               long                       4   
q                long long               long                       8
Q           usigned long long            long                       8    
f                float                   float                      4      
d               double                  double                      8    
s               char[]                   string                     1  
p               char[]                   string                     1
P               void*                       long                与OS有关










'''