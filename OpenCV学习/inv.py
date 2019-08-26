# -*- coding=GBK -*-
import cv2 as cv
import numpy as np


# 像素取反
def inverse(image):
    dst = cv.bitwise_not(image)
    cv.imshow("取反", dst)


src = cv.imread("C:/bg.jpg")
cv.namedWindow("原来", cv.WINDOW_NORMAL)
cv.imshow("原来", src)
t1 = cv.getTickCount()
inverse(src)
t2 = cv.getTickCount()
time = (t2 - t1) * 1000 / cv.getTickFrequency()
print("time: %s" % time)
cv.waitKey(0)
cv.destroyAllWindows()
