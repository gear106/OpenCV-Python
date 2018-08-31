# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 17:06:56 2018

@author: GEAR
"""
'''
物体跟踪：
现在我们知道如何将一幅图像从BGR转换到HSV中了， 我们可以利用这一点来提取带有某个
特定颜色的物体，在HSV颜色空间中要比在BGR空间中更容易表示一个特定的颜色，我们要提取
某个特定颜色的物体，下边就是我们的步骤：
1.从视频中获取每一帧图像
2.将图像转换到HSV空间
3.设置HSV阈值到蓝色范围
'''
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ret = cap.set(3, 240)
ret = cap.set(4, 240)

#定蓝色的阈值 ,这里要计算将颜色从BGR转换到HSV时的阈值！！！！
lower_blue = np.array([30, 100, 100])
upper_blue = np.array([70, 255, 255])

while True:
    # 获取每一帧图像
    ret, frame = cap.read()
    # 转换到HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # 根据阈值构建掩模
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # 对图像进行和掩模位运算
    res = cv2.bitwise_and(frame, frame, mask=mask)
    
    # 显示图像
    cv2.imshow('frame', frame)
    cv2.moveWindow('frame', x=0, y=0) #原地
    cv2.imshow('mask', mask)
    cv2.moveWindow('mask', x=frame.shape[1], y=0)   #右边
    cv2.imshow('res',res)
    cv2.moveWindow('res', y=frame.shape[0], x=0)    #下边
    
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
# 关闭窗口
cap.release()
cv2.destroyAllWindows()
    
