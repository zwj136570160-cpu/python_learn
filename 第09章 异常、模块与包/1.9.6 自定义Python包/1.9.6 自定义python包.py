"""
- 目标
1. 了解什么是python包
2. 掌握如何自定义包
"""

"""
基于python模块，我们可以在编写代码的时候，导入许多外部代码来丰富功能

但是如何python的模块太多了，就可能造成一定的混乱，那么如何管理呢？
"""

"""
- 什么是python包
从物理上看，包就是一个文件夹，在该文件夹下包含了一个__init__.py文件，该文件夹可用于包含多个模块文件
从逻辑上看，包的本质依然是模块

包的作用：
    当我们的模块文件越来越多时，包可以帮助我们管理这些模块，包的作用就是包含多个模块，但包的本质依然是模块
"""

"""
- 快速入门
步骤如下：
① 新建包my_package
② 新建包内模块：my_module1和my_module2
③ 模块内代码如下：
my_package
    __init__.py
    my_module1.py
    my_module2.py
my_module1模块中
print(1)
def info_print():
    print("info_print")
    
my_module2模块中
    print(2）
def info_print2():
    print("info_print2")

prcharm中的基本步骤：
new → python package → 输入包名 → 新建功能模块（有联系的模块）
"""

"""
- 导入包
方式一：
import 包名.模块名
包名.模块名.目标
"""
# 创建一个包
# 导入自定义的包中模块，并使用

import my_package.my_module1
import my_package.my_module2
my_package.my_module1.info_print()
my_package.my_module2.info_print2()

from my_package import my_module1
from my_package import my_module2
my_module1.info_print()
my_module2.info_print2()

from my_package.my_module1 import info_print
from my_package.my_module2 import info_print2
info_print()
info_print2()

"""
- 导入包
方式2：
注意：必须在__init__.py 文件中添加__all__ = []，控制允许导入的模块列表
from 包名 import *
模块名.目标
"""
# 通过__all__变量，控制import *
from my_package import *
my_module1.info_print()
# my_module2.info_print2() #  由于在包my_package中__init__.py文件中使用了__all__变量去控制了，只准使用my_module 所以my_module2报错了.

"""
- 总结
1. 什么是python的包
包就是文件夹，里面可以存放需要python的模块（代码文件），通过包，在逻辑上将一批模块归为一类，方便使用
2. __init__.py文件的作用？
创建包会默认自动创建的文件，通过这个文件来表示一个文件夹是python的包，而非普通的文件夹
3. __all__变量的作用？
同模块中学习到的是一个作用，控制import *能够导入的内容
"""


