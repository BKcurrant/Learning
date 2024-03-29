import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def back_projection_demo():
    sample = cv.imread("C://01.jpg")
    target = cv.imread("C://02.jpg")
    roi_hsv = cv.cvtColor(sample,cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target,cv.COLOR_BGR2HSV)
    cv.imshow("sample", sample)
    cv.imshow("target", target)
    roiHist = cv.calcHist([roi_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
    cv.normalize(roiHist, roiHist, 0, 255, cv.NORM_MINMAX)
    dst = cv.calcBackProject([target_hsv], [0, 1], roiHist, [0, 180, 0, 256], 1)
    cv.imshow("backProjectionDemo", dst)


def hist2d_demo(image):
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hist = cv.calcHist([image], [0, 1], None, [180, 256], [0, 180, 0, 256])
    # cv.imshow("hist2d", hist)
    plt.imshow(hist, interpolation='nearest')
    plt.title("2D Histogram")
    plt.show()


src = cv.imread("C://bg.jpg")
cv.namedWindow("原来", cv.WINDOW_NORMAL)
cv.imshow("原来", src)
# hist2d_demo(src)
back_projection_demo()
cv.waitKey(0)
cv.destroyAllWindows()

