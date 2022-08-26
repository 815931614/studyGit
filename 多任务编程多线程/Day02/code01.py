'''
Author: 815931614 815931614@qq.com
Date: 2022-08-26 00:42:13
LastEditors: 815931614 815931614@qq.com
LastEditTime: 2022-08-26 01:18:24
FilePath: /笔记/多任务编程多线程/code01.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE 
'''


from re import T
import threading
from time import sleep

# 线程函数
def fun01():
    for i in range(5):
        print(i)
        sleep(2)


t = threading.Thread(target=fun01)
t.start()
t.join()


