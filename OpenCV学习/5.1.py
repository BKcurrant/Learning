# -*- coding=GBK -*-
import cv2 as cv


# ��ֵ���㣺�Ӽ��˳�
def shu_image(src11, src22):
    src = cv.add(src11, src22)  # ��
    cv.imshow("���", src)
    src = cv.subtract(src11, src22)  # ��
    cv.imshow("���", src)
    src = cv.divide(src11, src22)  # ��
    cv.imshow("���", src)
    src = cv.multiply(src11, src22)  # ��
    cv.imshow("���", src)
    

src1 = cv.imread("C:/01.jpg")
src2 = cv.imread("C:/02.jpg")
cv.imshow("ԭ��1", src1)
cv.imshow("ԭ��2", src2)
shu_image(src1, src2)
cv.waitKey(0)
cv.destroyAllWindows()
