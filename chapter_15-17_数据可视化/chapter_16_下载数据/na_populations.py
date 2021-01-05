# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : na_populations.py
# Time       ：2020/11/12 14:30 
# Author     ：Yolanda Yan
# version    ：python 3.6
# Description：在世界地图上呈现数字数据
"""

import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()
wm.title = "Populations of Countries in North America"
# 人口最少的国家颜色最浅，人口最多的国家颜色最深
wm.add("North America",{'ca': 34126000,'us': 309349000,'mx': 113423000})

wm.render_to_file("./result/na_populations.svg")
