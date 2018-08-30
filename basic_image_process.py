# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 15:49:25 2018

@author: GEAR
"""

import cv2
import numpy as np

#图片地址
root = 'D:/python/OpenCV-Python/ImageData/'
image1 = cv2.imread(root+'IMG_1.jpg')

#获取像素值
image1[100,100] #获取BGR三个值
image1[100,100,0] #获取B值
image1.item(100,100, 0)

#修改像素值
image1[100,100,0] = 255             #方法1
image1.itemset((100,100,0), 10)     #方法2

#像素大小
print(image1.size)

#拆分图像通道
b,g,r = cv2.split(image1) # 这个操作比较耗时！！！
#推荐下边这种操作
b = image1[:,:,0]
g = image1[:,:,1]
r = image1[:,:,2]

# 合并图像通道
image2 = cv2.merge([b, g, r]) # 这里要加[],防止出错

# 为图像添加边的不同方式
BLUE = [255, 0, 0]
replicate = cv2.copyMakeBorder(image1, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(image1, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(image1, 10, 10, 10, 10, cv2.BORDER_REFLECT101)
wrap = cv2.copyMakeBorder(image1, 10, 10, 10, 10, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(image1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=BLUE)
cv2.imshow('replicate', constant)
cv2.waitKey(0)
cv2.destroyAllWindows()

