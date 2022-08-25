from multiprocessing import Process
from time import sleep,ctime

def tm():
    for i in range(3):
        sleep(2)
        print(ctime())

p = Process(target=tm)
p.daemon = True
p.start()
print(p.name)
print(p.pid)
print(p.is_alive())
