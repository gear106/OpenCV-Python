# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 18:01:01 2018

@author: GEAR
"""
'''
均值滤波
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

root = 'D:/python/OpenCV-Python/ImageData/'
image = cv2.imread(root+'IMG_1.jpg',0)

kernel = np.ones((5,5), np.float32) / 25

dst = cv2.filter2D(image, -1, kernel)

plt.subplot(121), plt.imshow(image), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()