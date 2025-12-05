"""
- 目标
1. 了解如何自定义模块并使用
2. 了解_main_变量的作用
"""

"""
- 制作自定义模块
python中已经帮我们实现了很多的模块，不过有时候我们需要一些个性化的模块，这里就可以通过自定义模块实现，也就是自己制作一个模块
"""
# 案例：新建一个python文件，命名为my_module1.py
import my_module1
from my_module1 import test
test(10, 20)
"""
- 注意：
每个python文件都可以作为一个模块，模块的名字就是文件的名字，也就是说自定义模块名必须要符合标识符命名规则

- 注意事项：
模块1代码
def my_test(a, b):
    print(a + b)

模块2代码
def my_test(a, b):
    print(a - b)
    
导入模块和调用功能代码
from my_module1 import my_test
from my_module2 import my_test

my_test函数是模块2中的函数
my_test(1, 1)

注意事项：当导入多个模块的时候，且模块内有同名功能，当调用这个同名功能的时候，调用到的是后面导入的模块的功能
"""

# 导入不同模块的同名功能
from my_module1 import test
from my_module2 import test #   使用的是my_module2模块
test(1, 2)

"""
- 测试模块
在实际开发中，当一个开发人员编写完一个模块后，为了让模块能够在项目中达到想要的效果
这个开发人员会自行在py文件中添加一些测试信息，例如，在my_module1.py文件中添加测试代码test(1, 1)
def test(a, b):
    print(a + b)
test(1, 2)

问题：
此时，无论是当前文件，还是其他已经导入了该模块的文件，在运行的时候都会自动执行'test'函数的调用

解决方案：
def test(a, b):
    print(a + b)
只在当前文件中调用该函数，其他导入的文件不符合该条件，则不执行test函数调用
if__name__=="__main__":
    test(1, 2)
"""
# _main_变量
from my_module1 import test #   当my_module1模块中设置了__main__之后，模块内调用test函数，结果不执行

"""
- __all__
如果一个模块文件中有__all__变量，当使用from xxx import *导入时，只能导入这个列表中的元素 #  __all__只作用于*，如使用from xxx import test_b那么__all__将失效，test_b能正常调用
"""
from my_module3 import *
test_a(1, 2)
try:
    test_b(1, 2) # 因my_module3模块中把test_b赋值给了__all__，所以从外部调用模块的时候只能使用test_a函数
except NameError as e:
    print(e)

"""
- 总结
1. 如何自定义模块并导入？
在python代码为你教案中正常写代码，通过import、from关键字和导入python内置模块一样导入即可使用
2. __main__变量的功能是？
if__name__=="__main__"表示，只有当程序是直接执行的才会进入if内部，如果是被导入的，则if无法进入
3. 注意事项
· 不同模块，同名的功能，如果都被导入，那么后导入的会覆盖先导入的
· __all__变量可以控制import *的时候哪些功能可以被导入
"""




