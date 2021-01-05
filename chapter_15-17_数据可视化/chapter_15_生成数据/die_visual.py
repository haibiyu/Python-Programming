# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : die_visual.py
# Time       ：2020/11/11 14:56 
# Author     ：Yolanda Yan
# version    ：python 3.6
# Description：
"""

from die import Die
import pygal

# 创建一个D6
die = Die()

# 掷几次骰子，将结果保存在一个列表中
results =[die.roll() for roll_num in range(1000)]

# 分析结果
frequencies =[results.count(value) for value in range(1,die.num_sides+1)]
print(frequencies)

# 对结果进行可视化
hist = pygal.Bar()  # 绘制直方图

hist.title = "Results of rolling one D6 1000  times."
hist.x_labels = list(range(1,die.num_sides+1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6",frequencies)  # 将一系列值添加到图表中,给添加的值制定标签‘D6’
hist.render_to_file("./result/die_visual.svg")  # 将这个图表渲染为一个SVG文件




