# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : random_walk.py
# Time       ：2020/11/11 11:21 
# Author     ：Yolanda Yan
# version    ：python 3.6
# Description：
"""

from random import choice

class RandomWalk():
    """一个生成随机漫步数据的类"""

    def __init__(self,num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points  # 随机漫步次数

        # 所有随机漫步都初始化为（0,0）
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有的点"""

        # 不断漫步，直到列表达到指定长度
        while len(self.x_values) < self.num_points:

            # 决定前进方向，以及沿着该前进方向前进的距离
            x_step = self.get_step()   # 为正将向右移动，为负将向左移动
            y_step = self.get_step()   # 为正向上移动，为负向下移动

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        """决定前进方向，以及沿着该前进方向前进的距离"""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step
