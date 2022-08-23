"""
    包

"""

# # 方式1
# import package01.module01
# package01.module01.fun01()
#
# # 方式2
# from package01 import module01
# module01.fun01()

# 方式3
from package01 import *
# 需要在__init__.py 中添加 __all__ = ['module01']
module01.fun01()

# 方式4
from package01.module01 import *
fun01()
import sys
print(sys.path)

