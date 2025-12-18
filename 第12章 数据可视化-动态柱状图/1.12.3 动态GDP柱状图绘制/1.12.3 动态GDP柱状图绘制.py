#   读取数据
from pyecharts.charts import Bar, Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import LabelOpts, TitleOpts

with open(r"E:\python练习\python学习\第12章 数据可视化-动态柱状图\1.12.3 动态GDP柱状图绘制\1960-2019全球GDP数据.csv", "r", encoding="GB2312") as f:
    data_lines = f.readlines()
#   删除第一条数据
data_lines.pop(0)
#   定义一个空字典
data_dict = {}
#   将数据转换为字典存储
for line in data_lines:
    year = int(line.split(",")[0])
    country = line.split(",")[1]
    gdp = float(line.split(",")[2])
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])
#   生成时间轴
timeline = Timeline(
    #   主题颜色
    {"theme": ThemeType.LIGHT}
)
#   排序年份
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    year_data = data_dict[year][:8]
    x_data = []
    y_data = []
    for country_dgp in year_data:
        x_data.append(country_dgp[0]) # x轴添加国家
        y_data.append(country_dgp[1] // 100000000) # y轴添加GDP
    x_data.reverse()
    y_data.reverse()
    bar = (
        Bar()
        .add_xaxis(x_data)
        .add_yaxis(
            "GDP(亿)",
            y_data,
            label_opts=LabelOpts(position="right")
        )
        #   反转x轴和y轴
        .reversal_axis()
    )
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前8GDP数据")
    )
    (timeline
     .add(bar, str(year))
     .add_schema(
        play_interval=500, #   跳动的间隔
        is_timeline_show=True,  # 是否显示时间线
        is_auto_play=True,  # 是否自动播放
        is_loop_play=True
    ).render("1960-2019全球GDP前8国家.html")
     )
