# -*- coding=GBK -*-
import cv2 as cv
import numpy as np


# ����ȡ��
def inverse(image):
    dst = cv.bitwise_not(image)
    cv.imshow("ȡ��", dst)


src = cv.imread("C:/bg.jpg")
cv.namedWindow("ԭ��", cv.WINDOW_NORMAL)
cv.imshow("ԭ��", src)
t1 = cv.getTickCount()
inverse(src)
t2 = cv.getTickCount()
time = (t2 - t1) * 1000 / cv.getTickFrequency()
print("time: %s" % time)
cv.waitKey(0)
cv.destroyAllWindows()
