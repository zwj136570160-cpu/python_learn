"""
- 目标
1. 能够通过json模块对数据进行处理
"""
import json

# 处理数据
with open(r"E:\python练习\python学习\第十章 python基础综合案例（数据可视化-折线图可视化）\1.10.5 数据准备\折线图数据\美国.txt", "r", encoding="utf-8") as f_us:
    us_read = f_us.read() # 读取文件的全部内容
#   去掉不合json规范的开头
us_read = us_read.replace("jsonp_1629344292311_69436(", "")
#   去掉不合json规范的结尾
us_data = us_read[:-2]
#   json转python字典
us_data = json.loads(us_data)
#   获取trend key
trend_data = us_data["data"][0]["trend"]
#   获取日期数据，用于x轴，取2020年（到314的下标结束）
x_data = trend_data["updateDate"][:314]
#   获取确认数据，用于y轴，取2020年（到314的下标结束）
y_confirmed_data = trend_data["list"][0]["data"][:314]


