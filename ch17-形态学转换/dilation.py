# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 20:11:56 2018

@author: GEAR
"""

'''
与腐蚀相反，与卷积核对应的图像的像素值中只要有一个是1，中心元素的像素值就是1，所以
这个操作会增加图像中的白色区域（前景）。一般在去噪时先用腐蚀再膨胀。因为腐蚀在去掉
白噪声的同时，也使得前景对象变小，所以我们再对其进行膨胀，这时噪声已经被去掉，但是
前景还会继续增加，膨胀也可以用来连接两个分来的物体
'''
import cv2
import numpy as np

image = cv2.imread('j.png', 0)
cv2.namedWindow('original',cv2.WINDOW_NORMAL)
cv2.imshow('original', image)
print(image.shape)

kernel = np.ones((5,5), np.uint8)
dilation = cv2.dilate(image, kernel, iterations=1)

cv2.namedWindow('dilation',cv2.WINDOW_NORMAL)
cv2.imshow('dilation', dilation)
cv2.moveWindow('dilation', x=image.shape[1], y=0)

cv2.waitKey(0)
cv2.destroyAllWindows()

