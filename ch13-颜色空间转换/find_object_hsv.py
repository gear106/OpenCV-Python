# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 18:57:30 2018

@author: GEAR
"""

'''
如何找到跟踪对象的HSV值？
'''
import cv2
import numpy as np

green = np.uint8([[[255, 0, 0]]])
hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
print(hsv_green)

