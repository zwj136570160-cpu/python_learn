"""
- 练习案例：自定义工具包
创建一个自定义包，名称为：my_utils（我的工具）
在包内提供两个模块
· str_util.py(字符串相关工具，内含：)
    · 函数：str_reverse(s)，接受传入字符串，将字符串反转返回
    · 函数：substr(s, x, y)，按照下标x和y，对字符串进行切片
· file_util.py(文件处理相关工具，内含：)
    · 函数：print_file_info(file_name)，接收传入文件的路径，打印文件的全部内容，如文件不存在则捕获异常，输出提示信息，通过finally关闭文件对象
    · 函数：append_to_file(file_name, date)，接收文件路径以及传入数据，将数据追加写入到文件中

构建出包后，尝试着用一用自己编写的工具包
"""
import my_utils.str_util
from my_utils import file_util
print(my_utils.str_util.str_reverse("味精和楠楠！！"))
print(my_utils.str_util.substr("hello world", 6, 8))

file_util.append_to_file(r"E:\python练习\python学习\第九章 异常、模块与包\1.9.8 异常、模块、包_练习\test.txt", "味精大大！！！\n")
file_util.print_file_info(r"E:\python练习\python学习\第九章 异常、模块与包\1.9.8 异常、模块、包_练习\test.txt")
