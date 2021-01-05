# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : 练习_10_猫和狗.py
# Time       ：2019/12/16 15:57 
# Author     ：Yan You Fei
# version    ：python 3.6
# Description：
"""


def print_content(filename):
    """打印文本中的内容，对文件不存在的异常问题进行处理"""
    try:
        with open(filename,'r',encoding='utf-8') as f:
            contents=f.read()
    except FileNotFoundError:
        # print("\n")
        # print("Sorry, the file "+filename+" does not exsits.")
        pass
    else:
        print("The file "+filename+" contents:")
        print(contents)

filenames = ['cats.txt','dogs.txt']
for filename in filenames:
    print_content(filename)

