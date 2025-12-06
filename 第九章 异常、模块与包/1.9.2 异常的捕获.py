"""
- 目标
1. 知道为什么要捕获异常
2. 掌握捕获异常的语法格式
"""

"""
- 为什么要捕获异常
世界上没有完美的程序，任何程序在运行的过程中，都有可能出现：异常（bug），导致程序无法完美运行下去
我们要做的，就是在力所能及的范围内，对bug进行提前准备、提前处理
这种行为我们称之为：异常处理（捕获异常）

当我们的程序遇到了bug，那么接下来有两种情况
① 整个程序因为一个bug停止运行
② 对bug进行提醒，整个程序继续运行
显然在之前的学习中，我们所有的程序遇到bug就会出现①的情况，也就是整个程序直接崩溃
但是在真实工作中，我们肯定不能因为一个小的bug就让整个程序全部崩溃，也就是我们希望的是达到②的这种情况
那这里我们就需要使用到捕获异常

捕获异常的作用在于：提前假设某处会出现异常，做好提前准备，当真的出现异常的时候，可以有后续手段
"""

"""
- 捕获常规异常
基本语法：
try:
    可能发生错误的代码
except:
    如果出现异常执行的代码
"""
# 快速入门
# 需求：尝试以"r"模式打开文件，如果文件不存在，则以"w"方式打开
try:
    f = open(r"E:\python练习\python学习\第九章 异常、模块与包\tset.txt","r", encoding="utf-8")
except:
    print("出现异常了，因为tset文件不存在，我将open的模式，改为w模式去打开")
    f = open(r"E:\python练习\python学习\第九章 异常、模块与包\tset.txt","w", encoding="utf-8")

"""
- 基本语法
try:
    print(name)
except:
    print("name变量名称未定义错误")
注意：
① 如果尝试执行的代码的异常类型和要捕获的异常类型不一致，则无法捕获异常
② 一般try下方只放一行尝试执行的代码
"""
# 捕获多个异常
# try:
#     print(name)
#     # 1 / 0
# except NameError as e:
#     print("出现了变量未定义的异常")
#     print(e)

# 当捕获多个异常时，可以把要捕获的异常类型的名字，放到except后，并使用元组的方式进行书写
try:
    print(name)
    1 / 0
except(ZeroDivisionError, NameError) as e:
    print("出现了变量未定义或者除以0的异常错误")

# 捕获全部异常
try:
    1 / 0
    print(name)
except Exception as e:
    print("出现异常了")

"""
- 异常else
else表示的是如果没有异常要执行的代码
"""
try:
    open(r"E:\python练习\python学习\第九章 异常、模块与包\tset.txt", "r", encoding="utf-8")
except Exception as e:
    print("出现异常了")
else:
    print("没有异常！")

"""
- 异常的finally
finally表示的是无论是否异常都要执行的代码，例如关闭文件：
"""
global f # 声明f为全局变量
try:
    f = open(r"E:\python练习\python学习\第九章 异常、模块与包\tset.txt", "r", encoding="utf-8")
except Exception as e:
    print("出现异常了")
    f = open(r"E:\python练习\python学习\第九章 异常、模块与包\tset.txt", "w", encoding="utf-8")
else:
    print("没有异常！")
finally:
    print("我是finally，有没有异常我都要执行")
    f.close()

"""
- 总结
1. 为什么要捕获异常？
在可能发生异常的地方，进行捕获，当异常出现的时候，提供解决方式，而不是任由其导致异常无法运行
2. 捕获异常的语法
try:
    可能要发生异常的语句
except 异常 as 别名:
    出现异常的准备手段 
else:  可选
    未出现异常时应做的事情
finally:  可选
    不管出不出现异常都会做的事情
3. 如何捕获所有异常
异常的种类多种多样，如果想要不管什么类型的异常都能捕获刀，那么使用
· except:
· except Exception:
两种方式都可以捕获所有异常
"""

