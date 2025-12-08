"""
此工具包my_utils仅用于1.9.8 综安案例学习使用
"""

"""
· str_reverse(s)，接受传入字符串，将字符串反转返回
· substr(s, x, y)，按照下标x和y，对字符串进行切片
"""

def str_reverse(s):
    """
    将字符串s进行反转
    :param s: 将被反转的字符串
    :return: 反转后的字符串并返回
    """
    slicing = s[::-1]
    return slicing

if __name__ == "__main__":
    print(str_reverse("hello world"))
# 此if判断用于测试str_reverse函数输出结果，当外部调用时不生效

def substr(s, x, y):
    """
    按照下标x和y，对字符串s进行切片操作
    :param s: 需要进行切片的字符串
    :param x: 切片的开始下标
    :param y: 切片的结束下标
    :return: 切片完成的字符串
    """
    slicing_2 = s[x:y]
    return slicing_2

if __name__ == "__main__":
    print(substr("weijing",2,3))
# 此if判断用于测试substr函数输出结果，当外部调用时不生效