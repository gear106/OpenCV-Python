# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 19:51:15 2018

@author: GEAR
"""

'''
形态学操作一般情况下对二值图进行处理
两个基本的形态学操作是腐蚀和膨胀，他们的变体构成了开运算、闭运算、梯度等
腐蚀就像土壤侵蚀一样，这个操作会把前景物体的边界腐蚀掉（但是前景仍然是白
色），具体操作为卷积核沿着图像移动，如果与卷积核对应的原图像的所有像素值
都是1，那么中心元素就保持原来的像素值，否则变为0，结果是前景物体会变小，
整幅图像的白色区域会减小，这对于去除白噪声很有用，也可以用来分开两个连
在一起的物体
'''
import cv2
import numpy as np

image = cv2.imread('j.png',0)
cv2.imshow('original', image)
print(image.shape)

kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(image, kernel, iterations=1)

cv2.namedWindow('erode',cv2.WINDOW_NORMAL)
cv2.imshow('erode', erosion)
cv2.moveWindow('erode', x=image.shape[1], y=0)

cv2.waitKey(0)
cv2.destroyAllWindows()
