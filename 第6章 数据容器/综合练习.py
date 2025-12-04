"""
- 需求：幸运数字6
输入任意数字，如数字8，生成nums列表，元素值为1~8，从中选取幸运数字(能够被6整除)移动到新列表lucky，打印nums与lucky。
"""

# 设置输入数字
input_num = int(input("请输入您的数字："))
# 生成nums列表
nums = list(range(1, input_num + 1))
# 设置一个空列表用于接收符合条件的元素
lucky_nums = []
# 判断元素是否符合条件
for element in nums:
    if element % 6 == 0:
        lucky_nums.append(element)
print(f"{nums}中能被6整除的数字为：{lucky_nums}")

