"""
- 文件的写入操作
"""
import time

"""
- 写操作快速入门
"""
# 1.打开文件
f = open("文本使用.txt", "w", encoding="utf-8")
# 2.文件写入
f.write("hello world")
# 3.内容刷新
f.flush()
"""
- 注意
· 直接调用write，内容并为真正写入文件，而是会积攒在程序的内存中，称之为缓冲区
· 当调用flush的时候，内容会真正写入文件
· 这样做是避免频繁的操作硬盘，导致效率下降（攒一堆，一次性写硬盘）
"""

# 打开文件
f = open(r"E:\python练习\python学习\第8章 文件操作\1.8.3 文件写入操作\文本使用.txt", "w", encoding="utf-8")
# write写入
f.write("hello world")    # 内容写入到内存中
f.flush()     # 将内存中积攒的内容，写入到硬盘的文件中
# close关闭
f.close()    # close内置了flush的功能的
# 打开一个存在的文件
f = open(r"E:\python练习\python学习\第8章 文件操作\1.8.3 文件写入操作\文本使用.txt", "w", encoding="utf-8")
# write写入、flush刷新
f.write("味精金闪闪！！！")
# close关闭
f.close()

"""
- 总结
1. 写入文件使用open函数的‘w’模式进行写入
2. 写入的方法有
· write()，写入内容
· flush()，刷新内容到硬盘中
3. 注意事项
· w模式，文件不存在，会创建新文件
· w模式，文件存在，会清空原有内容
· close()方法，带有flush()方法的功能
"""