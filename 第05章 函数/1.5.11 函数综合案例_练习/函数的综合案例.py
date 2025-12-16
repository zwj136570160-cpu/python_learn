"""
- 综合案例：味精ATM
· 主菜单效果
-----------------主菜单-----------------
楠楠，您好，欢迎来到味精银行，请选择操作：
查询余额 [输入1]
存款    [输入2]
取款    [输入3]
退出    [输入4]
请输入您的选择：
· 查询余额效果
-----------------查询余额-----------------
楠楠，您好，您的余额剩余：5000000元
· 存、取款效果
-----------------存款-----------------
楠楠，您好，您存款50000元成功
楠楠，您好，您的余额剩余：5050000元
-----------------取款-----------------
楠楠，您好，您取款50000元成功
楠楠，您好，您的余额剩余：4950000元

· 定义一个全局变量：money，用来记录银行卡余额（默认5000000）
· 定义一个全局变量，name，用来记录客户姓名（启动程序时输入）
· 定义如下的函数：
    · 查询余额函数
    · 存款函数
    · 取款函数
    · 主菜单函数
· 要求：
· 程序启动后要求输入客户姓名
· 查询余额、存款、取款后都会返回主菜单
· 存款、取款后，都应显示一下当前余额
· 客户选择退出或输入错误，程序会退出，否则一直运行
"""

money = 5000000
name = input("请输入您的姓名：") # 获取用户ID

# 主菜单
def main_menu():
    print("-----------------主菜单-----------------")
    print(f"{name}，您好，欢迎来到味精银行，请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    # 通过\t制表符对齐输出
    return input("请输入您的选择：")

# 查询余额
def query(show_header):
    if show_header:
        print("-----------------查询余额-----------------")
    print(f"{name}，您好，您的余额剩余：{money}元")

# 存款
def deposit(amount):
    print("-----------------存款-----------------")
    global money
    money += amount
    print(f"{name}，您好，您存款{money}元成功")

    # 调用query查询余额
    query(False)

# 取款
def withdraw_money(withdraw):
    print("-----------------取款-----------------")
    global money
    money -= withdraw
    print(f"{name}，您好，您取款{withdraw}元成功")

    # 调用query查询余额
    query(False)

# 设置无限循环，确保程序不会退出
while True:
    keyboard_input = main_menu()
    if keyboard_input == "1":
        query(True)
        continue

    elif keyboard_input == "2":
        input_amount = int(input("请输入您需要存入的金额："))
        deposit(input_amount)
        continue

    elif keyboard_input == "3":
        input_amount = int(input("请输出您需要取出的金额："))
        withdraw_money(input_amount)
        continue

    elif keyboard_input == "4":
        print("程序退出拉！！")
        break # 通过break退出循环，程序退出
    else:
        print("选择错误")
        break # 通过break退出循环，程序退出


