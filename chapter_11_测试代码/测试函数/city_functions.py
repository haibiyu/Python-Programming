# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : city_functions.py
# Time       ：2019/12/18 16:38 
# Author     ：Yan You Fei
# version    ：python 3.6
# Description：
"""

def get_formatted_city_country(city,country,population=''):
    """将城市和国家拼接起来"""
    if population:
        city_counrty = city + ", " + country
        formatted_city_counrty = city_counrty.title() + " - population " + population
    else:
        city_counrty = city + ", " + country
        formatted_city_counrty = city_counrty.title()
    return formatted_city_counrty


