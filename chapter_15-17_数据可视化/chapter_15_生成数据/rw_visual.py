# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : rw_visual.py
# Time       ：2020/11/11 11:40 
# Author     ：Yolanda Yan
# version    ：python 3.6
# Description：将随机漫步的所有点都绘制出来
"""

import matplotlib.pyplot as plt

from random_walk import RandomWalk

import warnings

warnings.filterwarnings("ignore")  # 忽略警告

# 只要程序处理活动状态，就不断的模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk()  # 增加点数,由默认5000增加到50000
    rw.fill_walk()

    # 设置绘图窗口尺寸
    plt.figure(figsize=(10, 6))

    # 绘制散点图，用颜色映射指出漫步中各点的先后顺序，并删除点的黑色轮廓，让数据点颜色更明显
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolors='None', s=15)

    # plt.plot(rw.x_values, rw.y_values, linewidth=3)  # 运动轨迹

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='None', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='None',
                s=100)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break
