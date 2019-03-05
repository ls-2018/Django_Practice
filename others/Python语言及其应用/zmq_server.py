# '''
# pip3 install pyzmq
# https://github.com/imatix/zguide/tree/master/examples/Python
#
# REQ     同步请求
# REP     异步请求
# DEALER  异步请求
# ROUTER  异步响应
# PUB     发布
# SUB     订阅
# PUSH    扇出
# PULL    扇入
#
# '''
import zmq
import simplejson as jsonmod

host = '127.0.0.1'
port = 6789
context = zmq.Context()
server = context.socket(zmq.REP)
server.bind('tcp://%s:%s' % (host, port))
while True:
    request_bytes = server.recv()
    print(request_bytes)
    # print(request_bytes.decode('utf8',errors='ignore'))
    # print(jsonmod.JSONDecoder().raw_decode(s=request_bytes.decode('utf8'), )[0])
# demo = b'"\\u4e2d"'
# import simplejson as jsonmod
# print(demo.decode(encoding='utf-8'))
