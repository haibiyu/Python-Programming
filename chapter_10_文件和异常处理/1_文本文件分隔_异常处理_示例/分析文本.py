# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : 分析文本.py
# Time       ：2019/12/16 14:17 
# Author     ：Yan You Fei
# version    ：python 3.6
# Description：
"""
# title = "Alice’s Adventures in Wonderland"
# print(title.split())  # split()以空格分隔符将字符串拆成多个部分



def count_words(filename):
    """计算一个文件大致包含多少单词"""
    try:
        with open(filename,'r', encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file "+filename+" has about "+str(num_words)+" words.")


filenames =["alice.txt","mobi.txt"]
for filename in filenames:
    count_words(filename)