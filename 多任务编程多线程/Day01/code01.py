import multiprocessing as mp

from time import sleep


num = 0

def fun():
   
    print('1')
    num = 222
    sleep(3)
    print(2)

p = mp.Process(target=fun)
p.start()
p.join()
print(num)