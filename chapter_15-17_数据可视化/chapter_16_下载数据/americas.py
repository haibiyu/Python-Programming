# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : americas.py
# Time       ：2020/11/12 14:12 
# Author     ：Yolanda Yan
# version    ：python 3.6
# Description：
"""

# 以下两句与书中不同，（书中的模块已经不存在了）
import pygal_maps_world.maps
wm = pygal_maps_world.maps.World()  # 世界地图
wm.title = "North,Central, and South American"

# add需要输入一个标签和一个列表，列表表示的是要突出的国家的国别码
# 每次调用add()都将为指定的国家选择一种新颜色，并在图表左边显示该颜色和指定的标签
wm.add("North America",['ca','mx','us'])  # 北美，加拿大、墨西哥、美国
wm.add("Central America",['bz','cr','gt','hn','ni','pa','sv'])  # 中美
wm.add('South America',['ar','bo','br','cl','co','ec','gf',
                        'gy','pe','py','sr','uy','ve'])  # 南美

# 创建一个包含该图表的.svg文件，可在浏览器中打开
wm.render_to_file("./result/americas.svg")
