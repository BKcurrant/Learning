# -*- coding=GBK -*-
import cv2 as cv
import numpy as np


# ��ȡͼƬ�е�ָ���������ָ���������ĳһͼƬ
def jie_image(src1):
    src2 = src1[500:600, 500:600]  # ��ȡ��5�е�89�еĵ�500�е�630�е�����
    cv.imshow("��ȡ", src2)
    src1[200:300, 200:300] = src2  # ָ��λ����䣬��СҪһ���������
    cv.imshow("�ϳ�", src1)


src = cv.imread("C:/bg.jpg")
cv.imshow("ԭ��", src)
jie_image(src)
cv.waitKey(0)
cv.destroyAllWindows()