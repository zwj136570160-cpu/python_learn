"""
- 掌握在字符串，整数，浮点数之间进行相互转换
- 了解转换的注意事项
"""

"""
- 常见的转换语句
- int(x) 将X转换为一个整数
- float(x) 将X转换为一个浮点数
- str(x) 将X转换为一个字符串
"""
# 以上语句，同type语句一样，都是带有结果的（返回值），可以使用print直接输出，或者同变量存储结果值（返回值）

# 将整数类型转换为字符串
str(666)
int_str = str(666)
print(type(int_str), int_str)

# 将浮点数类型转化为字符串
float_str = str(13.14)
print(type(float_str), float_str)

# 将字符串转化为整数
str_int = int("666")
print(type(str_int), str_int)

# 错误示例，想要将字符串转化为数字，必须保证字符串内容为数字
# num_int = int("味精味精！！！")
# print(type(num_int), num_int)

# 整数转浮点数
int_float = float(666)
print(type(int_float), int_float)

#浮点数转整数
float_int = int(13.14)
print(type(float_int), float_int) # 浮点数转整数，会导致小数点后的部分丢失

