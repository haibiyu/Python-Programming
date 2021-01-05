# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : die.py
# Time       ：2020/11/11 14:50 
# Author     ：Yolanda Yan
# version    ：python 3.6
# Description：
"""

from random import randint

class Die():
    """表示一个骰子的类"""

    def __init__(self,num_sides=6):
        """骰子默认为6面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面数之间的随机数"""
        return randint(1,self.num_sides)