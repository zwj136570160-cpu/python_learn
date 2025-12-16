"""
- 学习目标
1.快速体验函数的使用
2.了解函数的作用
"""
from itertools import count

# 1.5.11 函数综合案例_练习：是组织好的，可重复使用的，用来实现特定功能打代码段
# 案例
name = "weijing"
length = len(name)
print(length)

"""
- 思考：为什么随时都可以使用len()统计长度？
因为，len()是python内置的函数：
· 是提前写好的
· 可以重复使用
· 实现统计长度这一特定功能的代码段

我们使用过的：input()、print()、str()、int()等都是python的内置函数
"""

"""
- 函数的快速体验案例
不使用内置函数len()，完成字符串长度的计算
注意：体验代码，会出现未学习到的语法，只需要关心效果即可
"""

# 需求：统计字符串的长度，不使用内置函数len()
str1 = "weijing"
str2 = "guangyao"
str3 = "python"

# 定义一个计数的变量
count = 0
for i in str1:
    count += 1
print(f"字符串{str1}的长度是：{count}")

for i in str2:
    count += 1
print(f"字符串{str1}的长度是：{count}")

for i in str3:
    count += 1
print(f"字符串{str1}的长度是：{count}")

# 以上代码过于重复，可使用len函数来优化这个过程
def my_len(data): # my_len是一个自定义的函数符合函数的定义：1.已组织好的 2.可重复使用 3.针对特定功能
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度是：{count}")

my_len(str1)
my_len(str2)
my_len(str3)

"""
- 思考：为什么要学习、使用函数？
为了得到一个针对特定需求、可供重复利用的代码段，提高程序的复用性、减少重复性代码、提高开发效率   优雅！！！！！！！！！！！！！！！
"""

"""
- 总结
1.函数是：
组织好的、可重复使用的、用来实现特定功能的代码段
2.使用函数的好处是：
· 将功能封装在函数内，可供随时随地重复利用
· 提高代码的复用性，减少重复代码，提高开发效率
"""


