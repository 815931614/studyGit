'''
Author: 815931614 815931614@qq.com
Date: 2022-08-29 00:50:20
LastEditors: 815931614 815931614@qq.com
LastEditTime: 2022-08-29 01:04:23
FilePath: /笔记/正则表达式/day1/code05_flags.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AEs 

'''
import re

s = """Hello world
123,你好
"""

regex = re.compile(r'\w+',re.A)
l = regex.findall(s)
print(l) # ['Hello', 'world', '123']


regex = re.compile(r'[a-z]+',re.I)
l = regex.findall(s)
print(l) # ['Hello', 'world']

regex = re.compile(r'.+',re.S)
l = regex.findall(s)
print(l) # ['Hello world\n123,你好\n']


regex = re.compile(r'^123',re.M)
l = regex.findall(s)
print(l) # ['123']

s = """Hello world  # 注释
123,你好             # 注释
"""
regex = re.compile(r'^Hello',re.X)
l = regex.findall(s)
print(l) # ['Hello']