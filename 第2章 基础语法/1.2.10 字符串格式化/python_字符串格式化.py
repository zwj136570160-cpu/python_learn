# 掌握通过占位的形式拼接字符串（字符串格式化）

# 变量过多，拼接起来太麻烦
"""
name = "味精"
add = "兰亭公寓"
tel = 139999999
print("我的名字是：" + name +  "我的地址是：" + add + "我的电话是：" +  tel)
"""
from pyexpat.errors import messages

# 字符串无法和数字或其他数据类型完成拼接

# 思考：是否有其他方式，既方便又支持拼接其他类型？
# 答案：有，可以通过字符串的格式化完成和各数据类型的拼接

# 格式化语法：
name = "味精"
messages = "要帅哥微信 %s" % name
print(messages)
# 其中的，%s
# % 表示：我要占位
# s 表示：将变量变成字符串放入占位的地方

# 数字类型也可以通过格式化完成和字符串的拼接
name = "味精,"
add = "兰亭公寓,"
tel = 139999999
avg_salary = 12000
messages = "我的名字是：%s，家住：%s，手机号是：%s，工资是：%s元" % (name, add, tel, avg_salary)
print(messages)

"""
- 在python中，支持非常多的数据类型占位
1.%s 将内容转化为字符串，放入占位位置
2.%d 将内容转化为整数，放入占位位置
3.%f 将内容转化为浮点型，放入占位位置
"""

name = "味精"
tel = 150270
h_no = 605.5
messages = "我的名字是：%s，手机号是：%d，家住%f" % (name, tel, h_no)
print(messages)





















