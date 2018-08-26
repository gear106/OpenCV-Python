# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 16:35:52 2018

@author: GEAR
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('D:\python\opencv\ImageData\IMG_1.jpg')
px = img[100:150,100:150]
img[200:250,200:250] = px

b,g,r = cv2.split(img)

cv2.imshow('example', img)
cv2.waitKey(0)
cv2.destroyAllWindows()