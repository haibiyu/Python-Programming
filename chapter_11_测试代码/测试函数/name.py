# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : name.py
# Time       ：2019/12/18 15:43 
# Author     ：Yan You Fei
# version    ：python 3.6
# Description：
"""
from TestProject_local.待整理.python编程从入门到实战.测试代码.测试函数.name_function import get_formated_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first =='q':
        break
    last = input("\nPlease give me a last name: ")
    if last == 'q':
        break
    formatted_name = get_formated_name(first,last)
    print("\tNeatly formatted name " + formatted_name +".")