"""
- 目标：掌握使用continue和break关键字控制循环

- 思考：无论while循环或者是for循环，都是重复性的执行特性操作
在这个重复的过程中，会出现一些其他情况让我们不得不：
· 暂时跳过某次循环，直接进行下一次
· 提前推出循环，不在继续
对于这种场景，python提供continue和break关键字，用以对循环进行临时跳过和直接结束

- continue
continue关键字用于：中断本次循环，直接进入下一次循环
continue可以用于：for循环和while循环，效果一致
语句格式：
for i in range(1,100):
    语句1
    continue
    语句2

以上代码：
· 在循环内，遇到continue就结束当此循环，进行下一次
· 所以，语句2是不会执行的。

应用场景：
在循环中，因某些原因，临时结束本次循环。
"""

# 演示循环中断语句continue
for i in range(1,6):
    print("语句1")
    continue
    print("语句2")

"""
- continue在嵌套循环中的应用
continue关键字只可以控制：他所在的循环临时中断
for i in range(1,100): # 2
    语句1
    for j in range(1,100): # 1
        语句2
        continue
        语句3
        
    语句4
"""

# 演示continue的嵌套应用
for i in range(1,6):
    print("语句1")
    for j in range(1,6):
        print("语句2")
        continue
        print("语句3")

    print("语句4")

"""
- break
break关键字用于：直接结束循环
break可以用于：for循环和while循环，效果一致
语句格式：
for i in range(1,100):
    语句1
    break
    语句2
    
语句3

以上代码：
· 在循环内，遇到break就结束循环了
· 所以，执行了语句1后，直接执行语句3了
"""

# 演示循环中断语句break
for i in range(1,101):
    print("语句1")
    break
    print("语句2")

print("语句3")

"""
- break在嵌套循环中的应用
break关键词同样只可以控制：他所在的循环结束
语句格式：
for i in range(1,100): # 2
    语句1
    for j in range(1,100): # 1
    break
    语句3
    
语句4
"""

# 演示break的嵌套应用
for i in range(1,6):
    print("语句1")
    for j in range(1,6):
        print("语句2")
        break
        print("语句3")

    print("语句4")

"""
- 总结：
1.continue的作用是：
中断所在循环的当此执行，直接进入下一次
2.break的作用是：
直接结束所在的循环
3.注意事项：
· continue和break，在for和while循环中作用一致
· 在嵌套循环中，只能作用在所在的循环上，无法对上层循环起作用
"""



