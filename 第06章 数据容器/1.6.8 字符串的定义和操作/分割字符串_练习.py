"""
- 练习案例：分割字符串

给定一个字符串："guangyao and weijing"
· 统计字符串内有多少个"g"字符
· 将字符串内的空格，全部替换为字符："|"
· 并按照"|"进行字符串分割，得到列表
"""

# 用变量接收字符串
my_str = "guangyao and weijing"

# 统计字符串内有多少个"g"字符
count_num = my_str.count("g")
print(f"字符串{my_str}中字符串'g'有{count_num}个")

# 将字符串内的空格，全部替换为字符："|"
new_my_str = my_str.replace(" ", "|")
print(f"字符串{my_str}，被替换空格后，结果是：{new_my_str}")

# 按照"|"进行字符串分割，得到列表
new_my_str_2 = new_my_str.split("|")
print(f"字符串{new_my_str}，按照|分割后，得到：{new_my_str_2}")