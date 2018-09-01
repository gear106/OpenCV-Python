# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 08:37:55 2018

@author: GEAR
"""
'''
简单阈值：当像素值高于阈值时，我们给这个像素赋予一个新值（可能是白色），否则我们给他赋予
另外一种颜色（也许是黑色）。这个函数就是cv2.threshhold(),这个函数的第一个参数就是原图像
原图像应该是灰度图，第二个参数就是用来对像素值进行分类的阈值，第三个参数就是当像素值高于
（有时是低于）阈值时应该被赋予新的像素值，此外还有第四个可选参数
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('grey-gradient.jpg', 0)

ret, thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV) #做相反操作
ret, thresh3 = cv2.threshold(image, 127, 255, cv2.THRESH_MASK)
ret, thresh4 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
ret, thresh5 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)

title = ['Original', 'BINARY', 'BINARY_INV', 'MASK', 'TRUNC', 'TOZERO_INV']
images = [image, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.xticks([]), plt.yticks([])
plt.show()


cv2.imshow('thresh1', thresh1)

cv2.waitKey(0)
cv2.destroyAllWindows()
