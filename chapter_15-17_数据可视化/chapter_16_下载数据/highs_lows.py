# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : highs_lows.py
# Time       ：2020/11/11 16:16 
# Author     ：Yolanda Yan
# version    ：python 3.6
# Description：
"""

import csv
import matplotlib.pyplot as plt
from datetime import datetime

# 从文件中获取日期、最高温度和最低温度
# filename = './data/sitka_weather_07-2014.csv'
# filename = './data/sitka_weather_2014.csv'
filename = './data/death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)  # 创建一个与该文件相关联的阅读器（reader）对象
    header_row = next(reader)  # 调用第一次，返回文件的第一行，即与天气有关的指标
    # print(header_row)

    # # 打印文件头及其位置
    # for index,column in enumerate(header_row):
    #     print(index,column)

    dates = []
    highs = []
    lows = []
    # 阅读器对象从其停留的地方继续往下读取CSV文件，每次都自动返回当前所处位置的下一行
    for row in reader:  # 遍历文件中余下的各行，由于上面已经读了头文件，剩下的从第二行开始
        try:
            current_date = datetime.strptime(row[0],'%Y-%m-%d')  # 将字符串转换为对应日期
            high = int(row[1])  # 索引1的位置为最高温度,将字符串转换为整数
            low = int(row[3])
        except ValueError:  # 针对数据中有一项缺失 进行处理
            print(current_date, 'missing data')  # 打印一条错误消息，指出缺失数据的日期
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # 根据数据绘制图像
    fig = plt.figure(dpi=128, figsize=(10, 6))
    # alpha指定颜色的透明度,0表示完全透明，1（默认设置）表示完全不透明
    plt.plot(dates,highs, c='red', alpha=0.5)
    plt.plot(dates,lows, c='blue', alpha=0.5)
    # 给图表区域着色，参数facecolor为填充区域的颜色
    plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

    # 设置图像的格式
    # plt.title("Daily high temperatures,July 2014", fontsize=24)  # 2014.7月的
    title = 'Daily high and low temperatures - 2014\nDeath Valley,CA'
    plt.title(title, fontsize=20)  # 2014年
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()  # 绘制斜的日期标签，以免它们彼此重叠
    plt.ylabel('Temperature(F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

