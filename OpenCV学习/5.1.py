# -*- coding=GBK -*-
import cv2 as cv


# 数值运算：加减乘除
def shu_image(src11, src22):
    src = cv.add(src11, src22)  # 加
    cv.imshow("相加", src)
    src = cv.subtract(src11, src22)  # 减
    cv.imshow("相减", src)
    src = cv.divide(src11, src22)  # 乘
    cv.imshow("相乘", src)
    src = cv.multiply(src11, src22)  # 除
    cv.imshow("相除", src)
    

src1 = cv.imread("C:/01.jpg")
src2 = cv.imread("C:/02.jpg")
cv.imshow("原来1", src1)
cv.imshow("原来2", src2)
shu_image(src1, src2)
cv.waitKey(0)
cv.destroyAllWindows()
