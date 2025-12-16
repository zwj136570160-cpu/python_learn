"""
- 基于学到的循环知识，完成发工资案例
练习案例：发工资
某公司，账户余额有1万元，给20名员工发工资
· 员工编号从1到20，从编号1开始，依次领取工资，每人可领取1000元
· 领工资时，财务判断员工的绩效分（1-10）（随机生成），如果低于5，不发工资，换下一位
· 如果工资发完了，结束发工资
提示：
· 使用循环对员工依次发放工资
· continue用于跳过员工，break直接结束发工资
· 随机数可以用：
import random
num = random.randint(1,10)
"""

# 定义账户余额
money = 10000
# for循环对员工发放工资
for staff in range(1,21):
    # 生成员工随机绩效
    import random
    num = random.randint(1, 10)
    # 判断员工绩效是否符合发工资条件
    if num < 5:
        print(f"员工{staff},绩效分{num},低于5，不发工资，下一位。")
        # 使用continue语句中断绩效不符合发放工资的员工循环
        continue
    elif num > 5:
        # 判断工资余额是否足够，如不足够使用break暂停发放工资
        if money >= 1000:
            money -= 1000
            print(f"向员工{staff}发放工资1000元，账户余额{money}元。")
        else:
            print("工资发完了，下个月领取把。")
            break

