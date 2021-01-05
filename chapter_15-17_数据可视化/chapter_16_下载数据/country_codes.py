# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : country_codes.py
# Time       ：2020/11/12 11:36 
# Author     ：Yolanda Yan
# version    ：python 3.6
# Description：
"""

# 注意：pygal为web交互式插件，因此需要联网
import pygal.maps.world  # 地图绘制，该句与书中不同，因为书中模块已经不存在

# 定义函数，返回适用于pygal的两位国别码
def get_country_code(country_name):
    """根据指定的国家，返回pygal使用的两个字母的国别码"""
     # pygal两位国别码列表表示法：pygal.maps.world.COUNTRIES.items()
    no_code_country_name={'Yemen, Rep.':'ye','Bolivia':'bo',}
    for code,name in pygal.maps.world.COUNTRIES.items():  # 改句与书中不同
        if name == country_name:
            return code
        elif country_name == 'Yemen, Rep.':
            return 'ye'
        elif country_name == 'Vietnam':
            return code
        elif country_name == 'Venezuela, RB':
            return 've'
        elif country_name == 'Tanzania':
            return 'tz'
        elif country_name == 'Moldova':
            return 'md'
        elif country_name == 'Macedonia, FYR':
            return 'mk'
        elif country_name == 'Macao SAR, China':
            return 'mo'
        elif country_name == 'Lao PDR':
            return 'la'
        elif country_name == 'Korea, Dem. Rep.':
            return 'kp'
        elif country_name == 'Korea, Rep.':
            return 'kr'
        elif country_name == 'Iran, Islamic Rep.':
            return 'ir'
        elif country_name == 'Hong Kong SAR, China':
            return 'hk'
        elif country_name == 'Guinea-Bissau':
            return 'gn'
        elif country_name == 'Gambia, The':
            return 'gm'
        elif country_name == 'Egypt, Arab Rep.':
            return 'eg'
        elif country_name == 'Bolivia':
            return 'bo'
        elif country_name == 'Congo, Dem. Rep.':
            return 'cd'
    # 如果没有找到指定的国家，就返回None
    return None

#
# print(get_country_code('Andorra'))
# print(get_country_code('United Arab Emirates'))
# print(get_country_code('Afghanistan'))