# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : scoreboard.py
# Time       ：2020/11/4 10:26 
# Author     ：Yolanda Yan
# version    ：python 3.6
# Description：
"""

import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """显示得分信息类"""
    def __init__(self,ai_settings,screen,stats):
        """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 显示得分信息时使用的字体设置
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        # 准备包含最高得分和当前得分的图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()  # 在当前得分下方显示当前等级
        self.prep_ships()

    def prep_score(self):
        """将得分转换为一幅渲染的图像"""
        # round()通常让小数精确到小数点后多少位，其中小数位数是由第二个实参指定的。然而，如果将第二个实参指定为负数，round()将圆整到最近的10、100、1000等整数倍
        rounded_score = int(round(self.stats.score,-1))
        score_str = "{:,}".format(rounded_score)  # 例如，输出1,000,000而不是1000000
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)

        # 将得分放在右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """将最高得分转换为渲染的图像"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)  # 例如，输出1,000,000而不是1000000
        self.high_score_image = self.font.render(high_score_str, True, self.text_color,
                                            self.ai_settings.bg_color)

        # 将最高得分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def prep_level(self):
        """将等级转换为渲染的图像"""
        self.level_image = self.font.render(str(self.stats.level), True,
                                                 self.text_color,
                                                 self.ai_settings.bg_color)

        # 将等级放在得分下面
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10


    def prep_ships(self):
        """显示还余下多少艘飞船"""
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.ai_settings,self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """在屏幕上显示当前得分、最高得分和当前等级"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)

        # 绘制飞船
        self.ships.draw(self.screen)


