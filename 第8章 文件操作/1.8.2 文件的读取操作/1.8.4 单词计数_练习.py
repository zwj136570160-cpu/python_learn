"""
- 单词计数
通过windows的文本编辑器软件，将如下内容，复制并保存到：word.txt文件可以存储在任意位置
itheima itcast python
itheima python itcast
beijing shanghai itheima
shenzhen guangzhou itheima
wuhan hangzhou itheima
zhengzhou bigdata itheima

通过文件读取操作，读取此文件，统计itheima单词出现的次数
"""

# 方法1：使用字符串的方法count统计次数
with open(r"E:\python练习\python学习\第8章 文件操作\1.8.2 文件的读取操作\word.txt", "r", encoding="utf-8") as f:   # 在路径前面加r可以把路径改成原始字符串，让python不解析转义符，避免报错，使用with open语法 打开文本
    result = f.read()   # 使用read读取整个文本的内容
    print(type(result)) # 判断count文件类型，判断结果为str(字符串)
    count_num = result.count("itheima") # 使用字符串方法count统计itheima在文本中出现的次数，并赋值给count_num
    print(f"itheima在文件中出现的次数为：{count_num}次") # 输出

# 方式2：读取内容，一行一行读取
    count = 0 # 使用count计算itheima出现的次数
    for line in f:
        line = line.strip()  # 去除开头和结尾的空格以及换行符
        list_new = line.split(" ")
        print(list_new)
        for word in list_new:
            if word == "itheima":
                count += 1
    print(f"itheima在文件中出现的次数为：{count}次")




