# -*- coding=GBK -*-
import cv2 as cv
import numpy as np


def nextrace_object_demo():
    capture = cv.VideoCapture("D:/1.mp4")  # 导入视频
    while True:
        ret, frame = capture.read()
        if ret == False:
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)  # 转换色彩空间为hsv
        # 设置白色的范围，跟踪视频中的白色
        lower_hsv = np.array([0, 0, 221])  # 设置过滤的颜色的低值
        upper_hsv = np.array([180, 30, 255])  # 设置过滤的颜色的高值
        mask = cv.inRange(hsv, lower_hsv,
                          upper_hsv)  # 调节图像颜色信息（H）、饱和度（S）、亮度（V）区间，选择白色区域
        cv.imshow("video", frame)
        cv.imshow("mask", mask)
        c = cv.waitKey(40)
        if c == 27:
            break


nextrace_object_demo()
cv.waitKey(0)
cv.destroyAllWindows()