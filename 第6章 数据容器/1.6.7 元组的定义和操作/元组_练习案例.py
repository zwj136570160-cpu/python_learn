"""
- 练习案例：元组的基本操作
定义一个元组，内容是：（"光耀", 11, ["football", "music"])，记录的是一个学生的信息（姓名、年龄、爱好）

请通过元组的功能（方法），对其进行
1.查询其年龄所在的下标位置
2.查询学生的姓名
3.删除学生爱好中的football
4.增加爱好：coding到爱好list内
"""

# 定义元组用变量接收
my_tuple = ("光耀", 11, ["football", "music"])

# 查询其年龄所在的下标位置
age = my_tuple.index(11)
print(f"年龄的下标位置是：{age}")

# 查询姓名
name = my_tuple[0]
print(f"学生的姓名为：{name}")

# 删除学生爱好中的football
del my_tuple[2][0]
print(my_tuple)

# 增加爱好coding到爱好list内
my_tuple[2].append("coding")
print(f"添加爱好coding至元组list中，结果为：{my_tuple}")
