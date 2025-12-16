"""
- 数据容器的通用操作 - 遍历
数据容器尽管各自有各自的特点，但是他们也有通用的一些操作

首先，在遍历上
· 5类数据容器都支持for循环 （列表、元组、字符串、集合、字典）
· 列表、元组、字符串支持while循环遍历，集合、字典不支持（无法下标索引）

尽管遍历的形式各有不同，但是，他们都支持遍历操作

- 数据容器的通用统计功能
除了遍历这个共性外，数据容器可以通用非常多的功能方法
len(容器)：统计容器的元素个数
max(容器)：统计容器的最大元素
min(容器)：统计容器的最小元素
"""

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}
# len元素个数
print(f"列表，元素个数有：{len(my_list)}个")
print(f"元组，元素个数有：{len(my_tuple)}个")
print(f"字符串，元素个数有：{len(my_str)}个")
print(f"集合，元素个数有：{len(my_set)}个")
print(f"字典，元素个数有：{len(my_dict)}个")

# max最大元素
print(f"列表，最大元素是：{max(my_list)}")
print(f"元组，最大元素是：{max(my_tuple)}")
print(f"字符串，最大元素是：{max(my_str)}")
print(f"集合，最大元素是：{max(my_set)}")
print(f"字典，最大元素是：{max(my_dict)}")

# min最小元素
print(f"列表，最小元素是：{min(my_list)}")
print(f"元组，最小元素是：{min(my_tuple)}")
print(f"字符串，最小元素是：{min(my_str)}")
print(f"集合，最小元素是：{min(my_set)}")
print(f"字典，最小元素是：{min(my_dict)}")

"""
- 容器的通用转换功能
除了小标索引这个共性外，还可以通用类型转换
list(容器)：将给定容器转换为列表
str(容器)：将给定容器转换为字符串
tuple(容器)：将给定容器转换为元组
set(容器)：将给定容器转换为集合
"""
# 类型转换：容器转列表
print(f"列表转列表的结果是：{list(my_list)}")
print(f"元组转列表的结果是：{list(my_tuple)}")
print(f"字符串转列表的结果是：{list(my_str)}")
print(f"集合转列表的结果是：{list(my_set)}")
print(f"字典转列表的结果是：{list(my_dict)}")

# 类型转换：容器转元组
print(f"列表转元组的结果是：{tuple(my_list)}")
print(f"元组转元组的结果是：{tuple(my_tuple)}")
print(f"字符串转元组结果是：{tuple(my_str)}")
print(f"集合转元组的结果是：{tuple(my_set)}")
print(f"字典转元组的结果是：{tuple(my_dict)}")

# 类型转换：容器转字符串
print(f"列表转字符串的结果是：{str(my_list)}")
print(f"元组转字符串的结果是：{str(my_tuple)}")
print(f"字符串转字符串结果是：{str(my_str)}")
print(f"集合转字符串的结果是：{str(my_set)}")
print(f"字典转字符串的结果是：{str(my_dict)}") # key和value都能保留

# 类型转换：容器转集合
print(f"列表转集合的结果是：{set(my_list)}")
print(f"元组转集合的结果是：{set(my_tuple)}")
print(f"字符串转集合结果是：{set(my_str)}")
print(f"集合转集合的结果是：{set(my_set)}")
print(f"字典转集合的结果是：{set(my_dict)}")
# 顺序被打乱，由于集合是无序类型

"""
- 容器通用排序功能
通用排序功能
sorted(容器, [reverse = True]) reverse默认为False，将容器的排序结果进行反转可传递True
"""
my_list = [1, 3, 2, 5, 4]
my_tuple = (2, 4, 1, 3, 5)
my_str = "acdrfge"
my_set = {2, 5, 1, 3, 4}
my_dict = {"key3": 1, "key4": 2, "key1": 3, "key2": 4, "key5": 5}
# 进行容器的排序
print(f"列表对象的排序结果：{sorted(my_list)}")
print(f"元组对象的排序结果：{sorted(my_tuple)}")
print(f"字符串对象的排序结果：{sorted(my_str)}")
print(f"集合对象的排序结果：{sorted(my_set)}")
print(f"字典对象的排序结果：{sorted(my_dict)}")
# 排序之后的结果类型是列表（list）

print(f"列表对象的反向排序结果：{sorted(my_list, reverse = True)}")
print(f"元组对象的反向排序结果：{sorted(my_tuple, reverse = True)}")
print(f"字符串对象反向排序结果：{sorted(my_str, reverse = True)}")
print(f"集合对象的反向排序结果：{sorted(my_set, reverse = True)}")
print(f"字典对象的反向排序结果：{sorted(my_dict, reverse = True)}")
