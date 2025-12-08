"""
此工具包my_utils仅用于1.9.8 综安案例学习使用
"""

"""
· print_file_info(file_name)，接收传入文件的路径，打印文件的全部内容，如文件不存在则捕获异常，输出提示信息，通过finally关闭文件对象
· append_to_file(file_name, date)，接收文件路径以及传入数据，将数据追加写入到文件中
"""

# 接收传入文件的路径，打印文件的全部内容，如文件不存在则捕获异常，输出提示信息，通过finally关闭文件对象
def print_file_info(file_name):
    """
    接收文件，并进行打印，如存在异常则捕获异常，并进行输出提示信息，最后通过finally关闭文件
    :param file_name: 需要打开的文件路径
    :return: None
    """
    f = None
    try: #  如执行代码出现异常，则捕获异常
        f = open(file_name, "r", encoding ="utf-8")
        content = f.read()
        print(f"文件的全部内容如下：\n{content}") #   打印文件的全部内容
    except Exception as e: #    捕获异常之后并进行输出异常信息
        print(f"程序出现异常了，原因是：{e}")
    finally:
        if f:
            f.close()
if __name__ == "__main__": # 用于测试print_file_info函数，外部调取不生效
    print_file_info("测试文本.txt")

# 接收文件路径以及传入数据，将数据追加写入到文件中
def append_to_file(file_name, date):
    """
    接收文件并传入数据，并将数据追加写入到文件中
    :param file_name:需要接收的文件路径
    :param date:追加的数据信息
    :return: None
    """
    with open(file_name, "a", encoding ="utf-8" ) as f: #   打开文件
        f.write("此文件仅用于1.9.8综合练习使用")
        f.write("\n")
        f.write(date) # 写入文件
        f.flush() # 将写入的文件存入硬盘内进行刷新



