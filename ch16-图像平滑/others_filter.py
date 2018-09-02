# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 18:14:02 2018

@author: GEAR
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

root = 'D:/python/OpenCV-Python/ImageData/'
image = cv2.imread(root+'IMG_1.jpg',0)

# 平均滤波
dst1 = cv2.blur(image, (5,5))
# 这里也可以使用cv2.boxFilter()来实现
dst4 = cv2.boxFilter(image, -1, (5,5)) # 结果同dst1

# 高斯模糊
dst2 = cv2.GaussianBlur(image, (5,5), 0) # 0表示来计算窗口大小5x5高斯函数的标准差

#中值模糊
#这里的5表示孔径的尺寸， 一个大于1的奇数，这里表示采用5x5的范围来计算
dst3 = cv2.medianBlur(image, 5)

#双边滤波
#cv2.bilateralFilter()能在保持边界清晰的情况下与有效的去除噪声，但这种滤波速度慢
dst5 = cv2.bilateralFilter(image, 9, 75, 75)

plt.subplot(221), plt.imshow(image), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(222), plt.imshow(dst1), plt.title('Averaging')
plt.xticks([]), plt.yticks([])

plt.subplot(223), plt.imshow(dst2), plt.title('Gaussian')
plt.xticks([]), plt.yticks([])

plt.subplot(224), plt.imshow(dst3), plt.title('median')
plt.xticks([]), plt.yticks([])
plt.show()
