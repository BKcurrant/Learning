import cv2 as cv
import numpy as np


def bi_demo(src1):
    dst = cv.bilateralFilter(src1, 0, 100, 14)
    cv.imshow("bi_demo", dst)


src = cv.imread("C://11.jpg")
cv.namedWindow("原来", 0)
cv.imshow("原来", src)
bi_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()

