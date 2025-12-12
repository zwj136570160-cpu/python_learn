"""
- 目标
1. 构建一个基础的折线图
2. 使用全局配置项设置属性
"""


"""
- pyecharts入门
· 基础折线图
"""

"""
- pyecharts有哪些配置选项
· 全局配置选项
· 系列配置选项
"""

"""
set_global_opts方法
· 这里全局配置选项可以通过set_global_opts方法来进行配置，相应的选项和选项的功能可以参考1.10.4 set_global_opts示例图
· 系列配置项，我们在后面构建案例时讲解
"""
# 导包，导入line功能构建折线图对象
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts
from pyecharts.charts import Bar

# 得到折线图对象
Line = Line()
# 添加x轴数据
Line.add_xaxis(["中国", "美国", "英国"])
# 添加y轴数据
Line.add_yaxis("GDP", [10, 20, 30])
# 设置全局配置项
Line.set_global_opts(
    title_opts=TitleOpts(
        title="GDP展示",
        pos_left="center",
        pos_bottom="1%"
    ),
    legend_opts=LegendOpts(
        is_show=False
    ),
    toolbox_opts=ToolboxOpts(
        is_show=True
    ),
    visualmap_opts=VisualMapOpts(
        is_show=True
    )
)
# 生成图表
Line.render()

"""
- 总结
1. pyecharts模块有很多的配置选项，常用刀三个类别的选项：
    · 全局配置选项
    · 系列配置选项
2. 全局配置项能做什么？
    · 配置图标的标题
    · 配置图例
    · 配置鼠标移动效果
    · 配置工具栏
    · 等整体配置项
"""




