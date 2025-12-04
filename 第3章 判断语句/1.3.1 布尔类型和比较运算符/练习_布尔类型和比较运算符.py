# 演示布尔类型的定义以及比较运算符的应用

# 定义变量存储布尔类型的数据
"""
- 真：True
- 假：False
布尔类型的字面量
"""
bool_1 = True
bool_2 = False
print(f"bool_1变量的内容是：{bool_1}，类型是：{type(bool_1)}")
print(f"bool_2变量的内容是：{bool_2}，类型是：{type(bool_2)}")

# 比较运算符的使用
# ==, !=, >, <, >=, <= （比较运算符）

# 演示进行内容的相等比较
num1 = 10
num2 =10
print(f"10 == 10的结果是：{num1 == num2}")

# 演示进行内容的不相等比较
num1 = 10
num2 = 5
print(f"10 != 5的结果是：{num1 != num2}")

name1 = "itcast"
name2 = "itheima"
print(f"itcast == itheima的结果是：{name1 == name2}") # 比较运算符可用于字符串

# 演示大于小于、大于等于、小于等于的比较运算
num1 = 10
NUM2 = 5
print(f"10 > 5的结果是：{num1 > num2}") # 大于
print(f"5 < 10的结果是：{num2 < num1}") # 小于
print(f"10 >= 5的结果是：{num1 >= num2}") # 大于等于
print(f"5 <= 10的结果是：{num2 <= num1}") # 小于等于

"""
- 总结：
1.在python中，可以表示真假的数据类型是：
布尔类型(bool)，字面量True表示真，字面量False表示假

2.除了可以定义布尔类型外，还可以通过比较运算符计算得到布尔类型
· == 判断内容是否相等，满足为true，不满足为false （a=3,b=3，则（a == b）为true
· != 判断内容是否不相等，满足为true，不满足为false （a=1,b=3，则(a != b)为true
· > 判断运算符左侧内容是否大于右侧，满足为true，不满足false (a=7,b=3,则（a > b)为true
· < 判断运算符左侧内容是否小于右侧，满足true，不满足为false (a=3,b=7,则（a < b)为true
· >= 判断运算符左侧内容是否大于等于右侧，满足为true，不满足false (a=3,b=3,则（a >= b)为true
· <= 判断运算副左侧内容是否小于等于右侧，满足为true，不满足false (a=3,b=3,则（a <= b)为true
"""