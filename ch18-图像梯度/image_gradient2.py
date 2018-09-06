# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 22:19:43 2018

@author: GEAR
"""
'''
虽然我们可以通过参数-1来设定输出图像的深度（数据类型）与原图像保持一致，但是我们在
代码里一般用cv2.CV_64F，这是因为比如从黑到白的边界的导数是整数，而一个从白到黑的边界
点导数是负数，如果原图的深度是np.int8时，所有的负值都会被截断为0，这样会导致把边缘
丢失掉。若我们想把这两种边界都检测到，最好的办法是将输入的数据类型设置的更高，比如
cv2.CV_16S, cv2.CV_64F等，取绝对值然后再把它转回到cv2.CV_8U.
下边是输出图片的深度不同造成的不同效果：
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

root = 'D:/python/OpenCV-Python/data/'
image = cv2.imread(root+'box.jpg',0)

sobelx8u = cv2.Sobel(image, cv2.CV_8U, 1, 0, ksize=5)
sobelx64f = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)

abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)

plt.subplot(1,3,1), plt.imshow(image, cmap='gray')
plt.title('original'), plt.xticks([]), plt.yticks([])

plt.subplot(1,3,2), plt.imshow(sobelx8u, cmap='gray')
plt.title('sobelx8u'), plt.xticks([]), plt.yticks([])

plt.subplot(1,3,3), plt.imshow(sobelx64f, cmap='gray')
plt.title('sobelx64f'), plt.xticks([]), plt.yticks([])
