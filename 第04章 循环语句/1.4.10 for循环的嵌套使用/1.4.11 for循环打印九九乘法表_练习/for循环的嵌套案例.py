# 练习案例for循环打印九九乘法表
from ipaddress import summarize_address_range

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j} * {i} = {i * j}\t", end="")

    print()
print()

for i in range(1,10):
    j = i
    while j <= 9:
        print(f"{i} * {j} = {i * j}\t", end='')
        j += 1
    print()







