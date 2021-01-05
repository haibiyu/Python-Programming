# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : alien_invasion.py
# Time       ：2020/11/2 14:44
# Author     ：Yolanda Yan
# version    ：python 3.6
# Description：
"""

import sys
import pygame
from pygame.sprite import Group  # Group类类似于列表，但提供了有助于开发游戏的额外功能

from settings import Settings  # 导入Settings类
from ship import Ship  # 导入Ship类
import game_functions as gf

from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard



def run_game():
    """初始化游戏,设置并创建一个屏幕对象"""
    # 初始化pygame、设置和屏幕对象
    pygame.init()

    ai_settings = Settings()  # 创建一个Settings实例，并将其存储在变量ai_settings中

    # 创建屏幕
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建play按钮
    play_button = Button(ai_settings,screen,'play')

    # 创建用于存储游戏统计信息的实例,并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)

    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen,ship, aliens)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,aliens, bullets)

        if stats.game_active:
            # 飞船的位置将在检测到键盘事件后（但在更新屏幕前）更新
            ship.update()

            gf.update_bullets(ai_settings, screen,stats,sb, ship, aliens,bullets)

            gf.update_aliens(ai_settings,screen,stats,sb, ship, aliens,bullets)

        # 更新屏幕上的图像,并切换到新的屏幕
        gf.update_screen(ai_settings, screen, stats, sb,ship, aliens, bullets, play_button)


if __name__ == '__main__':
    run_game()
