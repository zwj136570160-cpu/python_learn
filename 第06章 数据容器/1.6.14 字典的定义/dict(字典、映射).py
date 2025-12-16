"""
- 目标：
1. 掌握字典的定义格式
"""

"""
- 为什么使用字典
· 生活中的字典：
通过字可以找到对应的含义
· python中的字典
通过Key找到对应的Value
"""

"""
- 案例
老是有一份名单，记录了学生的姓名和考试总成绩
姓名   成绩
小王   77
小张   88
味精   99
现在需要将其通过python录入至程序中，并可以通过学生姓名检索学生的成绩
使用字典最为合适
姓名：Key
成绩：Value
可以通过Key(姓名)，取到对应的Value(成绩)

为什么使用字典？
因为可以使用字典，使用先Key取出Value的操作
"""

"""
- 字典的定义
同样使用{}，不过存储的元素是一个个的：键值对

定义字典字面量
{key: value, key:value, ......, key: value}
定义字典变量
my_dict = {key: value, key: value, ......, key: value}
定义空字典
my_dict = {}
my_dict = dict()
"""
# 定义字典
my_dict = {"小王": 77, "小张": 88, "味精": 99}     # 定义字典变量

# 定义空字典
my_dict_2 = {}    # 使用{}定义空字典
my_dict_3 = dict()    # 使用dict()定义空字典
print(f"字典1的内容是：{my_dict}，类型是：{type(my_dict)}")
print(f"字典2的内容是：{my_dict_2}，类型是：{type(my_dict_2)}")
print(f"字典1的内容是：{my_dict_3}，类型是：{type(my_dict_3)}")
# 目前接触到的数据类型：list(列表)、tuple(元组)、str(字符串)、1.6.12 集合的定义和操作、dict(字典)

# 定义重复的字典
my_dict = {"小王": 77, "小张": 88, "味精": 99, "小张": 79, "小张": 60}
# 字典不允许重复，新的Key会覆盖老的Key

"""
- 字典数据的获取
字典同集合一样，不可以使用下标索引
但是字典可以通过key值来取得对应的value
语法：字典key可以取得对应的value
"""
my_dict = {"小王": 77, "小张": 88, "味精": 99}
score_key_1 = my_dict["小王"]
score_key_2 = my_dict["小张"]
score_key_3 = my_dict["味精"]
print(f"小王的考试成绩是：{score_key_1}")
print(f"小张的考试成绩是：{score_key_2}")
print(f"味精的考试成绩是：{score_key_3}")

"""
- 字典的嵌套
字典的key和value可以是任意数据类型（key不可为字典）
证明，字典是可以嵌套

· 需求如下，记录学生各科的考试信息
姓名   语文   数学   英语
小王   77    66    33
小张   88    86    55
味精   99    96    66
"""
# 定义嵌套字典
stu_score_dict = {
    "小王": {
        "语文": 77,
        "数学": 66,
        "英语": 33
    }, "小张": {
        "语文": 88,
        "数学": 86,
        "英语": 55
    }, "味精": {
        "语文": 99,
        "数学": 96,
        "英语": 66
    }
}
print(f"学生的考试信息是：{stu_score_dict}")
# 从嵌套字典中获取数据
# 看一下小王的语文信息
score = stu_score_dict["小王"]["语文"]
print(f"小王的语文成绩是：{score}")

"""
- 总结
1. 为什么使用字典
字典可以提供基于key检索value的场景实现
2. 字典的定义语法
定义字典字面量
{key: value, key:value, ......, key: value}
定义字典变量
my_dict = {key: value, key: value, ......, key: value}
定义空字典
my_dict = {}
my_dict = dict()
3. 字典的注意事项
· 键值对的key和value可以是任意类型（key不可为字典）
· 字典内的key不允许重复，重复添加等同于覆盖原有数据
· 字典不可使用下标索引，而是通过key检索value
"""
