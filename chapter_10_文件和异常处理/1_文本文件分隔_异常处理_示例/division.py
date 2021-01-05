# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : division.py
# Time       ：2019/12/16 11:41 
# Author     ：Yan You Fei
# version    ：python 3.6
# Description：
"""

print("Give me two numbers,and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number =='q':
        break
    # try-except 对异常进行处理，能够抵御无意的用户错误和恶意攻击
    try:
        answer = int(first_number) / int(second_number)

    except ZeroDivisionError:
        print("You can't divide by zero! ")
    else:  # try成功执行后执行else
        print(answer)



