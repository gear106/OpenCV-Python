# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 19:27:15 2018

@author: GEAR
"""
'''
图像扩展缩放只是改变图像的尺寸大小，OpenCV的cv2.resize()函数可以实现这个功能
在缩放时我们一般使用cv2.INTER_AREA,在扩展时我们使用cv2.INTRE_CUBIC(慢)和
cv2.INTER_LINEAR,默认情况下所有改变图像尺寸大小的操作使用的插值方法都是cv2.INTER_LINEAR
'''
import cv2
import numpy as np

root = 'D:/python/OpenCV-Python/ImageData/'
image = cv2.imread(root+'IMG_1.jpg')
#下边的None本应该是输出图像的尺寸，但是因为我们后边设置了缩放因子，因此这里为None
res1 = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

#下边我们直接设置了输出图像尺寸，所以不用设置缩放因子
height, width = image.shape[:2]
res2 = cv2.resize(image, (2*width, 2*height), interpolation=cv2.INTER_LINEAR)

# 将图像缩小为原来的一半
res3 = cv2.resize(image, (width//2, height//2), interpolation=cv2.INTER_AREA)


cv2.imshow('image', image)
cv2.imshow('res1', res1)
cv2.imshow('res2', res2)
cv2.imshow('res3', res3)

cv2.waitKey(0)
cv2.destroyAllWindows()
