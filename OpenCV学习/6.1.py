# -*- coding=GBK -*-
import cv2 as cv
import numpy as np


# 截取图片中的指定区域或在指定区域添加某一图片
def jie_image(src1):
    src2 = src1[500:600, 500:600]  # 截取第5行到89行的第500列到630列的区域
    cv.imshow("截取", src2)
    src1[200:300, 200:300] = src2  # 指定位置填充，大小要一样才能填充
    cv.imshow("合成", src1)


src = cv.imread("C:/bg.jpg")
cv.imshow("原来", src)
jie_image(src)
cv.waitKey(0)
cv.destroyAllWindows()