# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 17:03:19 2018

@author: GEAR
"""
import cv2
import numpy as np

'''
10 图像上的算术运算
'''

'''
可以使用函数cv2.add()将两幅图像进行加法运算，也可以直接使用numpy, res = img1 + img2
两幅图像的大小，类型必须一致，或第二个图像可以使用标量值，OpenCV中的加法是一种饱和操作
而numpy中的加法是一种模操作, OpenCV的结果会更好一点
'''
x = np.uint8 ([250])
y = np.uint8([10])
print(cv2.add(x, y))  # 250 + 10 = 260 => 255
print(x+y)            # 250 + 10 = 260 % 256 = 4

'''
图像混合： g(x) = (1+a)*f(x) + a*h(x), 其中a(0~1),把两幅图像混合到一起，第一幅权重为
1+a, 第二幅为a
'''
root = 'D:/python/OpenCV-Python/data/'
img1 = cv2.imread(root+'ml.png')
img2 = cv2.imread(root+'ml.png')
dst  = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)  # 这里需要两幅图像大小相同
cv2.imshow('img2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()




