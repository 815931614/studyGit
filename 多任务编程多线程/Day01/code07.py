from multiprocessing import Queue,Process
from random import randint
from time import sleep
q = Queue(3)

def request():
    for i in range(20):
        q.put((randint(1,100),randint(1,100)))



def handle():
    while True:
        sleep(.5)
        try:
            x, y = q.get(timeout=3)
        except:
            break
        else:
            print(f'{x},{y}')

p1 = Process(target = request)
p2 = Process(target = handle)
p1.start()
p2.start()
p1.join()
p2.join()