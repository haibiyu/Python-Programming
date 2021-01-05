# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : bar_descriptions.py
# Time       ：2020/11/19 11:09 
# Author     ：Yolanda Yan
# version    ：python 3.6
# Description：
"""
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS("#333366",base_style=LCS)
chart = pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)
chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts =[{'value': 16101, 'label': 'Description of httpie.'},
             {'value': 15028, 'label': 'Description of django.'},
             {'value': 14798, 'label': 'Description of flask.'}]


chart.add('', plot_dicts)
chart.render_to_file('./result/bar_descriptions.svg')
