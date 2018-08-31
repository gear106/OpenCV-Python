# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 16:55:33 2018

@author: GEAR
"""

'''
在OpenCV中有超过150中进行颜色转换的方法，但我们经常用到的一般只有两种：
BGR <-> Gray 和 BGR <-> HSV
我们需要用到的函数有：cv2.cvtColor(input_image, flag),其中flag是转换类型
对于BGR <-> Gray，我们用到的flag为cv2.COLOR_BGR2GRAY,但我们要注意在OpenCV
中HSV格式中H 色彩/亮度 的取值范围是[0 179], S 饱和度 和 V 亮度的取值范围是
[0, 255]
'''
import cv2
flags = [i for i in dir(cv2) if i.startswith ('COLOR_')]
print(flags)
