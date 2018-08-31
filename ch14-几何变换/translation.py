# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 19:52:19 2018

@author: GEAR
"""
'''
图像平移就是将图像换一个位置，如果要沿着（x,y)方向移动，移动的距离是（tx,ty)
函数cv2.warpAffine()可以完成这个工作，其第三个参数输出的是图像的大小，它的
格式应该是图像的（宽，高），图像的宽对应的是列数，高对应的是行数
'''
import cv2
import numpy as np

root = 'D:/python/OpenCV-Python/ImageData/'
image = cv2.imread(root+'IMG_1.jpg', 0)

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
height, width = image.shape

#图像平移矩阵
M = np.float32([[1, 0, 100], [0, 1, 50]]) #(tx=100, ty=50)

dst = cv2.warpAffine(image, M, (width, height))
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()






