'''
Author: 815931614 815931614@qq.com
Date: 2022-08-26 04:07:17
LastEditors: 815931614 815931614@qq.com
LastEditTime: 2022-08-26 04:19:20
FilePath: /笔记/多任务编程多线程/Day02/code05.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AEd

'''
from threading import Thread 
from time import sleep,ctime


class MyThread(Thread):
    def __init__(self,target,args,kwargs,name='Tedu'):
        self.target = target
        self.args = args
        self.kwargs = kwargs
        super().__init__()

    def run(self):
        self.target(*self.args,**self.kwargs)




def player(sec,song):
    print(sec,song)
    for i in range(2):
        print(f"Playing{song}:{ctime()}")
        sleep(sec)


t = MyThread(target=player,args=(3,),kwargs={
    'song' : ''
},name='t1')
t.start()
t.join()