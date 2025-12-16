"""
演示河南省疫情可视化开发
"""
import json

from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts, TitleOpts

#   读取数据
with open(r"/第11章 数据可视化-地图可视化/疫情.txt", "r", encoding="utf-8") as f:
    data = f.read()
#   将json文件转换为json
data = json.loads(data)
#   取到河南省数据
hen_data_list = data["areaTree"][0]["children"][3]["children"]

#   组装每个市和确诊人数为元组，并将各个市的数据封装至列表内
hen_data = [] # 绘图所需数据
for hen in hen_data_list:
    hen_name = hen["name"] + "市"
    hen_confirm = hen["total"]["confirm"]
    hen_data.append((hen_name, hen_confirm))
#   手动添加济源市数据
hen_data.append(("济源市", 5))
#   创建地图对象
hen_epidemic_map = (
    Map()
    #   添加数据
    .add(
        series_name="各市区确诊人数",
        data_pair=hen_data,
        maptype="河南"
    )
    #   设置全局选项
.set_global_opts(
        title_opts=TitleOpts(
            title="河南省疫情地图"
        ),
        visualmap_opts=VisualMapOpts(
            is_show=True, # 是否显示
            is_piecewise=True, # 是否分段
            pieces=[
                {"min": 1, "max": 10, "label": "1-10", "color": "#CCFFFF"},
                {"min": 11, "max": 100, "label": "10-100", "color": "#FFFF99"},
                {"min": 101, "max": 200, "label": "101-200", "color": "#CC3333"},
                {"min": 201, "max": 300, "label": "201-300", "color": "#6b0014"}
            ]
        )
    )
    .render("1.11.3河南省疫情地图.html")
)


