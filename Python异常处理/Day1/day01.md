# 包 package

#### 定义

- 将模块以文件夹的形式进行分组管理。

#### 作用

- 让一些相关的模块组织在一起，使逻辑结构更加清晰

#### 导入

```python
from 包名 import 模块名 [as 模块新名]
from 包名.子包名 import 模块名 [as 模块新名]
from 包名.子包名.模块名 import 成员名 [as 属性新名]
```

# 异常处理

常见异常类型

- 名称异常(NameError):变量未定义
- 类型异常(TypeError): 不同类型数据进行运算
- 索引异常(IndexError)：超出索引范围
- 属性异常(AttributeError): 对象没有对应名称的属性
- 键异常(KeyError): 没有对应名称的键
- 为实现异常(NotImplementedError):尚未实现的方法
- 异常基类Exception

#### 处理

​	语法

```python
try:
	# 可能触发异常的语句
except 错误类型1 [as 变量1]:
    处理语句1
except 错误类型2 [as 变量2]:
    处理语句2
....
else:
    未发生异常的语句
finally:
    无论是否发生异常的语句	
```

#### 抛出异常

​	raise ValueError('异常提示')

#### 自定义异常

```python
# 1、定义
class 类名Error(Exception):
    def __init__(self,参数):
        super().__init__(参数)
        self.数据 = 参数
  
# 2、调用
	try:
        ...
        raise 自定义异常类名(参数)
        ...
    except 定义异常类 as 变量名:
        变量名.数据

# 3、 作用: 封装错误信息

```

