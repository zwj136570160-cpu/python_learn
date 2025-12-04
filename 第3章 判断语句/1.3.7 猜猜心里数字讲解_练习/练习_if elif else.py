"""
- 练习案例：猜猜心里数字
1.定义一个变量，数字类型，内容随意
2.基于input语句输入猜想的数字，通过if和多次elif的组合，判断猜想数字是否和心里数字一致。
"""
# 方式1
num = int(input("请输入第一次猜想的数字："))
num1 = int(input("不对，再猜一次："))
num2 = int(input("不对，再猜最后一次："))

if num == 1:
    print("正确！")
elif num1 == 2:
    print("正确！")
elif num2 == 3:
    print("正确！")
else:
    print("sorry，全部猜错拉，我想的是：10")

# 方式2
num = 10 # 定义一个变量数字

# 通过键盘输入获取猜想的数字，通过多行if 和 elif的组合进行猜想比较
if int(input("请输入第一次猜想的数字：")) == num:
    print("恭喜第一次就猜对了呢！")
elif int(input("不对，再猜一次：")) == num:
    print("恭喜你猜对了呢！")
elif int(input("不对，再猜最后一次：")) == num:
    print("猜对啦！！")
else:
    print("sorry，全部猜错拉，我想的是：10")