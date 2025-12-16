"""
- 目标
1. 了解什么是第三方包
2. 掌握只用pip安装第三方包
"""

"""
- 什么是第三方包
包可以包含一堆python模块，而每个模块又内含许多的功能
我们可以认为：一个包，就是一堆同类型功能的集合体

在python程序的生态中，有许多非常多的第三方包（非python官方），可以极大的帮助我们提高开发效率，如：
· 科学计算中常用的：numpy包
· 数据分析中常用的：pandas包
· 大数据计算中常用的：pyspark、apache-flink包
· 图形可视化常用的：matplotlib、pyecharts
· 人工智能常用的：tensorflow
· 等

这些第三方包，极大丰富python的生态，提高了开发效率
但是由于是第三方，所以python没有内置，所以我们需要安装他们才可以导入使用
"""

"""
- 安装第三方包 - pip
第三方包的安装费用简单，我们只需要使用python内置的pip程序即可
pip install 包名称
即可通过网络快速安装第三方包
"""

"""
- pip的网络优化
由于pip是连接的国外的网站进行包的下载，所以有的时候会速度很慢
我们可以通过如下命令，让其链接国内的网站进行包的安装
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple
https://pypi.tuna.tsinghua.edu.cn/simple是清华大学提供的一个网址，可供pip程序下载第三方包
"""

"""
- 安装第三方包 - pycharm
pycharm也提供了安装第三方包的功能
"""

"""
- 总结
1. 什么是第三方包，有什么作用？
第三方包就是非python官方内置的包，可以安装他们的扩展功能，提高开发效率
2. 如何安装？
· 在命令提示符（cmd）：
    · pip install 包名称
    · pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名称
· 在pycharm中安装
"""
