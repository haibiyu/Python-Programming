# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : scatter_squares.py
# Time       ：2020/11/10 16:03 
# Author     ：Yolanda Yan
# version    ：python 3.6
# Description：
"""

import matplotlib.pyplot as plt

# # 绘制一个散点图
# plt.scatter(2,4,s=200)
# # 设置图表标题，并给坐标轴加上标签
# plt.title("Square Numbers",fontsize=24)
# plt.xlabel("Value",fontsize=14)
# plt.ylabel("Square of Value",fontsize=14)
#
# # 设置刻度标记的大小
# plt.tick_params(axis='both',which='major',labelsize=14)
# plt.show()

# # 绘制多个散点图
# x_values = [1,2,3,4,5]
# y_values = [1,4,9,16,25]
# plt.scatter(x_values, y_values, s=100)  # s:点的大小
# # 设置图表标题，并给坐标轴加上标签
# plt.title("Square Numbers",fontsize=24)
# plt.xlabel("Value",fontsize=14)
# plt.ylabel("Square of Value",fontsize=14)
#
# # 设置刻度标记的大小
# plt.tick_params(axis='both',labelsize=14)
#
# plt.show()

# 自动计算数据
x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]
# 散点默认为蓝色点和黑色轮廓，edgecolors='None':删除数据点的轮廓
# c:定义数据点的颜色,c='red'为红色，
# plt.scatter(x_values,y_values,c='red',edgecolors='None',s=40)

# # c=(0,0,0.8)：分别表示红色、绿色和蓝色分量，均为0~1之间的小数值，值越接近0，指定的颜色越深，值越接近1，指定的颜色越浅
# plt.scatter(x_values,y_values,c=(0,0,0.8),edgecolors='None',s=40)

# 使用颜色映射colormap,根据每个点的y值来设置其颜色
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
            edgecolors='None', s=40)

# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])
# 保存图表
plt.savefig("./result/squares_plots.png", bbox_inches='tight')

# plt.show()
