import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


# 创建直方图
def create_rgb_demo(image):
    h, w, c = image.shape
    rgbHist = np.zeros([16*16*16, 1], np.float32)
    bsize = 256 / 16
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            index = np.int(b/bsize)*16*16 + np.int(g/bsize)*16 + np.int(r/bsize)
            rgbHist[np.int(index), 0] = rgbHist[np.int(index), 0] + 1
    return rgbHist


# 利用直方图比较相似性，用巴氏和相关性比较好
def hist_compare(image1, image2):
    hist1 = create_rgb_demo(image1)
    hist2 = create_rgb_demo(image2)
    match1 = cv.compareHist(hist1, hist2, method=cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1, hist2, method=cv.HISTCMP_CORREL)
    match3 = cv.compareHist(hist1, hist2, method=cv.HISTCMP_CHISQR)
    print("巴式距离：%s, 相关性：%s, 卡方：%s"%(match1, match2, match3))


src1 = cv.imread("C://01.jpg")
src2 = cv.imread("C://02.jpg")
cv.imshow("1", src1)
cv.imshow("2", src2)
hist_compare(src1, src2)
cv.waitKey(0)
cv.destroyAllWindows()

