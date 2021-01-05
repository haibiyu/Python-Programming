# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : chapter_07_用户输入和while循环.py
# Time       ：2020/10/26 15:21 
# Author     ：Yolanda Yan
# version    ：python 3.6
# Description：
"""

import numpy as np

x0=np.array([1,2,3,4,5,6,7,8])
x1 = x0.cumsum()  # 1-AGO序列  cumsum()累计求和
z1 = (x1[:len(x1)-1] + x1[1:])/2.0  # 紧邻均值（MEAN）生成序列  x1(k+1)+x1(k)/2
z1 = z1.reshape((len(z1),1))  # n-1行 1列
B = np.append(-z1, np.ones_like(z1), axis=1)   # [-Z1(2) 1]
Yn = x0[1:].reshape((len(x0)-1, 1))    # 即x0(1) x0(2) ... x0(n)
[[a],[b]] = np.dot(np.dot(np.linalg.inv(np.dot(B.T, B)), B.T), Yn)  # 计算参数 [a,b]=inv(B'B)B'Y
f = lambda k: (x0[0]-b/a)*np.exp(-a*(k-1))-(x0[0]-b/a)*np.exp(-a*(k-2))  #还原值

print("x1",x1)
print("z1",z1)
print("B",B)
print("y",Yn)
print("a",a)
print("b",b)
print("f",f(9))

"""P109"""

prompt = "\nTell me something, and I will repeat it back to you ."
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

prompt = "\nPlease enter the name of a city you have visited."
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

# ########## 练习题 ############### #
"""7-4 比萨配料"""
prompt = "\n请输入一系列的比萨配料。"
prompt += "\n在输入‘quit'时结束循环。"
while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print("我们会在比萨中添加" + message + "配料。")

"""7-5  电影票"""
prompt = "\n请输入观众年龄，在输入’quit‘时结束循环。"
while True:
    age_message = input(prompt)
    if age_message == 'quit':
        break
    else:
        age = int(age_message)

    if age < 3:
        print("您的电影票是免费的。")
    elif age >= 3 and age <= 12:
        print("您的电影票价为10美元。")
    elif age > 12:
        print("您的电影票价为15美元。")
# ############################### #


"""P112"""
# 首先，创建一个待验证用户列表，和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 验证每个用户，直到没有未验证用户为止，将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    confirmed_users.append(current_user)

# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

"""删除包含特定值的所有列表元素"""
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

"""7.3.3使用用户输入来填充字典"""

responses = {}
# 设置一个标志，指出调查者是否继续
polling_active = True

while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\nWhat is your name ? ")
    response = input("Which mountain would you like to climb someday?")
    # 将答卷存储在字典中
    responses[name] = response
    # 看是否还有人要参加调查
    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat == 'no':
        polling_active = False
# 调查结束，显示结果
print("\n---Poll Results---")
for name, response in responses.items():
    print(name.title() + " would like to climb " + response.title() + ".")