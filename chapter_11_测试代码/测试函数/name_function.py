# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : name_function.py
# Time       ：2019/12/18 15:44 
# Author     ：Yan You Fei
# version    ：python 3.6
# Description：
"""

def get_formated_name(first, last, middle=''):
    """生成整洁的姓名."""
    if middle:
        full_name = first + " " + middle + " " + last
    else:
        full_name = first + " " + last
    return full_name.title()