'''
Author: 815931614 815931614@qq.com
Date: 2022-08-26 03:53:44
LastEditors: 815931614 815931614@qq.com
LastEditTime: 2022-08-26 04:05:05
FilePath: /笔记/多任务编程多线程/Day02/code04.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AEhre

'''
from threading import Thread


class MyThread(Thread):
    def __init__(self):
        super(MyThread,self).__init__()

    def run(self) -> None:
        self.fun1()
        self.fun2()



    def fun1(self):
        print('步骤1')

    def fun2(self):
        print('步骤2')


t = MyThread()
t.start()
t.join()