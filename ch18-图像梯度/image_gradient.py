# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 20:40:29 2018

@author: GEAR
"""
'''
图像梯度：
OpenCV提供了三种不同的梯度滤波器，或者说高通滤波器:Sobel,Scharr,Laplacian
Sobel,Scharr其实就是求一阶或二阶导，Scharr是对Sobel(使用小的卷积核求解梯度角度时)
的优化。Laplacian是求二阶导数.
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

root = 'D:/python/OpenCV-Python/data/'

image = cv2.imread(root + 'sudoku.jpg',0)
#cv2.CV_64F输出图像的深度（数据类型），可以使用-1，与原图像保持一致np.uint8
laplacian = cv2.Laplacian(image, cv2.CV_64F)
#参数1,0为只在x方向求导，最大可求2阶导数
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
#参数0,1为只在y方向求导
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)

plt.subplot(2,2,1),plt.imshow(image, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])


