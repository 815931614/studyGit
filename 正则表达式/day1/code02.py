'''
Author: 815931614 815931614@qq.com
Date: 2022-08-28 22:50:10
LastEditors: 815931614 815931614@qq.com
LastEditTime: 2022-08-28 23:17:38
FilePath: /笔记/正则表达式/day1/code02.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

import re
s = 'a  b  c  d e-f'
l = re.split(r'[^\w]+', s)
print(l) # ['a', 'b', 'c', 'd', 'e', 'f']



s = '2019/10/12'

ns = re.sub(r'/','-',s)
print(ns)  # 2019-10-12

ns = re.subn(r'/','-',s)
print(ns)  # ('2019-10-12', 2)
