# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : game_functions.py
# Time       ：2020/11/2 14:44
# Author     ：Yolanda Yan
# version    ：python 3.6
# Description：
"""

import sys
import pygame

from bullet import Bullet
from alien import Alien
from time import sleep

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
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        # 松开右箭头键，moving_right设为False
        ship.moving_right = False
    # 使用elif是因为每个事件都只与一个键相关联；
    # 如果玩家同时按下了左右箭头键，将检测到两个不同的事件
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, stats,sb, play_button, ship,aliens, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        # 响应QUIT事件
        if event.type == pygame.QUIT:
            sys.exit()

        # 响应KEYDOWN事件
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        # 响应KEYUP事件
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 玩家单击时鼠标的x和y坐标
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button,ship, aliens, bullets,mouse_x,mouse_y)


def check_play_button(ai_settings, screen, stats,sb,play_button,ship, aliens, bullets,mouse_x,mouse_y):
    """在玩家点击play按钮时开始新游戏"""
    # collidepoint()检查鼠标单击位置是否在Play按钮的rect
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    # 仅当玩家单击了Play按钮且游戏当前处于非活动状态时，游戏才重新开始
    if button_clicked and not stats.game_active:
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()
        # 隐藏光标
        pygame.mouse.set_visible(False)
        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True

        # 重置记分牌图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()


        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，让飞船居中
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()



def update_screen(ai_settings, screen, stats,sb,ship, aliens, bullets,play_button):
    """更新屏幕上的图像，并切换到新的屏幕"""
    screen.fill(ai_settings.bg_color)  # 用背景色填充屏幕

    # 先绘制子弹和飞船，再绘制外星人，让外星人在屏幕上位于最前面
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()  # 将飞船绘制到屏幕上，确保它出现在背景前面
    aliens.draw(screen)  # 在屏幕上绘制编组中的每个外星人

    # 显示得分
    sb.show_score()

    # 如果游戏处理非活跃状态，就绘制play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(ai_settings,screen,stats,sb,ship,aliens, bullets):
    """"更新子弹位置，并删除已消失的子弹"""
    # 更新子弹位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:  # 是否已从屏幕顶端消失
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen,stats,sb, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens, bullets):
    """响应子弹和外星人的碰撞"""
    # 删除发生碰撞的子弹和外星人
    # groupcollide将每颗子弹的rect同每个外星人的rect进行比较，并返回一个字典，其中包含发生了碰撞的子弹和外星人。在这个字典中，每个键都是一颗子弹，而相应的值都是被击中的外星人
    # 两个实参True告诉Pygame删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()  # 创建一幅显示最新得分的新图像
        check_high_score(stats,sb)

    if len(aliens) == 0:
        # 删除现有子弹，并新建一群新外星人
        bullets.empty()
        ai_settings.increase_speed()  # 加快游戏速度

        # 如果整群外星人都被消灭，就提高一个等级
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)

def fire_bullet(ai_settings,screen, ship, bullets):
    """如果还没达到限制，就发射一颗子弹"""
    # 创建一颗子弹，并将其加入编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:  # 前检查未消失的子弹数是否小于该设置
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)   # 将新子弹存储到编组bullets中

def get_number_aliens_x(ai_settings,alien_width):
    """计算每行可容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = ai_settings.screen_height - 3*alien_height - ship_height
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    """创建一个外星人，并将其放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算一行可容纳多少个外星人
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    # 创建外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings,aliens):
    """有外星人到达边缘时，采取相应措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    """将整群外星人下移，并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings,screen,stats,sb, ship, aliens,bullets):
    """响应被外星人撞到的飞船"""
    if stats.ship_left > 0:
        # 将ship_left 减 1
        stats.ship_left -= 1

        # 更新记分牌
        sb.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并将飞船放到屏幕底端中央
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)  # 在游戏进入非活动状态后，立即让光标可见

def check_aliens_bottom(ai_settings,screen,stats, sb, ship, aliens,bullets):
    """检查是否有外星人到达屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样处理
            ship_hit(ai_settings,screen,stats,sb, ship, aliens,bullets)
            break

def update_aliens(ai_settings,screen,stats,sb, ship, aliens,bullets):
    """检查是否有外星人位于屏幕边缘，并更新整群外星人的位置"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

    # 检测外星人与飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):  # 找到的第一个与飞船发生了碰撞的外星人
        update_aliens(ai_settings,stats,screen, ship, aliens,bullets)

    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings,screen,stats, sb, ship, aliens,bullets)

def check_high_score(stats,sb):
    """检查是否诞生了新的最高分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()  # 修改最高得分图像



