# -*- coding=GBK -*-
import cv2 as cv


# ɫ�ʿռ��ת��
def color_space_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # RGBת��Ϊgray
    cv.imshow("gray", gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)  # RGBת��Ϊhsv
    cv.imshow("hsv", hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)  # RGBת��Ϊyuv
    cv.imshow("yuv", yuv)


src = cv.imread("C:/bg.jpg")
cv.namedWindow("ԭ��", cv.WINDOW_NORMAL)
cv.imshow("ԭ��", src)
color_space_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()