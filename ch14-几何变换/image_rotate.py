# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 20:07:46 2018

@author: GEAR
"""
'''
图像旋转: cv2.getRotationMatrix2D的第一个参数为旋转中心，第二个为旋转角度，第三个
为旋转后的缩放因子，可以通过设置旋转中心，缩放因子， 以及窗口大小来防止旋转后超出
边界的问题
'''
import cv2
import numpy as np

root = 'D:/python/OpenCV-Python/ImageData/'
image = cv2.imread(root+'IMG_1.jpg', 0)
height, width = image.shape

M = cv2.getRotationMatrix2D((width//2, height//2), 45, 0.5)
dst = cv2.warpAffine(image, M, (width, height)) #第三个参数为输出图像的尺寸大小

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()



