def f1():
    for i in range(3):
        yield  i

    print('生成器结束')

g = f1()
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())

