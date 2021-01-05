# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : alien_invasion.py
# Time       ：2020/10/26 15:54 
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


def run_game():
    """初始化游戏,设置并创建一个屏幕对象"""
    # 初始化pygame、设置和屏幕对象
    pygame.init()

    ai_settings = Settings()  # 创建一个Settings实例，并将其存储在变量ai_settings中

    # 创建屏幕
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)

        # 飞船的位置将在检测到键盘事件后（但在更新屏幕前）更新
        ship.update()

        gf.update_bullets(bullets)

        # 更新屏幕上的图像,并切换到新的屏幕
        gf.update_screen(ai_settings, screen, ship, bullets)


if __name__ == '__main__':
    run_game()
