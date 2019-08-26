# -*- coding=GBK -*-
import cv2 as cv
import numpy as np

src = cv.imread("C:/bg.jpg")
cv.namedWindow("原来", cv.WINDOW_NORMAL)
cv.imshow("原来", src)

# 通道分离，输出三个单通道图片
b, g, r = cv.split(src)  # 将彩色图像分割成3个通道
cv.imshow("blue", b)
cv.imshow("green", g)
cv.imshow("red", r)

# 通道合并
src = cv.merge([b, g, r])
cv.imshow("合并", src)

# 修改某个通道的值
src[:, :, 2] = 0
cv.imshow("单通道", src)

cv.waitKey(0)
cv.destroyAllWindows()
