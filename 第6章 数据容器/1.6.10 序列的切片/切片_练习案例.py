"""
- 练习案例：序列的切片实践

有字符串："万过薪月，员序程马黑来，nohtyp学"
· 请使用学过的任何方式，得到"黑马程序员"
"""

# 方法1：切片取出，然后倒序
my_str = "万过薪月，员序程马黑来，nohtyp学"
element_num = my_str.index("，")
element_num_2 = my_str.index("黑")
print({element_num}, {element_num_2})
result = my_str[element_num_2:element_num:-1]
print(f"方法1的结果是：{result}")

# 方法2：使用split分隔，replace替换“来”为空，倒序字符串
result2 = my_str.split("，")[1].replace("来", "")[::-1]
print(f"方法2的结果是：{result2}")

# 方法3：倒序字符串，切片取出
result3 = my_str[::-1][9:14]
print(f"方法3的结果是：{result3}")
