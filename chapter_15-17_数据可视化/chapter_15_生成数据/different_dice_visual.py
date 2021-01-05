# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : different_dice_visual.py
# Time       ：2020/11/11 15:26 
# Author     ：Yolanda Yan
# version    ：python 3.6
# Description：
"""
from die import Die
import pygal

# 创建一个D6和一个D10
die_1 = Die()
die_2 = Die(10)

# 掷几次骰子，将结果保存在一个列表中
results =[die_1.roll()+die_2.roll() for roll_num in range(50000)]

# 分析结果
max_num = die_1.num_sides + die_2.num_sides
frequencies =[results.count(value) for value in range(2, max_num + 1)]
print(frequencies)

# 对结果进行可视化
hist = pygal.Bar()  # 绘制直方图

hist.title = "Results of rolling a D6 and a D10 50000  times."
hist.x_labels = list(range(2, max_num + 1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6+D10", frequencies)  # 将一系列值添加到图表中,给添加的值制定标签‘D6’
hist.render_to_file("./result/different_dice_visual.svg")  # 将这个图表渲染为一个SVG文件
