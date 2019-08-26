# -*- coding=GBK -*-
import cv2 as cv
import numpy as np

src = cv.imread("C:/bg.jpg")
cv.namedWindow("ԭ��", cv.WINDOW_NORMAL)
cv.imshow("ԭ��", src)

# ͨ�����룬���������ͨ��ͼƬ
b, g, r = cv.split(src)  # ����ɫͼ��ָ��3��ͨ��
cv.imshow("blue", b)
cv.imshow("green", g)
cv.imshow("red", r)

# ͨ���ϲ�
src = cv.merge([b, g, r])
cv.imshow("�ϲ�", src)

# �޸�ĳ��ͨ����ֵ
src[:, :, 2] = 0
cv.imshow("��ͨ��", src)

cv.waitKey(0)
cv.destroyAllWindows()
