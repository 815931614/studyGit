from multiprocessing import Process
from time import sleep

def worker(a,b,aa):
    print(a, b,aa)

p = Process(target=worker, args=(1,),kwargs={
    'b' : 2,
    'aa' : 1
})
p.start()
p.join()
