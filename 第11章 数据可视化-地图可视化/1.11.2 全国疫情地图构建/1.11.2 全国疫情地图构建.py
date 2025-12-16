"""
演示全国疫情可视化地图开发
"""
import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts, TitleOpts

#   读取数据文件
with open(
    file=r"E:\python练习\python学习\第11章 数据可视化-地图可视化\1.11.2 全国疫情地图构建\疫情.txt",
    mode="r",
    encoding="utf-8"
) as f:
    data = f.read()
#   取到各省数据
#   将字符串json转换为python的字典
data = json.loads(data)
#   从字典中取出各个省份的数据
province_data_list = data["areaTree"][0]["children"]
#   组装每个省份和确诊人数为元组，并各个省的数据都封装入列表内
data_list = [] #    绘图需要使用的数据
for province_data in province_data_list:
    province_name = province_data["name"] # 省份名称
    #   使用any()方法判断province_name结尾是否包含有"省", "市", "自治区", "特别行政区"，如没有可直接加上
    no_need_suffix = ["省", "市", "自治区", "特别行政区"]
    if not any(province_name.endswith(suffix) for suffix in no_need_suffix):
        province_name += "省"
        #   单独把特殊区域名字拿出来进行处理
        if province_name in ["北京省", "天津省", "重庆省"]:
            province_name = province_name.replace("省", "市")
        elif province_name in ["香港省", "澳门省"]:
            province_name = province_name.replace("省", "特别行政区")
        elif province_name in ["西藏省", "内蒙古省"]:
            province_name = province_name.replace("省", "自治区")
        elif province_name in ["宁夏省"]:
            province_name = province_name.replace("省", "回族自治区")
        elif province_name in ["广西省"]:
            province_name = province_name.replace("省", "壮族自治区")
        elif province_name in ["新疆省"]:
            province_name = province_name.replace("省", "维吾尔自治区")
    province_confirm = province_data["total"]["confirm"] #  确证人数
    data_list.append((province_name, province_confirm))
#   创建地图对象
epidemic_map = (
    Map()
    #   添加数据
    .add(
        series_name="各省份确诊人数",
        data_pair=data_list,
        maptype="china"
    )
    #   设置全局配置
    .set_global_opts(
        title_opts=TitleOpts(
            title="全国疫情地图"
        ),
        visualmap_opts=VisualMapOpts(
            is_show=True, # 是否显示
            is_piecewise=True, # 是否分段
            pieces=[
                {"min": 1, "max": 99, "label": "1-99", "color": "#CCFFFF"},
                {"min": 100, "max": 999, "label": "100-999", "color": "#FFFF99"},
                {"min": 1000, "max": 4999, "label": "1000-4999", "color": "#FF9966"},
                {"min": 5000, "max": 9999, "label": "5000-9999", "color": "#FF6666"},
                {"min": 10000, "max": 9999, "label": "10000-9999", "color": "#CC3333"},
                {"min": 10000, "label": "> 100000", "color": "#6b0014"}
            ]
        )
    )
    .render("全国疫情地图.html")
)
