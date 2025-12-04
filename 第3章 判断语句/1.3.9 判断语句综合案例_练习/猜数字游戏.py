# 通过逻辑判断语句，完成猜数字的案例代码编写

"""
- 案例需求：
定义一个数字（1~10，随机产生），通过3次判断来猜出数字

- 案例要求：
1.数字随机产生，范围1-10
2.有三次机会猜测数字，通过3层嵌套判断实现
3.每次猜不中，会提示大了或小了

提示：通过如下代码，可以定义一个变量num，变量内存储随机数字
import random
num = random.randint(1,10)
"""

# 构建一个随机的数字变量
import random
num = random.randint(1,10)
guess_num = int(input("请输入你猜测的数字："))

# 通过if判断语句进行数字的猜测
if guess_num == num:
    print("恭喜！第一次就猜对了！")
else:
    if guess_num > num:
        print("你猜大了")
    else:
        print("你猜小了")

    # 第二次猜测数字
    guess_num = int(input("再次输入你要猜测的数字："))

    if guess_num == num:
        print("恭喜！第二次猜中了！")
    else:
        if guess_num > num:
            print("你猜大了")
        else:
            print("你猜小了")

    #第三次猜测数字
    guess_num = int(input("你还有一次机会，请输入你要猜测的数字："))

    if guess_num == num:
        print("恭喜！猜对了！")
    else:
        print(f"不好意思，你的机会用完了，正确答案是：{num},游戏失败")

