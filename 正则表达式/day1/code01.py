'''
Author: 815931614 815931614@qq.com
Date: 2022-08-28 00:22:16
LastEditors: 815931614 815931614@qq.com
LastEditTime: 2022-08-28 22:59:45
FilePath: /笔记/正则表达式/day1/code01.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

import re

s = 'Levi:1111,suny:2222'
pattern = r'(\w+):(\d+)'

l = re.findall(pattern,s)
print(l) # [('Levi', '1111'), ('suny', '2222')]


regex = re.compile(pattern)
l = regex.findall(s) 
print(l) # [('Levi', '1111'), ('suny', '2222')]


# pos  截取目标字符串的开始匹配位置
# endpost 截取目标字符串的结束匹配位置
l = regex.findall(s,0,9) 
print(l) # [('Levi', '1111')]


