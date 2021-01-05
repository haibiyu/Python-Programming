# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : countries.py
# Time       ：2020/11/12 11:19 
# Author     ：Yolanda Yan
# version    ：python 3.6
# Description：
"""

# 注意：pygal为web交互式插件，因此需要联网
import pygal.maps.world  # 地图绘制

# pygal两位国别码列表表示法：pygal.maps.world.COUNTRIES.items()
COUNTRIES = pygal.maps.world.COUNTRIES  # COUNTRIES为字典类型

for country_code in sorted(COUNTRIES.keys()):
    print(country_code,COUNTRIES[country_code])

