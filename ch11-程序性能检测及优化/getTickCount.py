# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 23:29:20 2018

@author: GEAR
"""

# 计算程序运行时间
import cv2

root = 'D:/python/OpenCV-Python/data/'
img1 = cv2.imread(root + 'messi5.jpg')

e1 = cv2.getTickCount()

for i in range(5, 49, 2):
    img1 = cv2.medianBlur(img1, i)
    
e2 = cv2.getTickCount()
t = (e2 - e1) / cv2.getTickFrequency()
print(t)
    