# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 10:27:56 2018

@author: GEAR
"""
'''
OpenCV 和 matplotlib显示图片问题：cv2读入的图片默认是BGR顺序的，而matplotlib是
RGB顺序的，所以如果cv2读入的图片用matplotlib显示会有问题，解决方案如下：
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

#图片地址
root = 'D:/python/OpenCV-Python/ImageData/'
image1 = cv2.imread(root+'IMG_1.jpg')
b,g,r = cv2.split(image1)

image2 = cv2.merge([r,g,b])
plt.subplot(121);plt.imshow(image1)  #显示有问题
plt.subplot(122);plt.imshow(image2)  #显示正常
plt.show()

cv2.imshow('bgr image', image1)
cv2.imshow('rgb image', image2)
cv2.waitKey()
cv2.destroyAllWindows()