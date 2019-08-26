# -*- coding=GBK -*-
import cv2 as cv


# 逻辑运算：与或非的操作
def luo_image(src11, src22):
    src = cv.bitwise_and(src11, src22)  # 与 两张图片同一位置的色素两个值均不为零的才会有输出
    cv.imshow("与", src)
    src = cv.bitwise_or(src11, src22)  # 或 两张图片同一位置的色素两个值不全为零的才会有输出
    cv.imshow("或", src)
    src = cv.bitwise_not(src11)  # 非 对一张图片操作  取反
    cv.imshow("非", src)
    src = cv.bitwise_xor(src11, src22)  # 异或 两张图片同一位置的色素两个值有一个为零，另一个不为零才会输出
    cv.imshow("异或", src)


src1 = cv.imread("C:/01.jpg")
src2 = cv.imread("C:/02.jpg")
cv.imshow("原来1", src1)
cv.imshow("原来2", src2)
luo_image(src1, src2)
cv.waitKey(0)
cv.destroyAllWindows()
