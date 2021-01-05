# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : game_functions.py
# Time       ：2020/10/27 11:35 
# Author     ：Yolanda Yan
# version    ：python 3.6
# Description：
"""

import sys
import pygame

from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    # 检查按下的是否是右箭头键
    if event.key == pygame.K_RIGHT:
        # 按下右箭头键，moving_right设为True
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen, ship, bullets)


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        # 松开右箭头键，moving_right设为False
        ship.moving_right = False
    # 使用elif是因为每个事件都只与一个键相关联；
    # 如果玩家同时按下了左右箭头键，将检测到两个不同的事件
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, scren, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        # 响应QUIT事件
        if event.type == pygame.QUIT:
            sys.exit()

        # 响应KEYDOWN事件
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, scren, ship, bullets)

        # 响应KEYUP事件
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """更新屏幕上的图像，并切换到新的屏幕"""
    screen.fill(ai_settings.bg_color)  # 用背景色填充屏幕

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()  # 将飞船绘制到屏幕上，确保它出现在背景前面

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    """"更新子弹位置，并删除已消失的子弹"""
    # 更新子弹位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:  # 是否已从屏幕顶端消失
            bullets.remove(bullet)
    # print(len(bullets))


def fire_bullet(ai_settings,screen, ship, bullets):
    """如果还没达到限制，就发射一颗子弹"""
    # 创建一颗子弹，并将其加入编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:  # 前检查未消失的子弹数是否小于该设置
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)   # 将新子弹存储到编组bullets中