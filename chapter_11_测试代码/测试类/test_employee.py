# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : test_employee.py
# Time       ：2019/12/19 11:05 
# Author     ：Yan You Fei
# version    ：python 3.6
# Description：
"""

import unittest
from TestProject_local.待整理.python编程从入门到实战.测试代码.测试类.employee import Employee

class TestEmployee(unittest.TestCase):
    """ """
    def setUp(self):
        """创建一个员工对象，供使用的测试方法使用"""
        self.employee = Employee('joni','haom',8000)

    def test_give_default_raise(self):
        """测试是否能正常增加默认年薪量"""
        self.employee.give_raise()
        self.employee.show_salary()

    def test_give_custom_raise(self):
        """测试是否能正常增加任意的年薪量"""
        self.employee.give_custom_raise(3000)
        self.employee.show_salary()


if __name__ == '__main__':
    unittest.main()

