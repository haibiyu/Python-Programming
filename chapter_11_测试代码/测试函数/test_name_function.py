# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : test_name_function.py
# Time       ：2019/12/18 15:57 
# Author     ：Yan You Fei
# version    ：python 3.6
# Description：
"""
import unittest
from TestProject_local.待整理.python编程从入门到实战.测试代码.测试函数.name_function import get_formated_name

class NamesTestCase(unittest.TestCase):
    """测试 name_function.py"""
    # 方法名必须以test_打头，这样它才会在我们运行test_name_function.py时自动运行
    def test_first_last_name(self):
        """能够正确的处理像janis joplin这样的姓名吗？"""
        formatted_name = get_formated_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')  # 检查返回的姓名是否与预期的姓名一致

    def test_first_last_middle_name(self):
        """能够正确处的理像Wolfgang Amadeus Mozart这样的姓名吗？"""
        formatted_name = get_formated_name('wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()