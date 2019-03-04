from threading import BoundedSemaphore
semaphore = BoundedSemaphore(2)

semaphore._value    # 查看剩余资源值
semaphore.acquire()
semaphore.acquire()
semaphore.acquire() # 资源值为0后会阻塞
semaphore.release()
semaphore.release()
semaphore.release() # 抛异常




# 队列
from queue import Queue
q = Queue(32)
q.get()
q.put('xx')
## 都会阻塞