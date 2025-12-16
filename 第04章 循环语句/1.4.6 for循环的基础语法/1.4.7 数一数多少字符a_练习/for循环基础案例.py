"""
- 练习案例：数一数，有几个a
定义字符串变量name，内容为：itheima is a brand of itcast

提示：
1.计数可以在循环外定义一个整数类型变量用来做累计计数
2.判断是否为字母a，可以通过if语句结合比较运算符来完成
"""
name = "itheima is a brand of itcast" # 定义for待处理的序列
i = 0 # 定义一个变量，用来统计多少个a
for x in name:
    if x == "a":
        i += 1

print(f"itheima is a brand of itcast中共含有：{i}个字母a")


