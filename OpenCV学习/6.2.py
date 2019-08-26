# -*- coding=GBK -*-
import cv2 as cv
import numpy as np


# ָ����ɫ�滻
def fill_image(image):
    copyImage = image.copy()  # ����ԭͼ��
    h, w = image.shape[:2]  # ��ȡͼ��Ŀ�͸�
    mask = np.zeros([h + 2, w + 2], np.uint8)  # �½�ͼ�����  +2�ǹٷ�����Ҫ��
    cv.floodFill(copyImage, mask, (20,20), (0,255, 255), (10, 10, 10),
                 (10, 10, 10), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("���", copyImage)


src = cv.imread("C:/bg.jpg")
cv.imshow("ԭ��", src)
fill_image(src)
cv.waitKey(0)
cv.destroyAllWindows()
