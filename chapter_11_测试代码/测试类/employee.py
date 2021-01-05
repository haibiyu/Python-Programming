# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : employee.py
# Time       ：2019/12/19 10:59 
# Author     ：Yan You Fei
# version    ：python 3.6
# Description：
"""
class Employee():

    def __init__(self,first,last,salary):
        """存储名、姓和年薪"""
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self):
        """默认年薪增加5000美元"""
        self.salary += 5000

    def give_custom_raise(self,increase):
        """增加任意的年薪量"""
        self.salary += increase

    def show_salary(self):
        """显示年薪"""
        print(self.salary)

