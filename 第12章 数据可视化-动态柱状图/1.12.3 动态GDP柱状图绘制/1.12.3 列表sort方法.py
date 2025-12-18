"""
- 目标
1. 掌握列表的sort方法并配合lambda匿名函数完成列表排序
2. 完成图表所需的数据处理
3. 完成GDP动态图表绘制
"""

"""
- 列表的sort方法
在前面我们学习过sorted函数，可以对数据容器进行排序
在后面的数据处理中，我们需要对列表进行排序，并指定排序规则，sorted函数就无法完成了。
我们补充学习列表的sort方法

- 使用方式
list.sort(key=选择排序依据的函数，reverse=True/false)
· 参数key，是要求传入一个函数，表示将列表的每一个元素都传入函数中，返回排序的依据
· 参数reverse，是否反转排序结果，True表示降序，False表示升序
"""

#   准备list
my_list = [["a", 33], ["b", 55], ["c", 11]]
#   排序，基于带名函数
# def choose_sort_key(element):
#     return element[1]
# my_list.sort(
#     key=choose_sort_key,
#     reverse=True
# )
#   排序，基于lambda匿名函数
my_list.sort(
    key=lambda element: element[1],reverse=True
)