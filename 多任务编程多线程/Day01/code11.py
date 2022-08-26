'''
Author: 815931614 815931614@qq.com
Date: 2022-08-25 02:04:14
LastEditors: 815931614 815931614@qq.com
LastEditTime: 2022-08-25 04:27:34
FilePath: /笔记/多任务编程多线程/Day01/code11.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
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




