# -*- coding= utf-8 -*-
import cv2 as cv


def mo_image(src1):

    src2 = cv.blur(src1, (5, 5))
    cv.imshow("均值模糊", src2)

    src2 = cv.medianBlur(src1, 5)
    cv.imshow("中值模糊", src2)

    src2 = cv.GaussianBlur(src1, (5, 5), 2)
    cv.imshow("高斯模糊", src2)

    src2 = cv.bilateralFilter(src1, 5, 5, 2)
    cv.imshow("双边滤波", src2)


src = cv.imread("C://111111.jpg")
cv.namedWindow("原来", cv.WINDOW_NORMAL)
cv.imshow("原来", src)
mo_image(src)
cv.waitKey(0)
cv.destroyAllWindows()