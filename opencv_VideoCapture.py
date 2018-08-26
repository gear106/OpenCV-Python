# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 16:00:29 2018

5.1 用摄像头捕获视频，p18
@author: GEAR
"""

import numpy as np
import cv2

#为了捕获视频，需要创建一个VdieoCapture对象
cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0,(640, 480))


while(cap.isOpened()):
    #一帧一帧捕获图像
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame,0)
        
        #write the flipped frame
        out.write(frame)
    
    #显示结果帧
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
#最后需要停止捕获视频
cap.release()
out.release()
cv2.destroyAllWindows()

    