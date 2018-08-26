# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 14:53:59 2018

demo: 图片的读取和保存
@author: GEAR
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('D:\python\opencv\ImageData\IMG_1.jpg',0)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destoryAllWindows()
elif k == ord('s'):
    cv2.imwrite('IMG_1.png', img)
    cv2.destroyAllWindows()

