from multiprocessing import Pool

from time import sleep,ctime


def worker(msg):
    sleep(2)
    print(msg)
    return ctime()


# 创建进程池
pool = Pool(16)

# 向进程池添加事件
for i in range(25):
    msg = f"事件:{i}"
    r = pool.apply_async(func=worker,args=(msg,))

# 关闭进程池
pool.close()


# 回收进程池
pool.join()

print(r.get())