# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 21:00:03 2018

@author: GEAR
"""
'''
对于透视变换，我们需要一个3x3的变换矩阵，在变换前后直线还是直线，要构架这个变换矩阵
我们需要在输入图像上找4个点，以及他们在输出图像上对应的位置，这四个点的任意是三个都
不能共线。这个变换矩阵可以由函数cv2.getPerspectiveTransform()构建，然后将这个矩阵
传给函数cv2.warpPerspective
'''
import cv2
import numpy as np
root = 'D:/python/OpenCV-Python/data/'
image = cv2.imread(root + 'sudoku.jpg')

height, width = image.shape[:2]

pts1 = np.float32([[56,65], [368,52], [28, 387], [389, 390]])
pts2 = np.float32([[0,0], [300,0], [0,300], [300,300]])

M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(image, M, (300, 300))

cv2.imshow('dst', dst)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
