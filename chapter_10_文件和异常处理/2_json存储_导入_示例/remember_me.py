# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : remember_me.py
# Time       ：2019/12/18 11:30 
# Author     ：Yan You Fei
# version    ：python 3.6
# Description：
"""
import json

def get_stored_username():
    """如果存储了用户名，获取它"""
    filename = 'username.json'
    try:
        with open(filename,'r',encoding='utf-8') as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    filename = 'username.json'
    username = input("What's your name ?")
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(username, f)
    return username

def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()


