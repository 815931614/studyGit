'''
Author: 815931614 815931614@qq.com
Date: 2022-08-28 23:19:55
LastEditors: 815931614 815931614@qq.com
LastEditTime: 2022-08-28 23:45:11
FilePath: /笔记/正则表达式/code03.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

import re

s = '2020,12'
pattern = r'\d+'


# 返回包含匹配结果的迭代器
it = re.finditer(pattern, s)
for i in it:

    print(i.group())
# <re.Match object; span=(0, 4), match='2020'>
# <re.Match object; span=(5, 7), match='12'>



m = re.fullmatch(r'\w+', "hello-1973")
print(m)  # None

m = re.fullmatch(r'\w+', "hello_1973")
print(m)  # <re.Match object; span=(0, 10), match='hello_1973'>
print(m.group())  # hello_1973


m = re.match(r'[A-Z]\w*',"hello World")
print(m) # None

m = re.match(r'[A-Z]\w*',"Hello World")
print(m) # <re.Match object; span=(0, 5), match='Hello'>



m = re.search(r'\s+',"a ,\n")
print(m)  # <re.Match object; span=(1, 2), match=' '>





