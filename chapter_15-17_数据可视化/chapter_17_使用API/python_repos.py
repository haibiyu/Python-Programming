# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : python_repos.py
# Time       ：2020/11/13 9:50 
# Author     ：Yolanda Yan
# version    ：python 3.6
# Description：
"""

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
print("Status Code:", requests.get(url).status_code)
try:
    r = requests.get(url,timeout=3)
    # 与书中不同，书中会报错，加了一个try except
    if r.content:
        # 将API响应存储在一个大的变量中
        response_dict = r.json()
        # print(response_dict)
        # 处理结果,total_countb表示GitHub总共包含的python仓库数
        print("Total repositories: ", response_dict['total_count'])

        # 探索有关仓库的信息
        # 'items'是一个列表，其中包含很多字典，而每个字典都包含有关一个Python仓库的信息
        repo_dicts = response_dict['items']
        print("Repositories returned: ",len(repo_dicts))

        # 研究第一个仓库
        # repo_dict = repo_dicts[0]
        # print("\nKeys: ",len(repo_dict))  # 打印这个字典包含的键数,看有多少信息
        # for key in sorted(repo_dict.keys()):
        #     print(key)
        # print("\nSelected information about first repository:")
        # print("Name: ", repo_dict['name'])  # 项目名称
        # print("Owner: ", repo_dict['owner']['login'])  # 所有者的登录名
        # print("Stars: ", repo_dict['stargazers_count'])  # 项目获得多少个星的评级
        # print("Repository: ",repo_dict['html_url'])  # 项目在github仓库的url
        # print("Created: ", repo_dict['created_at'])  # 项目创建时间
        # print("Updated: ",repo_dict['updated_at'])   # 项目最后一次更新时间
        # print("Description: ", repo_dict['description'])  # 仓库的描述

        names, plot_dicts = [], []
        for repo_dict in repo_dicts:
            names.append(repo_dict['name'])  # 项目名称
            plot_dict={'value': repo_dict['stargazers_count'],  # 项目获得星个数
                       'label': repo_dict['description'],  # 仓库的描述
                       'xlink': repo_dict['html_url']}  # url地址
            plot_dicts.append(plot_dict)

        # 可视化
        my_style = LS("#333366",base_style=LCS)

        # 创建一个pygal类Config实例
        my_config = pygal.Config()
        # 修改my_config属性，定制图表的外观
        my_config.x_label_rotation = 45
        my_config.show_legend = False
        my_config.title_font_size = 24  # 标题字体大小
        my_config.label_font_size = 14  # 副标签是x轴上的项目名以及y轴上的大部分数字
        my_config.major_label_font_size = 18  # 主标签（y轴上为5000整数倍的刻度）字体
        my_config.truncate_label = 15   # 将较长的项目名缩短为15个字符
        my_config.show_y_guides = False  # 隐藏图表中的水平线
        my_config.width = 1000  # 自定义宽度，让图表更充分地利用浏览器中的可用空间

        chart = pygal.Bar(my_config, style=my_style)
        chart.title = 'Most-Starred Python Projects on Github'
        chart.x_labels = names

        chart.add('', plot_dicts)
        chart.render_to_file('./result/python_repos_1.svg')









except:
    print("OK")

