'''
Author: 815931614 815931614@qq.com
Date: 2022-08-26 01:18:08
LastEditors: 815931614 815931614@qq.com
LastEditTime: 2022-08-26 01:19:38
FilePath: /笔记/多任务编程多线程/Day02/code02.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AEm ti

'''
from threading import Thread
from time import sleep


# 含有参数的线程函数
def fun(sec,name):
    print("线程函数传参")
    sleep(sec)


t = Thread(target=fun,args=(1,'2'))