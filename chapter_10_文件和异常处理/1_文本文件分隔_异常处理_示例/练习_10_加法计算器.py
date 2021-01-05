# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : 练习_10_加法计算器.py
# Time       ：2019/12/16 15:44 
# Author     ：Yan You Fei
# version    ：python 3.6
# Description：
"""
print('请输入两个数字：')
print("输入'q'退出！")
while True:
    first_str = input("\n请输入第一个数字： ")
    if first_str == 'q':
        break
    second_str = input("\n请输入第二个数字： ")
    if second_str =='q':
        break
    try:
        first_num = int(first_str)
        second_num = int(second_str)
    except ValueError:
        print("输入的不是数字而是文本！")
    else:
        add_num = first_num + second_num
        print(add_num)

