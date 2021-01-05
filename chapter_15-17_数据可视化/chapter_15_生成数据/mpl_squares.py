# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : mpl_squares.py
# Time       ：2020/11/9 9:46 
# Author     ：Yolanda Yan
# version    ：python 3.6
# Description：
"""

import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_values, squares, linewidth=5)  # linewidth:绘制的线条的粗细

# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both',labelsize=14)

plt.show()



# 设置图表标题，并给坐标轴加上标签