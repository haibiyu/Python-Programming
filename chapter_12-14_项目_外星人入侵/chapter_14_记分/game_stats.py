# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : game_stats.py
# Time       ：2020/11/2 14:44
# Author     ：Yolanda Yan
# version    ：python 3.6
# Description： 跟踪游戏统计信息类
"""

class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # 游戏刚启动时处于非活动状态
        self.game_active = False

        # 在任何情况下都不应该重置最高分
        self.high_score = 0
        self.level = 1  # 当前等级

    def reset_stats(self):
        """初始化在游戏统计期间可能变化的统计信息"""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0



