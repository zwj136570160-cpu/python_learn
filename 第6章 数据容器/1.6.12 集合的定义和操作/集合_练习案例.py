"""
- 信息去重
有如下列表对象：
my_list = ["光耀", "味精", "楠楠", "python", "光耀", "味精", "best", "python", "python", "best", "python", "python"]

· 定义一个空集合
· 通过for循环遍历列表
· 在for循环中将列表的元素添加至集合
· 最终得到元素去重后的集合对象，并打印输出
"""

my_list = ["光耀", "味精", "楠楠", "python", "光耀", "味精", "best", "python", "python", "best", "python", "python"]
# 定义一个空集合
set_empty = set()
# for循环遍历列表
for element in my_list:
    set_empty.add(element)
# 输出去重后的集合对象
print(f"遍历列表my_list并将元素添加至空集合set_empty，结果是：{set_empty}")
