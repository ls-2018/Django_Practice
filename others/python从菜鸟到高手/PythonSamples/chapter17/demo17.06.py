'''
--------《Python从菜鸟到高手》源代码------------

欧瑞科技版权所有
作者：李宁
如有任何技术问题，请加QQ技术讨论群：264268059    
或关注“极客起源”订阅号或“欧瑞科技”服务号或扫码关注订阅号和服务号，二维码在源代码根目录
如果QQ群已满，请访问https://geekori.com，在右侧查看最新的QQ群，同时可以扫码关注公众号

“欧瑞学院”是欧瑞科技旗下在线IT教育学院，包含大量IT前沿视频课程，
请访问http://geekori.com/edu或关注前面提到的订阅号和服务号，进入移动版的欧瑞学院

“极客题库”是欧瑞科技旗下在线题库，请扫描源代码根目录中的小程序码安装“极客题库”小程序

关于更多信息，请访问下面的页面
https://geekori.com/help/videocourse/readme.md.html



'''
import threading
from time import sleep, ctime

class MyThread(object):
    def __init__(self, func, args):
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)
def fun(index, sec):
    print('开始执行', index, ' 时间:', ctime())
    sleep(sec)
    print('结束执行', index, '时间:', ctime())
def main():
    print('执行开始时间:', ctime())
    thread1 = threading.Thread(target = MyThread(fun,(10, 4)))
    thread1.start()
    thread2 = threading.Thread(target = MyThread(fun,(20, 2)))
    thread2.start()
    thread3 = threading.Thread(target = MyThread(fun,(30, 1)))
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()
    print('所有的线程函数已经执行完毕:', ctime())
if __name__ == '__main__':
    main()
