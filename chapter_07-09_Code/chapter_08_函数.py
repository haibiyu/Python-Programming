# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : chapter_08_函数.py
# Time       ：2020/10/26 15:27 
# Author     ：Yolanda Yan
# version    ：python 3.6
# Description：
"""

# ########## 练习题 ############### #
"""8-4 大号T恤"""
def make_shirt(size='大号', words='I love Python'):
    print("\nT恤的尺码是 " + size)
    print("T恤的字样是 " + words)

make_shirt()
make_shirt(size='中号')
make_shirt(words='I love China!')

"""8-5 城市"""
def describe_city(city_name, country_name='china'):
    print(city_name.title() + " is in " + country_name.title() + "!")

describe_city('beijing')
describe_city(city_name='sichuan')
describe_city(country_name='Japan', city_name='tokyo')
# ############################### #

"""8.3.2 让实参变成可选的"""
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# ########## 练习题 ############### #
"""8-6 城市名"""
def city_country(city_name, country_name):
    print(city_name.title() + ", " + country_name.title())

city_country('santiago', 'chile')
city_country('beijing', 'china')
city_country('tokyo', 'japan')

"""8-7专辑"""
def make_album(singer_name, album_name, song_number=''):
    album = {'singer_name': singer_name.title(),
             'album_name': album_name.title()}
    if song_number:
        album['song_number'] = song_number.title()
    return album

album = make_album('zhangjie', 'live')
print(album)

album = make_album('taozhe', 'aihenjiandan', '8')
print(album)

"""8-8 用户的专辑"""
def make_album(singer_name, album_name):
    album = {'singer_name': singer_name.title(),
             'album_name': album_name.title()}
    return album

while True:
    print("\nPlease tell me some album information: ")
    print("(enter 'q' at any time to quit)")

    s_name = input("Singer_name: ")
    if s_name == 'q':
        break
    a_name = input("Album_name: ")
    if a_name == 'q':
        break

    album = make_album(s_name, a_name)
    print(album)

"""8-11不变的魔术师"""
def show_magician(magicians_list):
    for name in magicians_list:
        print(name.title())

def make_great(magicians_list):
    for i in range(len(magicians_list)):
        magicians_list[i] = "the Great " + magicians_list[i].title()
    return magicians_list


magicians_list = ['john', 'tom', 'lily']
m = make_great(magicians_list[:])  # 传递的是列表的副本，对原始列表不做修改
show_magician(magicians_list)  # 显示原始列表的结果
show_magician(m)  # 显示修改后的结果
# ############################### #

"""8.5 传递任意数量的实参"""


def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra cheese')


def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton',
                             field='physics')
print(user_profile)

import random

menu = ['coffee', 'tea', 'cola', 'milk', 'water']
name = input("your name: ")
drink = random.choice(menu)
print("Hello " + name.title() + "! Enjoy your " + drink)