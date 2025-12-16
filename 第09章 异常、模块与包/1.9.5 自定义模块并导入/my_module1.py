def test(a, b):
    print(a + b)

if __name__ == '__main__':
    test(1, 2)
# 当模块内运行文件的时候name固定被赋值为main 所以if判断为True，会执行if内部代码，当外部调用模块时，name被赋值为模块名，所以if判断False，所以不执行if内部代码
# __main__是python的内置变量