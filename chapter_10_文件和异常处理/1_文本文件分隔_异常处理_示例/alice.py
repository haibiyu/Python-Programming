# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : alice.py
# Time       ：2019/12/16 11:54 
# Author     ：Yan You Fei
# version    ：python 3.6
# Description：
"""

filename="alice.txt"

try:
   with open(filename) as f:
       contents = f.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)