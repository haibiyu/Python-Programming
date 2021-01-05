# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : test_cities.py
# Time       ：2019/12/18 16:58 
# Author     ：Yan You Fei
# version    ：python 3.6
# Description：
"""
import unittest
from TestProject_local.待整理.python编程从入门到实战.测试代码.测试函数.city_functions import get_formatted_city_country

class NameTestCases(unittest.TestCase):
    """"""
    def test_city_country(self):
        """能够正确处理像'Santiago, Chile'这样的数据吗？"""
        formatted_city_country = get_formatted_city_country('santiago','chile')
        self.assertEqual(formatted_city_country,'Santiago, Chile')

    def test_city_country_population(self):
        """能够正确处理像'Santiago, Chile - population 5000000'这样的数据？"""
        formatted_city_country_population = get_formatted_city_country('santiago','chile','5000000')
        self.assertEqual(formatted_city_country_population,'Santiago, Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()