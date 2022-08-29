'''
Author: 815931614 815931614@qq.com
Date: 2022-08-29 00:15:47
LastEditors: 815931614 815931614@qq.com
LastEditTime: 2022-08-29 00:37:37
FilePath: /笔记/正则表达式/day1/code04.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import re

pattern = r'(ab)cd(?P<pig>ef)'

regex = re.compile(pattern)

obj = regex.search('abcdefghi')

# print(obj.pos) # 0 # 目标字符串开头位置
# print(obj.endpos) # 9 # 目标字符串结束位置
# print(obj.re) # re.compile('(ab)cd(?P<pig>ef)') # 正则表达式
# print(obj.string) # abcdefghi  # 
# print(obj.lastgroup) # pig  #  最后一组的名称
# print(obj.lastindex) # 2 #  最后一组的序号

print(obj.span()) # (0, 6)
print(obj.start()) # 0
print(obj.end()) # 6
print(obj.groupdict()) # {'pig': 'ef'}
print(obj.groups()) # ('ab', 'ef')
print(obj.group()) # abcdef
print(obj.group(1)) # ab
print(obj.group(2)) # ef
print(obj.group('pig')) # ef


