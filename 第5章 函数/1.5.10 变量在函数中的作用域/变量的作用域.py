"""
- 目标
1.知道什么是局部变量
2.知道什么是全局变量
"""

"""
- 局部变量
变量作用域指的是变量的作用范围（变量在哪里可用，在哪里不可用）
主要分为两类：局部变量和全局变量

所谓局部变量是定义在函数体内部的变量，即只在函数体内部生效
"""
# 演示局部变量
def testA():
    num = 100
    print(num)

testA() # 100
print(num) # 报错：name 'num' is not defined，出了函数体，局部变量就无法使用了！！
"""
变量num是定义在testA函数内部的变量，在函数体外部访问则立即报错

局部变量的作用：在函数体内部，临时保存数据，即当函数调用完成后，则销毁局部变量
"""

"""
- 全局变量
所谓全局变量，指的是在函数体内、体外都能生效的变量
思考：如果有一个数据，在函数体A和函数B中都要使用，该怎么办？
将这个数据存储在一个全局变量里面
"""
# 演示全局变量
# 定义全局变量a
num = 100

def test_a():
    print(f"test_a:{num}")  # 访问全局变量num，并打印变量num存储的数据

def test_b():
    print(f"test_b:{num}")  # 访问全局变量num，并打印变量num存储的数据

test_a()
test_b()
print(num)

"""
- global关键字
思考：testB函数需要修改变量num的值为200，如何修改程序？
"""
num = 100

def testA():
    print(num)

def testB():
    num = 200 # 局部变量
    print(num)

testA() # 结果：100
testB() # 结果：200
print(f"全局变量num = {num}") # 结果：全局变量num = 100
# testB函数内部的num = 200是定义了一个局部变量

# global关键字，在函数内声明变量为全局变量
num = 100

def testA():
    print(num)


def testB():
    global num # 设置内部定义的变量为全局变量
    num = 200
    print(num)


testA()  # 结果：100
testB()  # 结果：200
print(f"全局变量num = {num}")  # 结果：全局变量num = 100

"""
- 总结
1.什么是局部变量
作用范围在函数内部，在函数体外部无法使用
2.什么是全局变量
在函数内部和外部均可使用
3.如何将函数内定义的变量声明为全局变量
· 使用global关键字，global变量
"""