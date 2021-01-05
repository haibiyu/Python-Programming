# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : settings.py
# Time       ：2020/10/26 17:14 
# Author     ：Yolanda Yan
# version    ：python 3.6
# Description：
"""

class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 500
        self.bg_color = (230, 230, 230)  # 设置背景色，由RGB组成  将背景设置为一种浅灰色

        # 飞船的设置
        self.ship_speed_factor = 1.5

        # 子弹设置,创建宽3像素、高15像素的深灰色子弹
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3  # 存储所允许的最大子弹数
