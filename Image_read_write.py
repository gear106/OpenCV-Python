# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 22:38:46 2018

@author: GEAR
"""

'''
OpenCV读写操作
'''
import numpy as np
import cv2

# 每个像素都由一个8位整数来表示，即每个像素的范围值是0-255
img = np.zeros((100,100), dtype = np.uint8) 
# 利用cv2.cvtColor函数将该图像转换为Blue-green-red(BGR)格式
# cv2.COLOR_GRAY2BGR 颜色空间转换函数
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#-----------------转换图片格式--------------------#
root = 'D:/python/OpenCV-Python/ImageData/'
# image的第一个元素表示像素的y坐标，第二个表示x坐标一般
image = cv2.imread(root+'IMG_1.jpg')
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 获取某一位置像素值得两种方法：
print(image[0,0,0])
print(image.item((0,0,0)))
# 将图片保存为png格式：
cv2.imwrite(root+'IMG_1.png', image)

# 将指定通道的所有像素值设置为0
image[:,:,1] = 0





