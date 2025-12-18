"""
- 案例效果
通过pyecharts可以实现数据的动态显示，直观的感受1960-2019年全世界各国GDP的变化趋势
具体效果可参考文件 1.12.1效果

- 目标
1. 掌握构建一个基础的柱状图并能够反转x和y轴
"""

from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

bar = Bar()
    #   添加x轴数据
(bar.add_xaxis(
    ["中国", "美国", "英国"]
    #   添加y轴数据
).add_yaxis(
    "GDP", [30, 20, 10],
    itemstyle_opts={"color": "#FF0000"},
    label_opts=LabelOpts(
        position="right"
    )
) # 反转xy轴
 .reversal_axis()
 .render("1.12.1基础柱状图.html"))

"""
- 总结
1. 通过Bar()构建一个柱状图对象
2. 和折线图一样，通过add_xaxis()和add_yaxis()添加x和y轴数据
3. 通过柱状图对象的：reversal_axis()是，反转x和y轴
4. 通过label_opts=LabelOpts(position="right")设置数值标签在右侧显示
"""