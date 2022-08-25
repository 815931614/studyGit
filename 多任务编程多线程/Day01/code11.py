from multiprocessing import Semaphore,Process

from time import sleep

import os


# 创建信号量
# 服务程序最多允许3个进程同时执行事件
sem = Semaphore(3)

def work():
    print(f'{os.getpid()}')

    sem.acquire()
    print("...")
    sleep(3)
    sem.release()

jobs = []

for i in range(10):
    p = Process(target=work)
    jobs.append(p)
    p.start()


for j in jobs:
    j.join()


sem.get
