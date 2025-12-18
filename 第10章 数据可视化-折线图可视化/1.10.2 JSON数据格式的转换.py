"""
- 目标：
1. 知道什么是json
2. 掌握如何使用json进行数据转化
"""

"""
- 什么是json
· json是一种轻量级的数据交互格式，可以按照json指定的格式去组织和封装数据
· json本质上是一个带有特定格式的字符串
· 主要功能：json就是一种在各个编程语言中流通的数据格式，负责不同编程语言中的数据传递和交互，类似于：
    ① 国际通用语言-英语
    ②中国56哥名族不同地区的通用语言-普通话

- json有什么用
各类编程语言存储数据的容器不尽相同，在python中有字典（dict）这样的数据类型，而其他语言可能没有对应的字典
为了让不同语言都能够相互通用的互相传递数据，json就是一种非常良好的中转数据格式

· 以python和C语言互传数据为例：
    python格式数据 → json格式数据 → C语言程序接收json格式数据并转化为C语言数据继续使用
    C格式数据 → json格式数据 → python语言程序接收json格式数据并转化为python格式数据继续使用
"""

"""
- json格式数据转化
json格式的数据要求很严格，以下代码为要求

json数据的格式可以是：
{"name": "admin", "age": 18}
也可以是：
[{"name": "admin", "age": 18}, {"name": "root", "age": 16}, {"name": "张三", "age": 20}]
"""

"""
- python数据和json数据的相互转化
"""
# 导入json模块
import json
# 准备符合json格式要求的python数据
data = [
    {
        "name": "张大三", "age": 11
    }, {
        "name": "王大锤", "age": 13
    }, {
        "name": "赵啸虎", "age": 16
    }
]
# 通过json.dumps()方法把python数据转化为了json数据
data_str = json.dumps(data, ensure_ascii = False) # ensure_ascii = False 如字典中包含中文，需要传ensure_ascii的参数并设置为False，意思为：不使用ascii码转化它，如设置为True中文就会转换为unicode的字符
print(type(data_str)) # 查看data_str的数据类型
print(data_str) #   打印data_str的内容

# 准备字典，将字典转换为json
dict_data = {
    "name": "小王",
    "addr": "上海"
}
json_str = json.dumps(dict_data, ensure_ascii = False)
print(type(json_str)) # 查看json_str的数据类型
print(json_str) #   打印json_str的内容

# 通过json.loads()方法把json数据转化为了python
data2 = ('[{'
         '  "name": "张大三", "age": 11'
         '}, {'
         '  "name": "王大锤", "age": 13'
         '}, {'
         '  "name": "赵啸虎", "age": 16'
         '}]')
l = json.loads(data2)
print(type(l))
print(l)

# 将json字符串转换为python数据类型
s = ('{'
     '"name": "周杰伦",'
     '"addr": "台北"'
     '}')
d = json.loads(s)
print(type(d))
print(d)

"""
- 总结：
1. json：是一种轻量级的数据交互格式，采用完全独立于编程语言的文本格式来存储和表示数据（就是字符串）
python语言使用json有很大优势，因为：json无非就是一个单独的字典或一个内部元素都是字典的列表
所以json可以直接和python的字典或列表进行无缝转换
2. json格式数据化
· 通过json.dumps()方法把python数据转化为了json数据
    data = json.dumps()
    如果有中文可以带上：ensure_ascii =False参数来确保中文正常转换
· 通过json.loads()方法把json数据转化为了python列表或字典
    data = json.loads()
"""

