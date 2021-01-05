# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : button.py
# Time       ：2020/11/2 14:51 
# Author     ：Yolanda Yan
# version    ：python 3.6
# Description：
"""

import pygame.font  # 它让Pygame能够将文本渲染到屏幕上

class Button():

    def __init__(self,ai_settings,screen,msg):
        """初始化按钮的属性"""
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮的尺寸和其他属性
        self.width,self.height = 200,50
        self.button_color = (0,255,0)    # 亮绿色
        self.text_color = (255,255,255)  # 文本为白色
        # 实参None让Pygame使用默认字体，而48指定了文本的字号
        self.font = pygame.font.SysFont(None,48)

        # 创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        # 按钮的标签只需创建一次
        self.prep_msg(msg)  # msg：在按钮中显示的文本

    def prep_msg(self,msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        # 将存储在msg中的文本转换为图像，然后将该图像存储在msg_image中
        # 布尔实参指定开启还是关闭反锯齿功能（反锯齿让文本的边缘更平滑）
        # 余下的两个实参分别是文本颜色和背景颜色
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)

        # 让文本图像在按钮上居中
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """绘制一个用颜色填充的按钮，再绘制文本"""
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)




