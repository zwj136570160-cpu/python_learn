"""
- 练习案例：取出列表内的偶数
定义一个列表，内容是：[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
· 遍历列表，取出列表内的偶数，并存入一个新的列表中
· 使用while循环和for循环各操作一次

通过while循环，从列表：[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]中取出偶数，组成新列表：[2, 4, 6, 8, 10]
通过for循环，从列表：[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]中取出偶数，组成新列表：[2, 4, 6, 8, 10]

提示：
· 通过if判断来确认偶数
· 通过列表的append方法，来增加元素
"""

# 通过while循环来取出偶数并组成新列表

# 定义一个列表list_while
list_while = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 定义一个变量index来标记列表的下标
index = 0
# 定义一个空列表new_list用于接收符合if条件的元素
new_list = []
# 使用while循环遍历列表
while index < len(list_while):   # 循环条件：下标索引变量 < 列表的元素数量
    element = list_while[index]
    if element % 2 == 0:
        new_list.append(element)
    index += 1   # 对元素进行处理，每次循环index都+1

print(f"通过while循环，从列表：{list_while}中取出偶数，组成新列表:{new_list}")

# 通过for循环来取出偶数并组成新列表
list_while = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []
for element in list_while:
    if element % 2 == 0:
        new_list.append(element)

print(f"通过for循环，从列表：{list_while}中取出偶数，组成新列表:{new_list}")









