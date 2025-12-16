"""
- 目标
1. 掌握使用pyecharts构建基础的全国地图可视化图表
"""

from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

#   准备数据
data = [
    ("北京市",99),
    ("上海市",199),
    ("湖南省",299),
    ("台湾省",399),
    ("广东省",499)
]
my_map = (
    Map()
    #   添加数据
    .add(
        series_name="测试地图",
        data_pair=data,
        maptype="china"
    )
    #   设置全局选项
    .set_global_opts(
        visualmap_opts=VisualMapOpts(
            is_show=True,
            is_piecewise=True,
            pieces=[
                {"min": 1, "max": 9, "label": "1-9", "color": "#CCFFFF"},
                {"min": 10, "max": 99, "label": "10-99", "color": "#FF6666"},
                {"min": 100, "max": 500, "label": "100-500", "color": "#990033"}
            ]
        )
    )
    #   绘图
    .render(
        path="1.11.1测试地图.html"
    )
)