# Thread synchronization
# 线程同步

# Author: zhangzhp
# Date: 2017-8-21 17:29:48

# -------------------- 调用包 -------------------- #
import threading
import time

# -------------------- 定义类 -------------------- #

class myThread(threading.Thread):

    # ---------- 定义函数 ---------- #

    # 重写__init__函数
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    # 重写run函数
    def run(self):
        print("开启线程: " + self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name,self.counter,3)
        # 释放锁，开启下一个线程
        threadLock.release()

def print_time(threadName,delay,counter):
    while counter:
        time.sleep(delay)
        print("%s: %s"%(threadName,time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()
threads = []

# 创建线程
thread1 = myThread(1,"Thread-1",1)
thread2 = myThread(1,"Thread-2",2)

# 开始新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print("\n退出主线程")

