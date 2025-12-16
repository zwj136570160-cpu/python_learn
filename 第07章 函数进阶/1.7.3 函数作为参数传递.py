"""
- 目标
1. 掌握函数作为参数传递
"""

"""
在前面函数学习中，我们一直使用的函数，都是接受数据作为参数传入：
· 数字
· 字符串
· 字典、列表、元组

我们学习的函数本身，也可以作为参数传入另一个函数内
"""


def test_func(compute):     # compute传递的是函数计算逻辑，与def定义的函数数据不同
    result = compute(1, 2)
    print(f"compute的数据类型是：{type(compute)}")
    print(f"计算结果是：{result}")

def compute(x, y):
    return x + y

test_func(compute)
"""
函数compute，作为参数，传入了test_func函数中使用
· test_func需要一个函数作为参数传入，这个函数需要接收2个数字进行计算，计算逻辑由这个被传入函数决定
· compute函数接收2个数字对齐进行计算，compute函数作为参数，传递给了test_func函数使用
· 最终，在test_func函数内部，由传入的compute函数，完成了对数字的计算操作

所以，这是一种，计算逻辑的传递，而非数据的传递
"""

"""
- 总结
1. 函数本身是可以作为参数，传入另一个函数中进行使用的
2. 函数传入的作用在于：传入计算逻辑，而非传入数据
"""


