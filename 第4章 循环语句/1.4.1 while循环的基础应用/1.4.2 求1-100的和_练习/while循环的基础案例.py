"""
- 目标：能够使用while循环，完成猜数字案例

- 需求：设置一个1——100的随机整数变量，通过while循环，配合input语句，判断输入的数字是否等于随机数
· 无限次机会，直到猜中为止
· 每一次猜不中，会提示大了或小了
· 猜完数字后，提示猜了几次
提示：
· 无限次机会，终止条件不适合用数字累加来判断
    · 可以考虑布尔类型本身
· 需要提示几次猜中，就需要提供数字累加功能
· 随机数可以使用：import random
               num = random.randint(1,100)
"""

#获取1-100的随机数字
import random
num = random.randint(1,100)
count = 0

# 通过一个布尔类型的变量，做循环是否继续的标记
flag = True
while flag:
    guess_num = int(input("请输入你猜测的数字："))
    count += 1
    if guess_num == num:
        # 将flag设置为False将终止while循环
        flag = False
        print("恭喜你，你猜对了！")
    else:
        # 提示大了或小了
        if guess_num > num:
            print("你猜大了！")
        else:
            print("你猜小了！")
# 提示猜测次数
print(f"你一共猜了：{count}次，恭喜你猜对了！，正确的数字为：{guess_num}")

