# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 15:10:14 2018

@author: GEAR
"""

'''
自适应阈值：在前边的部分我们使用的是全局阈值， 整幅图像采用同一个数字作为阈值，这种
方法并不适应与所有情况， 尤其是当同一幅图像上的不同部分具有不同亮度时， 这种情况我们
需要采用自适应阈值，此时的阈值是根据图像上的每一个小区域计算与之对应的阈值，因此在同
一幅图像上的不同区域采用的是不同的阈值，从而使我们能在亮度不同的情况下得到更好的结果
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

root = 'D:/python/OpenCV-Python/data/'
image = cv2.imread(root+'sudoku.jpg', 0)
image = cv2.medianBlur(image, 5) # 5为滤波半径

ret, th1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# 11为阈值领域大小，用来计算阈值的区域大小
# 2为C值（常数）， 阈值就等于的平均值或者加权平均值减去这个常数

th2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 2)
th3 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 5, 2)
cv2.imshow('image', th3)
cv2.waitKey(0)
cv2.destroyAllWindows()