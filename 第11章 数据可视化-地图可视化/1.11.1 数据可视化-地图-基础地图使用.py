"""
- 目标
1. 掌握使用pyecharts构建基础的全国地图可视化图表
"""

from pyecharts.charts import Map
my_map = Map()
data = [
    ("北京",99),
    ("上海",199),
    ("湖南",299),
    ("台湾",399),
    ("广东",499)
]
my_map.add(series_name="测试", data_pair=data, maptype="china").render(path="测试地图")