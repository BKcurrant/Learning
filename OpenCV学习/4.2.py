# -*- coding=GBK -*-
import cv2 as cv
import numpy as np


def nextrace_object_demo():
    capture = cv.VideoCapture("D:/1.mp4")  # ������Ƶ
    while True:
        ret, frame = capture.read()
        if ret == False:
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)  # ת��ɫ�ʿռ�Ϊhsv
        # ���ð�ɫ�ķ�Χ��������Ƶ�еİ�ɫ
        lower_hsv = np.array([0, 0, 221])  # ���ù��˵���ɫ�ĵ�ֵ
        upper_hsv = np.array([180, 30, 255])  # ���ù��˵���ɫ�ĸ�ֵ
        mask = cv.inRange(hsv, lower_hsv,
                          upper_hsv)  # ����ͼ����ɫ��Ϣ��H�������Ͷȣ�S�������ȣ�V�����䣬ѡ���ɫ����
        cv.imshow("video", frame)
        cv.imshow("mask", mask)
        c = cv.waitKey(40)
        if c == 27:
            break


nextrace_object_demo()
cv.waitKey(0)
cv.destroyAllWindows()