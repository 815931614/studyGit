import hashlib
import threading

lock = threading.Lock()
lock2 = threading.Lock()
num = -1
def getNum():
    lock2.acquire()
    global num
    num += 1
    if len(str(num)) < 6:
        return '0' * ( 6 - len(str(num))) + str(num)
    else:
        return str(num)
string1 = "973602"
def has_test(c):

    s = hashlib.sha256()
    s.update(c.encode())
    b = s.hexdigest()
    return b
    # parameters_authentication("111", b, 1634884391)
def fileput(text):
    lock.acquire()
    with open('payPassWord.txt','a') as f:
        f.write(text + '\n')
    lock.release()

def fun():
    while 1:
        key = getNum()
        if len(key) > 6:
            return
        lock2.release()
        fileput(key + "---" + has_test(key))
tlist = []
for i in range(20):
    t1 = threading.Thread(target=fun)
    tlist.append(t1)
    t1.start()
import time
while 1:
    time.sleep(30)
    print(num)
