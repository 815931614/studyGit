'''
Author: 815931614 815931614@qq.com
Date: 2022-08-26 01:22:44
LastEditors: 815931614 815931614@qq.com
LastEditTime: 2022-08-26 01:45:56
FilePath: /笔记/多任务编程多线程/Day02/code03.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AEing

'''
from threading import Thread
from time import sleep

def fun():
    sleep(3)
    print("线程属性测试")


t = Thread(target=fun,name="Tarena")

# 线程名称
t.setName("Tedu")
print(t.getName())

# 线程生命周期
print(t.is_alive())














