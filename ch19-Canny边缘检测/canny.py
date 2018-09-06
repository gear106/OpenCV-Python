# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 09:42:29 2018

@author: GEAR
"""

'''
Canny边缘检测是一种非常流行的边缘检测算法，其由多步构成：
1.噪声去除：由于边缘检测很容易受到噪声的影响，所以第一步是使用5x5的高斯滤波器去除噪声
2.计算梯度图：对平滑后的图像使用Sobel算子计算水平方向和竖直方向的一阶导数，根据得到的这
两幅梯度图找到边界的梯度和方向。
3.非最大值抑制：在获得梯度的方向和大小之后，应该对整幅图像做一个扫描，去除那些非边界上的点
对每一个像素进行检测，看这个点的梯度是不是周围具有相同梯度方向的点中最大的
4.滞后抑制：现在要确定那些边界才是真正的边界，这时我们需要设置两个阈值：minVal和maxVal。
当图像的灰度梯度高于maxVal时被认为是真的边界，那些低于minVal的边界会淘汰，若介于两者之间，
就要看这个点是否与某个被确定为真正的边界点相连，如果是就认为他也是边界点，如果不是就抛弃。

OpenCV中的cv2.Canny()函数第一个参数是输入图像，第二第三个分别是minVal和maxVal，第三个参数
是用来计算图像梯度的Sobel卷积核的大小，默认值为3，最后一个参数是L2gradient,他可以用来设置
求梯度大小的方程。若True，则采用开方的方式求梯度，若False，则采用绝对值方式代替，默认为False
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

root = 'D:/python/OpenCV-Python/data/'
image = cv2.imread(root+'messi5.jpg', 0)
edges = cv2.Canny(image, 50, 200)

cv2.imshow('Edge', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
