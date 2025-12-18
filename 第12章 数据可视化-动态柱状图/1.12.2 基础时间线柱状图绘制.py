"""
- 目标
1. 掌握基础的时间线配置动态图表
2. 掌握设置主题更改颜色样式
"""
from pyecharts.globals import ThemeType
from pyecharts.options import LabelOpts
from pyecharts.charts import Bar, Timeline

"""
- 创建时间线
Timeline() - 时间线
柱状图描述的是分类数据，回答的是每一个分类中“有多少？”这个问题，这是柱状图的主要特点，同时柱状图很难动态的描述一个趋势性的数据吗，这里pyecharts为我们提供了一种解决方式-时间线

如果说一个Bar、Line对象是一张图表的话，时间线就是创建一个一维的x轴，轴上每一个点就是一个图表对象
"""
#   图表1
bar_1 = Bar().add_xaxis(
    ["中国", "美国", "英国"]
).add_yaxis(
    "GDP",
    [30, 20, 10],
    label_opts=LabelOpts(position="right"),
).reversal_axis()

#   图表2
bar_2 = Bar().add_xaxis(
    ["中国", "美国", "英国"]
).add_yaxis(
    "GDP",
    [50, 30, 20],
    label_opts=LabelOpts(position="right"),
).reversal_axis()

#   生成时间轴
timeline = Timeline(
    #   主题
    {"theme": ThemeType.LIGHT}
).add(
    bar_1, "2021年GDP"
).add(
    bar_2, "2022年GDP"
    #   用时间轴绘图
).add_schema(
    play_interval=1000, #   跳动的间隔
    is_timeline_show=True, #    是否显示时间线
    is_auto_play=True, #    是否自动播放
    is_loop_play=True # 是否循环播放
).render("基础柱状图-时间线.html")

