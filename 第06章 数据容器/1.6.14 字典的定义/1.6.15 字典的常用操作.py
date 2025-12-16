"""
- 目标
1. 掌握字典的常用操作
2. 掌握字典的特点
"""

"""
- 字典的常用操作
· 新增元素
    语法：字典[Key] = Value，结果：字典被修改，新增了元素
· 更新元素
    语法：字典[Key] = Value，结果：字典被修改，元素被更新
    注意：字典Key不可以重复，所以对已存在的Key执行上述操作，就是更新Value值
· 删除元素
    语法：字典.pop(key)，结果：获取指定key的value，同时字典被修改，指定key的数据被删除
· 获取全部的Key
    语法：字典.keys()，结果：得到字典中的全部Key
"""

# 定义字典
my_dict = {"小王": 77, "小张": 88, "味精": 99}
# 新增元素
my_dict["楠楠"] = 100
print(f"字典经过新增元素后，结果：{my_dict}")
# 更新元素
my_dict["味精"] = 70
print(f"字典经过更新元素后，结果：{my_dict}")
# 删除元素
score = my_dict.pop("味精")
print(f"字典中被移除了一个元素，结果：{my_dict}，味精的考试分数是：{score}分")
# 清空元素（clear）
my_dict.clear()
print(f"字典被清空了，内容是：{my_dict}")
# 获取全部key
my_dict = {"小王": 77, "小张": 88, "味精": 99}
keys = my_dict.keys()
print(f"字典的全部keys是：{keys}")
# 遍历字典
# 方式1：通过获取到全部的key来完成遍历
for key in keys:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{my_dict[key]}")
# 方式2：直接对字典进行for循环，每一次循环都是直接得到key
for key in my_dict:
    print(f"字典2的key是：{key}")
    print(f"字典2的value是：{my_dict[key]}")
# 统计字典内的元素数量
element_num = len(my_dict)
print(f"字典中的元素有：{element_num}个")

"""
- 字典的常用操作
字典[Key]   获取指定Key对应的Value值
字典[Key]=Value   添加或更新键值对
字典.pop(Key)   取出Key对应的Value并在字典内删除此Key的键值对
字典.clear()   清空字典
字典.keys()   获取字典的全部Key，可用于for循环遍历字典
len(字典）   计算字典内的元素数量
"""

"""
- 字典的特点
经过上述对字典的学习，可以总结出字典有如下特点：
· 可以容纳多个数据
· 可以容纳不同类型的数据
· 每一份数据是Key Value键对值
· 可以通过Key获取到Value，Key不可重复（重复会覆盖）
· 不支持下标索引
· 可以修改（增加或删除更新元素等）
· 支持for循环，不支持while循环
"""

"""
- 总结
1. 字典的常用操作
字典[Key]   获取指定Key对应的Value值
字典[Key]=Value   添加或更新键值对
字典.pop(Key)   取出Key对应的Value并在字典内删除此Key的键值对
字典.clear()   清空字典
字典.keys()   获取字典的全部Key，可用于for循环遍历字典
len(字典）   计算字典内的元素数量
2. 操作注意
· 新增和更新元素的语法一直，如果key不存在即新增，如果key存在即更新（key不可重复）
3. 字典的特点
· 可以容纳多个数据
· 可以容纳不同类型的数据
· 每一份数据是Key Value键对值
· 可以通过Key获取到Value，Key不可重复（重复会覆盖）
· 不支持下标索引
· 可以修改（增加或删除更新元素等）
· 支持for循环，不支持while循环
"""