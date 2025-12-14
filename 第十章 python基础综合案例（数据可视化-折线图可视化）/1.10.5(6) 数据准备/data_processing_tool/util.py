"""
此功能包仅限1.10.5（6）处理折线图数据使用
"""
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts

#   得到折线图对象
Line = Line()
def dp(fp, no_json, index, date_idx, data_idy, state):
    """
    数据处理流程：读取→处理json数据→json转python→获取数据
    :param fp: 文件路径地址(E:\python练习\python学习\第十章 python基础综合案例（数据可视化-折线图可视化）\1.10.5(6) 数据准备\折线图数据\美国.txt)
    :param no_json: 需要处理的json内容(jsonp_1629344292311_69436()
    :param index: 对符合json规范的内容进行切片下标(-2)
    :param date_idx: 日期数据下标(314)
    :param data_idy: 确诊数据下标(314)
    :param state: 确诊国家名称（美国）
    :return: None
    """
    #   读取文件
    with open(fp, "r", encoding="utf-8") as f:
        f_read = f.read()

    #   替换不合法JSON开头
    f_read = f_read.replace(no_json, "")

    #   去掉不合json规范的结尾
    f_data = f_read[:index]

    #   将json文件转化为python字典
    f_data = json.loads(f_data)

    #   获取trend key
    f_trend_data = f_data["data"][0]["trend"]

    #   获取日期数据,用于x轴
    f_x_data = f_trend_data["updateDate"][:date_idx]
    Line.add_xaxis(f_x_data)

    #   获取确诊数据，用于y轴
    f_y_data = f_trend_data["list"][0]["data"][:data_idy]
    Line.add_yaxis(
        f"{state}确诊人数",
                   f_y_data,
                   label_opts=LabelOpts(
                       is_show=False
                   )
    )

    #   设置全局选项
    Line.set_global_opts(
        title_opts=TitleOpts(
            title="2020年美日印三国确诊人数对比折线图",
            pos_left="center",
            pos_bottom="1%"
        ),
    )
    #   生成图标
    Line.render()

if __name__ == "__main__":
    dp(
        fp=r"E:\python练习\python学习\第十章 python基础综合案例（数据可视化-折线图可视化）\1.10.5(6) 数据准备\折线图数据\美国.txt",
        no_json="jsonp_1629344292311_69436(",
        index=-2,
        date_idx=314,
        data_idy=314,
        state="美国"
    )