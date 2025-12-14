"""
- 目标
1. 能够通过json模块对数据进行处理
2. 通过pycharts完成疫情折线图
"""
from data_processing_tool import util

#   印度的数据处理
util.dp(
    fp=r"E:\python练习\python学习\第十章 python基础综合案例（数据可视化-折线图可视化）\1.10.5(6) 数据准备\折线图数据\印度.txt",
    no_json="jsonp_1629350745930_63180(",
    index=-2,
    date_idx=269,
    data_idy=269,
    state="印度"
)

#   日本的数据处理
util.dp(
    fp=r"E:\python练习\python学习\第十章 python基础综合案例（数据可视化-折线图可视化）\1.10.5(6) 数据准备\折线图数据\日本.txt",
    no_json="jsonp_1629350871167_29498(",
    index=-2,
    date_idx=315,
    data_idy=315,
    state="日本"
)

#   美国的数据处理
util.dp(
    fp=r"E:\python练习\python学习\第十章 python基础综合案例（数据可视化-折线图可视化）\1.10.5(6) 数据准备\折线图数据\美国.txt",
    no_json="jsonp_1629344292311_69436(",
    index=-2,
    date_idx=314,
    data_idy=314,
    state="美国"
)