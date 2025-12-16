"""
- 追加写入操作快速入门
1. 打开文件，通过a模式打开即可
f = open("文件名", "a")
2. 文件写入
f.write("hello world")
3. 文件刷新
f.flush()
注意：
· a模式，文件不存在会创建文件
· a模式，文件存在会在最后，追加写入文件
"""
# 打开文件，不存在文件
f = open(r"E:\python练习\python学习\第8章 文件操作\1.8.5 文件的追加写入操作\1.8.5 测试文件.txt", "a", encoding="utf-8")
# write写入
f.write("hello world")
# flush刷新
f.flush()
# close关闭
f.close()
# 打开一个存在的文件
f = open(r"E:\python练习\python学习\第8章 文件操作\1.8.5 文件的追加写入操作\1.8.5 测试文件.txt", "a", encoding="utf-8")
# write写入，flush刷新
f.write("\n味精顶瓜瓜")
f.flush()
# close关闭
f.close()

"""
- 总结
1. 追加写入文件使用open函数的'a'模式进行写入
2. 追加写入的方法有（和w模式一致）
· write(),写入内容
· flush(),刷新内容到硬盘中
3. 注意事项
· a模式，文件不存在，会创建新文件
· a模式，文件存在，会在原有内容后面继续写入
· 可以是'\n'来写出换行符
"""