'''
 pip3 install gevent
'''
# from socket import gethostbyname # 同步的
# import gevent
# from gevent import socket  # 必须导入,进行初始化
#
# hosts = ['www.baidu.com', 'taobao.com']
# jobs = [gevent.spawn(gevent.socket.gethostbyname, host) for host in hosts]  # 开辟绿色线程
# gevent.joinall(jobs, timeout=5)
# for job in jobs:
#     print(job.value)

'''
绿色线程与普通线程的区别在于: 绿色线程不会阻塞(在遇到阻塞时,会切换到另一个线程)
'''

# demo2

import gevent
from gevent import monkey
monkey.patch_all()
import socket
#
hosts = ['www.baidu.com', 'taobao.com']
jobs = [gevent.spawn(socket.gethostbyname, host) for host in hosts]
gevent.joinall(jobs, timeout=5)
for job in jobs:
    print(job.value)
# 这里使用普通的socket,只要打上补丁,即使是标注库,也能让他们使用绿色线程.(不包括C写的扩展模块)