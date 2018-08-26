# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 16:26:17 2018

@author: GEAR
"""

import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8)

cv2.line(img,(0,0),(511,511), (255,0,0),5)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10,500), font, 4, (255,255,255),2)
winname = 'example'
cv2.namedWindow(winname)
cv2.imshow(winname,img)
cv2.waitKey()
cv2.destroyWindow(winname)
