"""
- 目标
1. 知道函数如何返回多个返回值
"""

"""
- 如果一个函数如这两个return，程序如何执行
"""
def return_num():
    return 1    # 只执行了第一个return，原因是因为return可以退出当前函数，导致return下方的代码不执行
    return 2
result = return_num()
print(result)

"""
- 如果一个函数要返回多个返回值，该如何书写？
"""
def test_return():
    return 1, 2
x, y = test_return()
print(x)
print(y)
# 按照返回值的顺序，写对应顺序的多个变量接收即可
# 变量之间用逗号隔开
# 支持不同类型的数据return

# 演示多个变量，接收多个返回值
def test_return():
    return 1, 2, 3, 4
x, y, z, i = test_return()
print(x)
print(y)
print(z)
print(i)