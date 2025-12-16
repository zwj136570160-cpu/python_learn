# 可以使用tpye语句来得到数据的类型
# type语句语法：type(被查看类型的数据)

# 在print语句中，直接输出数据类型信息
print(type(666)) # 整数 int
print(type(13.14)) # 浮点 float
print(type("味精，味精！！！！")) # 字符串 string 缩写：str

# 用变量存储type的结果（返回值）
int_type = type(666)
float_type = type(13.14)
string_type = type("味精，味精！！！")

print(string_type)
print(int_type)
print(float_type)

# 使用type语句，查看变量中存储的数据类型
name = "味精"
name_type = type(name)
print(name_type)

# 变量有类型吗？
# 通过type(1.2.3 变量）输出类型，这是查看变量的类型还是数据类型？
# 查看的是变量存储的类型，在python中变量无类型，但是变量存储的数据有类型