# -*- coding=GBK -*-
import cv2 as cv
import numpy as np


# 指定颜色替换
def fill_image(image):
    copyImage = image.copy()  # 复制原图像
    h, w = image.shape[:2]  # 读取图像的宽和高
    mask = np.zeros([h + 2, w + 2], np.uint8)  # 新建图像矩阵  +2是官方函数要求
    cv.floodFill(copyImage, mask, (20,20), (0,255, 255), (10, 10, 10),
                 (10, 10, 10), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("填充", copyImage)


src = cv.imread("C:/bg.jpg")
cv.imshow("原来", src)
fill_image(src)
cv.waitKey(0)
cv.destroyAllWindows()
