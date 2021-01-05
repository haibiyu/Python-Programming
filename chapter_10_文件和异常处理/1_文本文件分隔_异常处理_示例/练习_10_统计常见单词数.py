# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : 练习_10_统计常见单词数.py
# Time       ：2019/12/17 9:32 
# Author     ：Yan You Fei
# version    ：python 3.6
# Description：
"""
def count_words(filename,word):
    """统计文件中，某个单词的数量"""
    try:
        with open(filename,'r',encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print("Sorry,the file "+filename+" does not exist.")
    else:
        words_count = contents.lower().count(word)
        print("In %s, '%s' count is : %d ." % (filename, word, words_count))


filenames =['alice.txt','Komet und Erde.txt']
for filename in filenames:
    count_words(filename,'the')