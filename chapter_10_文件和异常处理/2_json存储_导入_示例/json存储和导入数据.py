# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : json存储和导入数据.py
# Time       ：2019/12/17 9:42 
# Author     ：Yan You Fei
# version    ：python 3.6
# Description：
"""
import json

# # 存储为json
# dict_data = {1: 'lucy', 2: "lily", 3: "monky"}
# filename = 'dict_format.json'
# # 方法一
# with open(filename, 'w', encoding='utf-8') as f:
#     json.dump(dict_data, f)
#
# # 方法二
# number_data = [1, 2, 3, 4, 5]
# filename = 'number_format.json'
# f = open(filename, 'w', encoding='utf-8')
# f_json = json.dumps(number_data)
# f.write(f_json)
# f.close()


# 导入json格式的数据
filename = 'number_format.json'
# f = open(filename, 'r', encoding='utf-8')
# data = json.load(f)
# print(data)

def save_to_json(filename, data):
    """将数据存储为json格式"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            data = json.dump(data, f)
    except FileNotFoundError:
        print("Sorry,the file " + filename + " does not exist.")
    else:
        print(data)


def load_json(filename):
    """导入json文件"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Sorry,the file " + filename + " does not exist.")
    else:
        print(data)

load_json(filename)