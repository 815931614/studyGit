

# Python re 模块使用

```
regex = re.compile(pattern,flags = 0)
功能：   生产正则表达式对象
参数:       pattern 正则表达式
		         flags 功能标志位，扩展正则表达式的匹配
返回值：正则表达式对象
```

 

```
regex.findall(string,pos,endpos)
功能：根据正则表达式匹配目标字符串内容
参数：string目标字符串
			pos  截取目标字符串的开始匹配位置
			endpost 截取目标字符串的结束匹配位置
返回值：匹配到的内容列表，如果正则表达式有子组则只能获得到子组对应的内容
```



```
re.findall(pattern,string,flags = 0)
功能：根据正则表达式匹配目标字符串内容
参数：pattern 正则表达式
			string目标字符串
			flags  功能标志位，扩展正则表达式的匹配
返回值：匹配到的内容列表，如果正则表达式有子组则只能获得到子组对应的内容
```



```
re.split(pattern,string,flags=0)
功能：使用正则表达式匹配内容，切割目标字符串
参数：pattern  正则表达式
			string  目标字符串
			flags  功能标志位，扩展正则表达式的匹配
返回值:切割后的内容列表
```



```
re.sub(pattern,replace,string,max,flags=0)
功能：使用一个字符串替换正则表达式匹配到的内容
参数：pattern 正则表达式
			replace 替换的字符串
			string 目标字符串
			max   最多替换几处，默认全部替换
			flags  功能标志位，扩展正则表达式的匹配
返回值：替换后的字符串

```



```
re.subn(pattern,replace,string,max,flags=0)
功能：使用一个字符串替换正则表达式匹配到的内容
参数：pattern 正则表达式
			replace 替换的字符串
			string 目标字符串
			max   最多替换几处，默认全部替换
			flags  功能标志位，扩展正则表达式的匹配
返回值：替换后的字符串和替换了几处


s = '2019/10/12'

ns = re.sub(r'/','-',s)
print(ns)  # 2019-10-12

ns = re.subn(r'/','-',s)
print(ns)  # ('2019-10-12', 2)

```

```
re.finditer(pattern,string,flags=0)
功能:根据正则表达式匹配目标字符串内容
参数：pattern 正则表达式
			string 目标字符串
			flags   功能标志位，扩展正则表达式的匹配
返回值：匹配结果的迭代器(迭代器中存放着match对象)

```



```
re.fullmatch(pattern,string,flags=0)
功能:完全匹配某个目标字符串
参数：pattern 正则
			string  目标字符串
返回值：匹配内容match  object


m = re.fullmatch(r'\w+', "hello-1973")
print(m)  # None

m = re.fullmatch(r'\w+', "hello_1973")
print(m)  # <re.Match object; span=(0, 10), match='hello_1973'>
print(m.group())  # hello_1973
```



```
re.match(pattern,string,flags=0)
功能： 匹配某个目标字符串开始位置
参数：pattern 正则
			string 目标字符串
返回值：匹配内容match  object

例如：
    m = re.match(r'[A-Z]\w*',"hello World")
    print(m) # None

    m = re.match(r'[A-Z]\w*',"Hello World")
    print(m) # <re.Match object; span=(0, 5), match='Hello'>
```



```
re.search(pattern,string,flags=0)
功能： 匹配目标字符串第一个符合内容
参数：pattern 正则
			string 目标字符串
返回值：匹配内容match  object

m = re.search(r'\s+',"a ,\n")
print(m)  # <re.Match object; span=(1, 2), match=' '>
```



compile对象属性

1. flags: falags 值
2. pattern : 正则表达式
3. groups：子组数量
4. groupindex: 捕获组名与组序号的字典





#### match对象的属性方法

1. 属性变量

   - pos 匹配的目标字符串开始位置

   - endpos  匹配的目标字符串结束位置

   - re 正则表达式

   - string 目标字符串

   - lastgroup 最后一组的名称

   - lastindex最后一组的序号

     ```
     import re
     
     pattern = r'(ab)cd(?P<pig>ef)'
     
     regex = re.compile(pattern)
     
     obj = regex.search('abcdefghi')
     
     print(obj.pos) # 0 # 目标字符串开头位置
     print(obj.endpos) # 9 # 目标字符串结束位置
     print(obj.re) # re.compile('(ab)cd(?P<pig>ef)') # 正则表达式
     print(obj.string) # abcdefghi  # 
     print(obj.lastgroup) # pig  #  最后一组的名称
     print(obj.lastindex) # 2 #  最后一组的序号
     ```

     

2. 属性方法

   - span() 获取匹配内容的起止位置

   - start() 获取匹配内容的开始位置

   - end() 获取匹配内容的结束位置

   - groupdict() 获取捕获组字典，组名为键，对应内容为值

   - groups() 获取子组对应内容

   - group(n = 0)

     ```
     功能：获取match对象匹配内容
     参数：默认为0表示获取整个match对象内容，如果是序列号或者组名则表示获取对应子组内容
     返回值：匹配字符串
     ```

   ```python
   pattern = r'(ab)cd(?P<pig>ef)'
   regex = re.compile(pattern)
   obj = regex.search('abcdefghi')
   
   print(obj.span()) # (0, 6)
   print(obj.start()) # 0
   print(obj.end()) # 6
   print(obj.groupdict()) # {'pig': 'ef'}
   print(obj.groups()) # ('ab', 'ef')
   print(obj.group()) # abcdef
   print(obj.group(1)) # ab
   print(obj.group(2)) # ef
   print(obj.group('pig')) # ef
   ```

### flags参数扩展

1. 使用函数：re模块调用的匹配函数。如：

   re.compile,re.findall,re.search....

2. 作用: 扩展丰富正则表达式的匹配功能

3. 常用flag

   A == ASCII 元字符只能匹配ascii码

   I == IGNORECASE 匹配忽略字母大小写

   S == DOTALL 使.可以匹配换行

   M == MULTILINE 使^$可以匹配每一行的开头结尾位置

   X == VERBOSE 为正则添加注释

4. 使用多个flag

   方法：使用按位或连接

   ​			flags = re.I|re.A

```python
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
```

