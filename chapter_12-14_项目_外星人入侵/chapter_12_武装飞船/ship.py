# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : ship.py
# Time       ：2020/10/26 17:27 
# Author     ：Yolanda Yan
# version    ：python 3.6
# Description：
"""

import os
import pygame

# 在Pygame中，原点(0, 0)位于屏幕左上角，向右下方移动时，坐标值将增大。
# 在1200×800的屏幕上，原点位于左上角，而右下角的坐标为(1200, 800)

class Ship():
    """创建飞船类"""
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像，并获取其外接矩阵
        cur_path = os.path.dirname(os.getcwd()).replace("\\", "/")  # 获取当前路径的上一路径
        self.image = pygame.image.load(cur_path+'/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx  # 要将游戏元素居中，rect的centerx等属性只能存储整数值
        self.rect.bottom = self.screen_rect.bottom  # 游戏元素与屏幕边缘对齐

        # 在飞船的属性center中存储为小数值
        self.center = float(self.rect.centerx)


        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船位置"""
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right: # 限制飞船的活动范围，防止移到屏幕外面
            self.center += self.ai_settings.ship_speed_factor
        # 使用if的目的是为了当同时按下左右键时，飞船的位置保持不变
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center更新rect
        self.rect.centerx = self.center


    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)