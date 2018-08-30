# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 21:29:24 2018

@author: GEAR
"""

'''
按位运算：AND, OR, NOT, XOR等，若想把opencv的标志放到另一幅图像上，如果使用加法，
颜色会改变，如果使用混合，会得到透明的效果，这时可以采用按位运算实现
'''

import cv2
import numpy as np

#加载图像
root = 'D:/python/OpenCV-Python/data/'
img1 = cv2.imread(root + 'messi5.jpg')
img2 = cv2.imread(root + 'opencv-logo-white.png')

# 我们想让logo放在图像的左上角，所以我们创建ROI
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

'''
现在创建一个logo的mask,并且创建其的reverse mask
cv2.THRESH_BINARY（黑白二值）,像素高于阈值时，给像素赋予新值，
否则，赋予另外一种颜色。函数是cv2.threshold() 
'''
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY) # mask
mask_inv = cv2.bitwise_not(mask)  # 值全位0

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_bg = cv2.bitwise_and(img2, img2, mask=mask)

dst = cv2.add(img1_bg, img2_bg)
img1[0:rows, 0:cols] = dst

cv2.imshow('img', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()