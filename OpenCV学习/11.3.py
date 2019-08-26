import cv2 as cv
import numpy as np


# 将大图片拆分成小图片后再用自适应局部阈值比较好
def big_image_demo(image):
    print(image.shape)
    cw = 200
    ch = 200
    h, w = image.shape[:2]
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("gray", gray)
    # 将一张图片每隔ch * cw分成一份
    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gray[row:row+ch, col:col+cw]
            dst = cv.adaptiveThreshold(roi, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 127, 2)
            gray[row:row + ch, col:col + cw] = dst
            print(np.std(dst), np.mean(dst))
    cv.imshow("1", gray)


src = cv.imread("C://bg.jpg")
big_image_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()