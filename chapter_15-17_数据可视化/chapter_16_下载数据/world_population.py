# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : world_population.py
# Time       ：2020/11/11 17:47 
# Author     ：Yolanda Yan
# version    ：python 3.6
# Description：
"""

import json
from country_codes import get_country_code
import pygal_maps_world.maps
from pygal.style import LightColorizedStyle as LCS,RotateStyle as RS

# 将数据加载到一个列表列表中
filename = './data/population_data.json'
with open(filename) as f:
    pop_data = json.load(f)  # 将数据转换为Python能够处理的格式，这里是一个列表

# 打印每个国家2010年的人口数量
# 创建一个包含人口数量的字典
cc_populations = {}
no_code_country_name =[]
for pop_dict in pop_data:
    # 每个pop_dict都是一个字典，包含四个键—值对
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']  # 国家的名称
        # 人口数量,由于小数的字符串直接转换为整数会报错，所以，先转换为小数再转换为整数
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# 根据人口数量将所有国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# 看看每组分别包括多少个国家
print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))

# ,井号后跟6个字符，前两个字符表示红色分量，接下来的两个表示绿色分量，最后两个表示蓝色分量。每个分量的取值范围为00（没有相应的颜色）~FF（包含最多的相应颜色）
wm_style = RS('#336699',base_style=LCS)  # 让Pygal使用一种基色，该色为淡蓝色基色,LCS为基本样式
wm = pygal_maps_world.maps.World(style=wm_style)
wm.title = 'World Populations in 2010, by Country'
# 人口最少的国家颜色最浅，人口最多的国家颜色最深
wm.add('0-10m', cc_pops_1)
wm.add('10m-1b', cc_pops_2)
wm.add('>1b', cc_pops_3)

wm.render_to_file('./result/world_population.svg')


