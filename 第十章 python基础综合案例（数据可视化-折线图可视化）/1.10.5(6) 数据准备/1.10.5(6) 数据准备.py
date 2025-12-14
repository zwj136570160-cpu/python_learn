"""
- 目标
1. 能够通过json模块对数据进行处理
2. 通过pycharts完成疫情折线图
"""
from data_processing_tool import util
from pyecharts.charts import Line

# import json
#
# # 处理数据
# with open(r"E:\python练习\python学习\第十章 python基础综合案例（数据可视化-折线图可视化）\1.10.5(6) 数据准备\折线图数据\美国.txt", "r", encoding="utf-8") as f_us:
#     us_read = f_us.read() # 读取美国的全部内容
#
# with open(r"E:\python练习\python学习\第十章 python基础综合案例（数据可视化-折线图可视化）\1.10.5(6) 数据准备\折线图数据\日本.txt", "r", encoding="utf-8") as f_jp:
#     jp_read = f_jp.read() # 读取日本的全部内容
#
# with open(r"E:\python练习\python学习\第十章 python基础综合案例（数据可视化-折线图可视化）\1.10.5(6) 数据准备\折线图数据\印度.txt", "r", encoding="utf-8") as f_in:
#     in_read = f_in.read() # 读取印度的全部内容
# #   去掉不合json规范的开头
# us_read = us_read.replace("jsonp_1629344292311_69436(", "")
# jp_read = jp_read.replace("jsonp_1629350871167_29498(", "")
# in_read = in_read.replace("jsonp_1629350745930_63180(", "")
# #   去掉不合json规范的结尾
# us_data = us_read[:-2]
# jp_data = jp_read[:-2]
# in_data = in_read[:-2]
# #   json转python字典
# us_data = json.loads(us_data)
# jp_data = json.loads(jp_data)
# in_data = json.loads(in_data)
# #   获取trend key
# us_trend_data = us_data["data"][0]["trend"]
# jp_trend_data = jp_data["data"][0]["trend"]
# in_trend_data = in_data["data"][0]["trend"]
# #   获取日期数据，用于x轴，取2020年（到314的下标结束）
# us_x_data = us_trend_data["updateDate"][:314]
# jp_x_data = jp_trend_data["updateDate"][:315]
# in_x_data = in_trend_data["updateDate"][:269]
# #   获取确认数据，用于y轴，取2020年（到314的下标结束）
# us_y_data = us_trend_data["list"][0]["data"][:314]
# jp_y_data = jp_trend_data["list"][0]["data"][:315]
# in_y_data = in_trend_data["list"][0]["data"][:269]


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