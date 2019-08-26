import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


# 画出图像的直方图
def plot_demo(image):
    plt.hist(image.ravel(), 256, [0, 256])  # image.ravel()将图像展开，256为bins数量，[0, 256]为范围
    plt.show("1")


def hist_image(image):
    color = ("blue", "green", "red")
    for i, color in enumerate(color):
        hist = cv.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show("2")


src = cv.imread("C://bg.jpg")
cv.namedWindow("原来", cv.WINDOW_NORMAL)
cv.imshow("原来", src)
plot_demo(src)
hist_image(src)
cv.waitKey(0)
cv.destroyAllWindows()
