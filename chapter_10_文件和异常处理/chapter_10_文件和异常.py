# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : chapter_10_文件和异常.py
# Time       ：2020/10/26 15:40 
# Author     ：Yolanda Yan
# version    ：python 3.6
# Description：
"""

"""关键字with在不再需要访问文件后将其关闭
在文件路径中使用反斜杠（\）
"""
file_path = 'F:\DataAnalysisaCode\BasicTest\Python编程：从入门到实践\pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)

"""逐行读取"""
file_path = 'F:\DataAnalysisaCode\BasicTest\Python编程：从入门到实践\pi_digits.txt'
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())  # 消除文件行末尾换行符引起的多余空白行

"""使用文件的内容"""
file_path = 'F:\DataAnalysisaCode\BasicTest\Python编程：从入门到实践\pi_digits.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()  # 删除字符串前后的空格

print(pi_string)
print(len(pi_string))

message = 'I really like dogs.'
message.replace('dog', 'cat')

"""将文本写入文件中 python以默认的只读模式打开文件
   ‘w’:读取模式
   ‘r’：写入模式
   ‘a’：附加模式
   ‘r+’:读取和写入模式
   如果写入的文件不存在，函数open()将自动创建它。
   以写入（'w'）模式打开文件时，若指定的文件已存在，Python将在返回文件对象前清空该文件
   函数write()不会在你写入的文本末尾添加换行符
   """
filename = 'F:\DataAnalysisaCode\BasicTest\Python编程：从入门到实践\programming1.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")  # Python只能将字符串写入文本文件
    file_object.write("I love creating new games.\n")

"""附加到文件
   将新的内容添加到文件尾部，不会覆盖原来的内容"""
filename = 'F:\DataAnalysisaCode\BasicTest\Python编程：从入门到实践\programming1.txt'
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

"""10-3访客"""
user_name = input("please inter your name: ")
filename = 'F:\DataAnalysisaCode\BasicTest\Python编程：从入门到实践\guest.txt'
with open(filename, 'a') as file_object:
    file_object.write(user_name.title())

"""10-4 访客名单"""
while True:
    message = "please inter your name "
    message += "(Enter 'quit' you can quit.)"
    name = input(message)
    if name == 'quit':
        break
    print("Welcom " + name.title())
    filename = 'F:\DataAnalysisaCode\BasicTest\Python编程：从入门到实践\guest_book.txt'
    with open(filename, 'a') as file_object:
        file_object.write(name.title() + "\n")

"""异常处理"""
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")

"""try-except-else """
print("Give me two numbers,and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_num = input("\nFirst number: ")
    if first_num == 'q':
        break
    second_num = input("\nSecond number: ")
    if second_num == 'q':
        break
    try:
        answer = int(first_num) / int(second_num)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

"""处理FileNotFoundError异常"""
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry,the file " + filename + " does not exist."
    print(msg)

"""将字符串以空格为分隔符拆分为多个部分
   并将这些部分存储在一个列表中"""
title = "Alice in Wonderland"
title.split()

filename = 'F:\DataAnalysisaCode\BasicTest\Python编程：从入门到实践\\alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry,the file " + filename + " does not exist."
    print(msg)
else:
    # 计算文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")

    ###########   10.3.7##########################################
"""计算多个文件的单词数"""


def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry,the file " + filename + " does not exist."
        print(msg)
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print(
            "The file " + filename + " has about " + str(num_words) + " words.")


filename = 'F:\DataAnalysisaCode\BasicTest\Python编程：从入门到实践\\alice.txt'
count_words(filename)

"""获取多个文件的单词数"""
filenames = ['F:\DataAnalysisaCode\BasicTest\Python编程：从入门到实践\\alice.txt',
             'siddhartha.txt']
for filename in filenames:
    count_words(filename)

"""10-6 加法运算"""
print("Give me two numbers,and I'll sum them.")
print("Enter 'q' to quit.")
while True:
    first_num = input("\nFirst number: ")
    if first_num == 'q':
        break
    second_num = input("\nSecond number: ")
    if second_num == 'q':
        break
    try:
        answer = int(first_num) + int(second_num)
    except ValueError:
        print("You can't sum by string!")
    else:
        print(answer)

#################写入到json文件中  从json文件中读取#####################
"""将列表写入到json中"""
import json

numbers = [1, 23, 4, 5]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

"""将json读取到内存中"""
import json

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)

import json

username = input("What is your name ? ")
filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username.title() + "!")

import json

filename = 'username.json'
with open(filename)as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username.title() + "!")

"""将前两个结合到一起，增加异常情况的处理"""
import json

# 如果以前存储了用户名，就加载它
# 否则，就提示用户输入用户名并存储它
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print(
            "We'll remember you when you come back, " + username.title() + "!")
else:
    print("Welcome back, " + username.title() + "!")

#####################重构##############################
import json


def greet_user():
    """问候用户，并指出其名字"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print(
                "We'll remember you when you come back, " + username.title() + "!")
    else:
        print("Welcome back, " + username.title() + "!")


greet_user()

import json


def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username.title() + "!")
    else:
        username = get_new_username()
        print(
            "We'll remember you when you come back, " + username.title() + "!")


greet_user()

##################练习题########################
"""10-11 喜欢的数字"""
favor_num = input("Please inter your favorite number: ")
filename = 'favorite_number.txt'
with open(filename, 'w') as f_obj:
    json.dump(favor_num, f_obj)  # 将数字存储到文件中

with open(filename) as f_obj:
    favor_num = json.load(f_obj)  # 从文件中读取数字
    print("I know your favorite number ! It's " + favor_num + ".")

"""10-3 记住喜欢的数字"""
filename = 'favorite_number.txt'
try:
    with open(filename) as f_obj:
        favor_num = json.load(f_obj)
except FileNotFoundError:
    favor_num = input("Please inter your favorite number: ")
    with open(filename, 'w') as f_obj:
        json.dump(favor_num, f_obj)
else:
    print("I know your favorite number ! It's " + favor_num + ".")