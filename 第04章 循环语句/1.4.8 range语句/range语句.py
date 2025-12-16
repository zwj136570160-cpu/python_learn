"""
- range语句
for 临时变量 in 待处理数据集（序列）
    循环满足条件时执行的代码
语法中的：待处理数据集，严格来说，称之为：序列类型
序列类型指，其内容可以一个个依次取出的一种类型，包括：
· 字符串
· 列表
· 元组
· 等

for循环语句，本质上是遍历：序列类型。
尽管除字符串外，其它的序列类型目前没学习到，但是不妨碍我们通过学习range语句，获得一个简单的数字序列。

- 语法1：
range(num)
获取一个从0开始，到num结束的数字序列（不含num本身）
如：range(5)取得的数据是：[0,1,2,3,4]

语法2：
rnage(num1,num2)
获得一个从num1开始，到num2结束的数字序列（不含num2本身）
如：range(5,10)取得的数据是：[5,6,7,8,9]

语法3：
range(num1, num2, step)
获得一个从num1开始到num2结束的数字序列（不含num2本身），数字之间的步长，以step为准（step默认为1）
如：range(5,10,2)取得数据是：[5,7,9]
"""

# range 语法1 range(num)
for x in range(10):
    print(x)

# range 语法2 range(num1,num2)
for y in range(5,10):
# 从5开始，到10结束（不含10本身）的一个数字序列，数字之间的间隔是1
    print(y)

# range 语法3 range(num1, num2, step)
for z in range(5,10,2):
# 从5开始，到10结束（不含10本身）的一个数字序列，数字之间的间隔是2
    print(z)

# 案例1：给楠楠送10朵花
for i in range(1,11):
    print(f"给楠楠送{i}朵花")

"""
- 总结
1.range语句的功能是：
获得一个数字序列
2.range语句的语法格式：
语法1 range(num)
语法2 range(num1,num2)
语法3 range(num1, num2, step)
3.range语句的注意事项：
· 语法1从0开始，到num结束（不含num本身）
· 语法2从num1开始，到num2结束（不含num2本身）
· 语法3从num1开始，到num2结束（不含num2本身），步长以step值为准

range的用途很多，多数用在for循环场景
"""