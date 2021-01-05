# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : language_survey.py
# Time       ：2019/12/19 9:32 
# Author     ：Yan You Fei
# version    ：python 3.6
# Description：
"""
from TestProject_local.待整理.python编程从入门到实战.测试代码.测试类.survey import AnonymoUsSurvey

# 定义一个问题，并创建一个表示调查的AnonymoUsSurvey对象
question = "What language did you first learn to speak?"
my_survey = AnonymoUsSurvey(question)

# 显示问题并存查答案
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("laguage: ")
    if response =='q':
        break
    my_survey.stored_response(response)

# 显示调查结果
print("Thank you to everyone who participated in the survey!")
my_survey.show_results()