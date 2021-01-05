# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : hn_submissions.py
# Time       ：2020/11/19 14:56 
# Author     ：Yolanda Yan
# version    ：python 3.6
# Description：
"""

import requests
from operator import itemgetter

# 执行API调用并存储响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
try:
    r = requests.get(url, timeout=3)
    # 与书中不同，书中会报错，加了一个try except
    if r.content:
        print("Status Code: ", r.status_code)  # 打印响应状态

        # 处理有关每篇文章的信息
        submission_ids = r.json()
        submission_dicts = []
        for submission_id in submission_ids[:30]:
            # 对每篇文章，都执行一个API调用
            url = ('https://hacker-news.firebaseio.com/v0/item/' + str(
                submission_id) + '.json')
            submission_r = requests.get(url)
            print(submission_r.status_code)  # 打印每次请求的状态，以便知道请求是否成功
            if submission_r.content:
                response_dict = submission_r.json()

                submission_dict = {'title': response_dict['title'],  # 文章标题
                                   'link': 'http://news.ycombinator.com/item?id=' + str(
                                       submission_id),  # 文章链接
                                   # dict.get()：在指定的键存在时返回与之相关联的值，并在指定的键不存在时返回你指定的值（这里是0）
                                   'comments': response_dict.get('descendants', 0)
                                   # 文章评论数
                                   }
                submission_dicts.append(submission_dict)

        # 按降序排列，即评论最多的文章位于最前面
        submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                                  reverse=True)
        for submission_dict in submission_dicts:
            print('\nTitle: ', submission_dict['title'])
            print('Discussion link: ', submission_dict['link'])
            print('Comments: ', submission_dict['comments'])
except:
    print("OK")


