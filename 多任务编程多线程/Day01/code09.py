from multiprocessing import Process,Value,Array



# 创建共享内存
# 共享内存开辟5个整型列表空间，数组中元素的默认值是0
# shm = Array('i', 5)

# 共享内存初始化数据
# shm = Array('i',[1,2,3])

# 字节串
shm = Array('c',b'hello')
def fun():
    # 共享内存对象可迭代
    for i in shm:

        print(i)

    # 修改共享内存
    shm[1] = b"2"

p  =  Process(target=fun)
p.start()
p.join()

# 通过value属性访问字节串（value只可以打印字节串）
print(shm.value)