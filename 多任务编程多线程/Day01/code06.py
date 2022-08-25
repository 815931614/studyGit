from multiprocessing import Pipe,Pool,Process
import os,time




# 创建管道
fd1,fd2 = Pipe(duplex=False)


def fun(name):
    time.sleep(3)

    # 向管道写入内容
    fd2.send({name:os.getpid()})


jobs = []
for i in range(5):
    p = Process(target=fun,args=(i,))
    jobs.append(p)
    p.start()

for i in range(5):
    # 读取管道, recv是一个阻塞函数
    print(fd1.recv())

for i in jobs:
    i.join()
