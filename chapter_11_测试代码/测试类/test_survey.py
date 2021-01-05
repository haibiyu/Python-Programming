# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : test_survey.py
# Time       ：2019/12/19 9:40 
# Author     ：Yan You Fei
# version    ：python 3.6
# Description：
"""
import unittest
from TestProject_local.待整理.python编程从入门到实战.测试代码.测试类.survey import AnonymoUsSurvey

class TestAnonymoUsSurvey(unittest.TestCase):
    """针对AnonymoUsSurvey的测试"""

    def setUp(self):
        """创建一个调查对象和一组答案，供使用的测试方法使用"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymoUsSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """测试单个答案会被妥善的存储"""
        self.my_survey.stored_response(self.responses[0])

        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善存储"""
        for response in self.responses:
            self.my_survey.stored_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()