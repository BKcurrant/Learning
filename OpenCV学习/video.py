# -*- coding=GBK -*-
import cv2 as cv


# 打开摄像头获取图片
def video_demo():
    capture = cv.VideoCapture(0)  # 打开摄像头，0代表的是设备id，如果有多个摄像头，可以设置其他数值
    while True:
        ret, frame = capture.read()
        '''读取摄像头,它能返回两个参数，第一个参数是bool型的ret，其值为True或False，
        代表有没有读到图片；第二个参数是frame，是当前截取一帧的图片'''
        frame = cv.flip(frame, 1)  # 翻转 0:上下颠倒 大于0水平颠倒   小于180旋转
        cv.imshow("video", frame)
        c = cv.waitKey(40)
        if c == 27:
            break


video_demo()
cv.destroyAllWindows()


