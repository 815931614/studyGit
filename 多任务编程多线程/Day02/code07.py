'''
Author: 815931614 815931614@qq.com
Date: 2022-08-27 03:49:18
LastEditors: 815931614 815931614@qq.com
LastEditTime: 2022-08-27 04:04:28
FilePath: /笔记/多任务编程多线程/Day02/code07.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import asyncio
from asyncio import tasks
import time

now = lambda : time.time()


async def do_work(x):
    print('waiting:' , x)
    await asyncio.sleep(x)
    return "Done after %s s"%x

start = now()

cor1 = do_work(1)
cor2 = do_work(2)
cor3 = do_work(3)

# 将协程对象生成一个可轮寻操作的对象列表
tasks = [
    asyncio.ensure_future(cor1),
    asyncio.ensure_future(cor2),
    asyncio.ensure_future(cor3),
]

# 得到轮寻对象调用run启动协程执行
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

















