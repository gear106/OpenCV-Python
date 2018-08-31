# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 20:21:26 2018

@author: GEAR
"""
'''
仿射变换，在仿射变换中，原图中所有的平行直线在结果中也是平行的，为了创建这个矩阵
我们需要从原图像中找到三个点以及他们在图像中的位置，然后cv2.getAffineTransform
会创建一个2x3的矩阵，最后这个矩阵会被传给函数cv2.warpAffine
'''
import cv2
import numpy as np

image = cv2.imread('drawing.png')
height, width = image.shape[:2]

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])   #变换前三点的坐标
pts2 = np.float32([[10, 100], [200, 50], [100, 250]]) #变换后对应坐标

M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(image, M, (width, height))

cv2.imshow('image', image)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()