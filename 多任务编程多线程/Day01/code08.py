from multiprocessing import Process, Value
import time
import random



# 创建共享内存
money = Value('i',5000)

# 操作共享内存
def man():
    for i in range(30):
        time.sleep(.2)
        money.value += random.randint(1,1000)



def firl():
    for i in range(30):
        time.sleep(.15)
        money.value -= random.randint(100,800)


m = Process(target=man)
f = Process(target=firl)

m.start()
f.start()

m.join()
f.join()

# 获取共享内存值
print(money.value)