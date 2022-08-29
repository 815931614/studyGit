from threading import Event


e = Event()
e.set()
print(e.wait(3))
e.clear()
print(e.wait(3))