# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 20:50:12 2018

@author: GEAR
"""

import cv2
import numpy as np

image = cv2.imread('j.png', 0)
cv2.namedWindow('original',cv2.WINDOW_NORMAL)
cv2.imshow('original', image)

kernel = np.ones((5,5), np.uint8)

'''
开运算:先腐蚀再膨胀就叫做开运算，其被用来去除噪声
'''
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imshow('opening', opening)

'''
闭运算：先膨胀再腐蚀,经常用来填充前景物体中的小洞，或者前景物体上的小黑点
'''
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.imshow('closing', closing)

'''
形态学梯度：其实就是一幅图像膨胀与腐蚀的差别，结果看上去就像前景的轮廓
'''
gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('gradient', gradient)

'''
礼帽：原始图像与进行开运算之后得到的图像的差
'''
tophat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

'''
黑帽：原始图像与进行闭运算之后得到的图像的差
'''
blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

cv2.waitKey(0)
cv2.destroyAllWindows()

